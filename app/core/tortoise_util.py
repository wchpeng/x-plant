import tortoise


async def execute_manual_sql(sql, args=None, connect_name='slave'):
    """手工执行sql"""
    conn = tortoise.Tortoise.get_connection(connect_name)
    result = await conn.execute_query_dict(sql, args)
    # print('get_default_manual_sql:')
    # print(f'sql: {sql}, args: {args}')
    # print(f'result: {result}')
    return result
