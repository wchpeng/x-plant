import os
from fastapi import APIRouter, Depends, Body, UploadFile, File
from app.core import (
    router_util,
    response_util,
    dependencies,
    token_util,
    pyutil
)
from app.models import (
    account as account_model
)
router = APIRouter(route_class=router_util.LogRoute)


@router.post(
    path='/account/login/v1',
    description='登录',
    response_class=response_util.MallResponseClass
)
async def login(
        username: str = Body(..., embed=True, description='账号'),
        password: str = Body(..., embed=True, description='密码')
):
    user = await account_model.User.get_or_none(username=username, password=password)
    if not user:
        return response_util.MallResponse.auth_err('账号或密码错误')

    payload = {'userid': user.id, 'username': user.username}

    return {
        'token': token_util.jwt_encode(payload),
        'nickname': user.username
    }


@router.post(
    path='/account/self-info/v1',
    description='当前用户信息',
    response_class=response_util.MallResponseClass
)
async def api_wxmini_login(user=Depends(dependencies.login_user)):
    if not user:
        return response_util.MallResponse.auth_err()
    return user


@router.post(
    path='/account/register/v1',
    description='注册用户',
    response_class=response_util.MallResponseClass
)
async def api_register_account(
        username: str = Body(..., min_length=1, max_length=20, description='注册用户'),
        password: str = Body(..., min_length=5, max_length=50, description='注册密码'),
):
    if await account_model.User.filter(username=username).exists():
        return response_util.MallResponse.info_err('用户名已注册')
    await account_model.User.create(username=username, password=password)
    return {}


@router.post(
    path='/account/upload/v1',
    description="上传图片",
    response_class=response_util.MallResponseClass
)
async def api_upload_image(file: UploadFile = File(None)):
    filename = file.filename
    suffix = filename.split('.')[-1]
    new_name = pyutil.generate_alias()
    with open(f'{os.path.join("data", "static", new_name)}.{suffix}', 'wb') as f:
        f.write(await file.read())

    return {'url': f'/static/{new_name}.{suffix}'}
