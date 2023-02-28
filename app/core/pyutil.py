import time
import uuid
import string
import random
import hashlib


def _generate_id():
    cursor, cursor_ts = 0, 0

    def get_id():
        nonlocal cursor, cursor_ts
        ts = int(time.time() * 100 - 1640966400*100)

        if cursor_ts == ts:
            cursor += 1
            if cursor > 99:
                cursor = random.randint(1, 50)
                time.sleep(0.01)
                ts = int(time.time() * 100 - 1640966400*100)
        else:
            cursor = random.randint(1, 50)
        cursor_ts = ts
        _id = f'{ts}{"%02d" % cursor}'
        return int(_id)
    return get_id


def generate_id2():  # 生成 tag-id
    return int(time.time()*1000) - 1640966400000


generate_id = _generate_id()  # 生成 sku-id


def generate_item_id():  # 生成 item-id
    ts = int(time.time() * 100 - 164096640000)
    return int(f'{ts}{random.randint(10, 99)}')


def generate_alias():
    return ''.join(random.choices(string.ascii_letters+string.digits, k=12))


def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode())
    return md5.hexdigest()


def generate_digits(length: int = 6):
    return ''.join(random.choices(string.digits, k=length))


def get_uuid(length=24):
    """获取最长32位的ID"""
    _uuid = ''.join(str(uuid.uuid4()).split('-'))
    return _uuid[:length]
