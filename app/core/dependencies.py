from fastapi import Header
from fastapi.requests import Request
from app.core import token_util, response_util


def login_user(request: Request, authorization=Header(None)):
    if not authorization:
        return None
    try:
        token = authorization.split(' ')[-1]
        if len(token) < 20:
            return None
        user = token_util.jwt_decode(token)
    # except token_util.jwt.exceptions.ExpiredSignatureError:
    #     raise response_util.MallResponseException(code=400, debug_msg='token已过期', msg='token已过期')
    except Exception as e:
        print('登录token错误：', str(e))
        return None

    request.headers._list.append((b'uid', str(user['userid']).encode()))  # 给请求头里添加 header: uid
    return user


# async def login_user(request: Request, authorization=Header(None)):
#     if not authorization:
#         return None
#
#     check_success, userinfo = await token_util.Token.check_token(authorization)
#     if check_success:
#         request.headers._list.append((b'uid', str(userinfo['userid']).encode()))  # 给请求头里添加 header: uid
#         return userinfo
#
#     return None


# async def anchor_user(userinfo=Depends(login_user)):
#     """主播用户"""
#     if not userinfo or userinfo['role'] not in [enums.Role.anchor, enums.Role.sub_anchor]:
#         return None
#     return userinfo
