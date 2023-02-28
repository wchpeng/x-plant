import time
import traceback

from app.config.settings import setting
from fastapi.routing import APIRoute
from fastapi.exceptions import ValidationError
from app.core import logging_util, alarm_util
from app.core.response_util import MallResponseException, MallResponseClass


class LogRoute(APIRoute):
    def get_route_handler(self):
        origin_route_handler = super(LogRoute, self).get_route_handler()

        async def custom_route_handler(request):
            request_body_bytes = await request.body()
            request_body = request_body_bytes.decode() if len(request_body_bytes) < 100000 else ''

            request_scope = {
                'method': request.scope['method'],
                'path': request.scope['path'],
                'query_string': request.scope['query_string'].decode(),
            }
            request_headers = dict(request.headers)
            t = time.time()

            try:
                response = await origin_route_handler(request)
                request_headers = dict(request.headers)
                response_body = response.body.decode()
                ext_json = {'cost_time': round(time.time() - t, 3)}

                logging_util.log_request_info(
                    request_headers=request_headers,
                    request_scope=request_scope,
                    request_body=request_body,
                    response_body=response_body,
                    ext_json=ext_json
                )

                return response
            except MallResponseException as e:
                code = e.code
                msg = e.msg
                debug_msg = e.debug_msg
                data = e.data
                traceback.print_exc()
            except ValidationError as e:
                code = 422
                msg = '服务异常'
                data = e.errors()
                debug_msg = '参数验证错误\n' + ','.join([f'{".".join([str(j) for j in i["loc"]])}: {i["msg"]}' for i in data])
                traceback.print_exc()
            except Exception as e:
                code = 499
                msg = '服务异常'
                debug_msg = str(e)
                data = traceback.format_exc()
                traceback.print_exc()

            ext_json = {'cost_time': round(time.time() - t, 3)}
            content = {'code': code, 'msg': msg}
            debug_content = {'code': code, 'msg': debug_msg, 'data': data}
            if setting.debug:
                print(debug_msg)

            logging_util.log_request_info(
                request_headers=request_headers,
                request_scope=request_scope,
                request_body=request_body,
                response_body=content,
                ext_json=ext_json
            )
            logging_util.log_request_error(
                request_headers=request_headers,
                request_scope=request_scope,
                request_body=request_body,
                response_body=debug_content,
                ext_json=ext_json
            )
            if not setting.debug and code not in (400, 401, 422):
                alarm_util.alarm(f'plant：\n\nscope:{request_scope}\nheaders:{request_headers}\n请求体:{request_body}\n错误:{debug_msg}')

            return MallResponseClass(content=content if not setting.debug else debug_content)

        return custom_route_handler
