import time
from datetime import datetime, timedelta, timezone

TZ = timezone(timedelta(hours=8))


def ts():
    return int(time.time())


def now():
    return datetime.now(tz=TZ)


def now_dt():
    return int(now().strftime('%Y%m%d'))


def now_offset(days=0, hours=0, minutes=0, seconds=0):
    return now() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


def now_offset_str(days=0, hours=0, minutes=0, seconds=0, fmt='%Y-%m-%d %H:%M:%S'):
    return now_offset(days, hours, minutes, seconds).strftime(fmt)


def now_str(fmt='%Y-%m-%d %H:%M:%S'):
    return now().strftime(fmt)


def now_hour(offset_seconds=0):
    """现在小时"""
    return now_offset(seconds=offset_seconds).strftime('%Y%m%d%H')


def exp_10min():
    return int(time.time()/600)


def utc_now():
    return datetime.utcnow()
