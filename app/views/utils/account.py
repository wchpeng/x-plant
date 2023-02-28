from app.config.settings import setting
from app.models import (
    account as account_model,
    qiyewx as qiyewx_model
)


async def get_openid_by_userids(userids):
    """通过用户的userids获取对应小程序商城的openid
    :param userids: List[str] 用户ids
    :return List[str] openids
    """
    _type = 3 if 'KD' in setting.mall_env else 2
    unionids = await account_model.User.filter(id__in=userids).values_list('wx_unionid', flat=True)
    openids = await qiyewx_model.WxThird.filter(unionid__in=unionids, type=_type).values_list('openid', flat=True)
    return openids
