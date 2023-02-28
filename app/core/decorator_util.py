"""装饰器"""
import time
import functools


# 同步函数：限制函数执行的qps
def qps(count):
    def decorator(function):
        function.__last_exec_timestamp = int(time.time())
        function.__exec_count = 0

        @functools.wraps(function)
        def inner(*args, **kwargs):
            now_timestamp = int(time.time())
            # 如果当前描述执行的次数 >= qps限制，不再执行
            if now_timestamp == function.__last_exec_timestamp:
                if function.__exec_count >= count:
                    print('overflow')
                    return

                function.__exec_count += 1
            else:
                function.__last_exec_timestamp = now_timestamp
                function.__exec_count = 1

            return function(*args, **kwargs)

        return inner
    return decorator


# 异步函数：限制函数执行的qps
def async_qps(count):
    def decorator(function):
        function.__last_exec_timestamp = int(time.time())
        function.__exec_count = 0

        @functools.wraps(function)
        async def inner(*args, **kwargs):
            now_timestamp = int(time.time())
            # 如果当前描述执行的次数 >= qps限制，不再执行
            if now_timestamp == function.__last_exec_timestamp:
                if function.__exec_count >= count:
                    print('overflow')
                    return

                function.__exec_count += 1
                result = await function(*args, **kwargs)
            else:
                function.__last_exec_timestamp = now_timestamp
                function.__exec_count = 1
                result = await function(*args, **kwargs)

            return result

        return inner
    return decorator


if __name__ == '__main__':
    import asyncio
    # asyncio.run(asyncio.gather(a_test(), a_test(), a_test(), a_test(), a_test(), a_test()))

    @qps(3)
    def test():
        print('test')


    @async_qps(3)
    async def a_test():
        print('a_test')


    for i in range(6):
        # test()
        time.sleep(0.2)
        asyncio.run(a_test())
