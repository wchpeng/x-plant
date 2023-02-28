import time
from fastapi import APIRouter, Depends, Body, Header, Query
from app.schemas import (
    rhizome as rhizome_schema
)
from app.core import (
    router_util,
    response_util,
    dependencies,
    token_util,
)
from app.models import (
    account as account_model,
    rhizome as rhizome_model,
)

router = APIRouter(route_class=router_util.LogRoute)


@router.get(
    path='/rhizome-list/v1',
    description='作品列表',
    response_model=rhizome_schema.RhizomeListSchema,
    response_class=response_util.MallResponseClass
)
async def api_mobile_login(
        name: str = Query('', description='名字'),
        page_no: int = Query(..., description='页码'),
        page_size: int = Query(..., description='每页条数'),
        user=Depends(dependencies.login_user)
):
    if not user:
        return response_util.MallResponse.auth_err()

    queryset = rhizome_model.Rhizome.filter(is_deleted=False)
    if name:
        queryset = queryset.filter(name__contains=name)
    total = await queryset.count()
    _list = await queryset.order_by('-id').offset((page_no-1)*page_size).limit(page_size).values()

    return {'total': total, 'list': _list}


@router.get(
    path='/rhizome-detail/v1',
    description='作品详情',
    response_model=rhizome_schema.RhizomeListItemSchema,
    response_class=response_util.MallResponseClass
)
async def api_rhizome_detail(
        rhizome_id: str = Query(..., description='作品id'),
        user=Depends(dependencies.login_user)
):
    if not user:
        return response_util.MallResponse.auth_err()

    rhizome = await rhizome_model.Rhizome.get_or_none(id=rhizome_id)
    if not rhizome:
        return response_util.MallResponse.info_err('数据不存在')

    return rhizome.__dict__


@router.post(
    path='/add-rhizome/v1',
    description='添加作品',
    response_class=response_util.MallResponseClass
)
async def api_rhizome_detail(
        name: str = Body(..., embed=True, description='作品名字'),
        desc: str = Body('', embed=True, description='作品详情'),
        model1: list = Body(..., embed=True, description='整体模型'),
        model2: list = Body(..., embed=True, description='单根模型'),
        model3: list = Body(..., embed=True, description='实体模型'),
        model4: list = Body(..., embed=True, description='仪器计算模型'),
        user=Depends(dependencies.login_user)
):
    if not user:
        return response_util.MallResponse.auth_err()

    if await rhizome_model.Rhizome.filter(name=name).exists():
        return response_util.MallResponse.info_err('名字已存在')
    await rhizome_model.Rhizome.create(
        name=name,
        desc=desc,
        model1=model1,
        model2=model2,
        model3=model3,
        model4=model4,
    )

    return {}


@router.put(
    path='/modify-rhizome/v1',
    description='修改作品',
    response_class=response_util.MallResponseClass
)
async def api_rhizome_detail(
        rhizome_id: int = Body(..., embed=True, description='作品id'),
        name: str = Body(None, embed=True, description='作品名字'),
        desc: str = Body(None, embed=True, description='作品详情'),
        model1: list = Body(None, embed=True, description='整体模型'),
        model2: list = Body(None, embed=True, description='单根模型'),
        model3: list = Body(None, embed=True, description='实体模型'),
        model4: list = Body(None, embed=True, description='仪器计算模型'),
        user=Depends(dependencies.login_user)
):
    if not user:
        return response_util.MallResponse.auth_err()

    rhizome = await rhizome_model.Rhizome.get_or_none(id=rhizome_id)
    if not rhizome:
        return response_util.MallResponse.data_not_exist()

    if name is not None:
        rhizome.name = name

    if name is not None:
        rhizome.name = name
    if desc is not None:
        rhizome.desc = desc
    if model1 is not None:
        rhizome.model1 = model1
    if model2 is not None:
        rhizome.model2 = model2
    if model3 is not None:
        rhizome.model3 = model3
    if model4 is not None:
        rhizome.model4 = model4
    await rhizome.save()

    return {}


@router.delete(
    path='/delete-rhizome/v1',
    description='删除作品',
    response_class=response_util.MallResponseClass
)
async def api_delete_rhizome(
        rhizome_id: int = Query(..., description='作品id'),
        user=Depends(dependencies.login_user)
):
    if not user:
        return response_util.MallResponse.auth_err()

    await rhizome_model.Rhizome.filter(id=rhizome_id).update(is_deleted=True)
    return {}
