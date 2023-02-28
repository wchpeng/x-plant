import orjson
from fastapi.responses import ORJSONResponse
from app.core import alarm_util


class MallResponseException(Exception):
    def __init__(self, code, debug_msg, msg, data=None, *args):
        self.code = code
        self.msg = msg
        self.debug_msg = debug_msg
        self.data = data
        super(MallResponseException, self).__init__(*args)


class MallResponseClass(ORJSONResponse):
    def render(self, content):
        if isinstance(content, (dict, list)) and ('code' not in content or not isinstance(content['code'], int)):
            content = {'code': 0, 'msg': 'success', 'data': content}
        return orjson.dumps(content)


def success_response(data=None):
    return ORJSONResponse(content={'code': 0, 'msg': 'success', 'data': data})


def error_response(code=499, msg='', data=None):
    return ORJSONResponse(content={'code': code, 'msg': msg, 'data': data})


class MallError:
    @classmethod
    def auth_err(cls, msg='请先登录'):
        return MallResponseException(code=400, debug_msg=msg, msg='请先登录')

    @classmethod
    def permission_denied(cls, msg='无权限'):
        return MallResponseException(code=401, debug_msg=msg, msg='无权限')


class MallResponse:
    @classmethod
    def auth_err(cls, msg='请先登录'):
        return error_response(code=400, msg=msg)

    @classmethod
    def info_err(cls, msg='信息错误'):
        return error_response(code=410, msg=msg)

    @classmethod
    def data_not_exist(cls, msg='数据不存在'):
        return error_response(code=404, msg=msg)

    @classmethod
    def lack_params(cls, msg='缺少参数'):
        return error_response(code=405, msg=msg)

    @classmethod
    def data_existed(cls, msg='数据已存在'):
        return error_response(code=411, msg=msg)

    @classmethod
    def over_limit(cls, msg='超出限制'):
        return error_response(code=420, msg=msg)

    @classmethod
    def data_validation_error(cls, msg='数据验证错误'):
        return error_response(code=412, msg=msg)

    @classmethod
    def rpc_error(cls, msg='rpc error'):
        return error_response(code=601, msg=msg)

    @classmethod
    def sensitive_words_error(cls, msg='含有敏感词'):
        return error_response(code=602, msg=msg)

    @classmethod
    def db_err(cls, msg='数据错误'):
        return error_response(code=799, msg=msg)

    @classmethod
    def pay_err(cls, msg='支付异常'):
        alarm_util.alarm(f'damai-mall 支付：\n{msg}')
        return error_response(code=801, msg=msg)

    @classmethod
    def unknown(cls, msg='未知错误'):
        return error_response(code=999, msg=msg)
