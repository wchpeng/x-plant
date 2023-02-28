import sys
import json
import socket
import threading
from loguru import logger
from app.core import time_util

logger.remove(handler_id=None)
logger.add(sys.stdout, format='{message}')


def logger_debug(msg):
    data = {
        'level': 'DEBUG',
        'datetime': time_util.now_str('%Y-%m-%d %H:%M:%S.%f'),
        "host": socket.gethostname(),
        'msg': msg
    }
    logger.debug(json.dumps(data, separators=(',', ':'), ensure_ascii=False))


def log_request_info(request_headers, request_scope, request_body, response_body, ext_json):
    data = {
        'level': 'INFO',
        'datetime': time_util.now_str('%Y-%m-%d %H:%M:%S.%f'),
        "host": socket.gethostname(),
        'data': {
            'headers': request_headers,
            'scope': request_scope,
            'request_body': request_body,
            'response_body': response_body,
            'ext_json': ext_json
        }
    }
    logger.info(json.dumps(data, separators=(',', ':'), ensure_ascii=False))


def log_request_error(request_headers, request_scope, request_body, response_body, ext_json):
    data = {
        'level': 'ERROR',
        'datetime': time_util.now_str('%Y-%m-%d %H:%M:%S.%f'),
        "host": socket.gethostname(),
        'data': {
            'headers': request_headers,
            'scope': request_scope,
            'request_body': request_body,
            'response_body': response_body,
            'ext_json': ext_json
        }
    }
    logger.error(json.dumps(data, separators=(',', ':'), ensure_ascii=False))


async def log_request_info2(request, response):
    content_type = request.headers.get('content-type')
    if content_type != 'application/json':
        request_body = ''
    else:
        request_body = (await request.body()).decode()

    request_scope = {
        'method': request.scope['method'],
        'path': request.scope['path'],
        'query_string': request.scope['query_string'].decode(),
    }
    # request_headers = {
    #     'content-length': request.headers.get('content-length'),
    #     'user-agent': request.headers.get('user-agent'),
    #     'authorization': request.headers.get('authorization'),
    #     'content-type': request.headers.get('content-type'),
    # }
    request_headers = dict(request.headers)
    response_body = response.body.decode()
    ext_json = {'cost_time': 0}
    log_request_info(
        request_headers=request_headers,
        request_scope=request_scope,
        request_body=request_body,
        response_body=response_body,
        ext_json=ext_json
    )
