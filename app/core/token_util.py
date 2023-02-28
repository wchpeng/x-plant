import jwt
import time

secret = '57b6d20f'


def jwt_decode(token):
    return jwt.decode(jwt=token, key=secret, algorithms=['HS256'])


def jwt_encode(payload: dict, expire_seconds: int = 7*24*3600):
    payload['exp'] = int(time.time()) + expire_seconds
    return jwt.encode(payload, secret, algorithm="HS256")


if __name__ == '__main__':
    # result = jwt_decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOjEwMDA1LCJ1c2VybmFtZSI6Ilx1NGU3MFx1NjI0Ylx1NTJhOVx1NzQwNlx1NTNmN1x1ZDgzY1x1ZGYxZiIsInVuaW9uaWQiOiJvSlZDTXdtTmJDMnYtX2ZlUkRLajJldzBzYzM4Iiwib3BlbmlkIjoib3Iya181UU0wWHdnVWtnNlg1a2lLUThpalZSbyIsInR5cGUiOiJ3eG1pbmkiLCJleHAiOjE2OTA0NjM2ODV9.NNPI75hYmQrgTHgy-twTOYf1noIAO8z2UZh4ajMmll8')
    # result = jwt_decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOjEwNzY2LCJ1c2VybmFtZSI6Ilx1ODJiOSIsInVuaW9uaWQiOiJvSlZDTXdoQ2tfMlI0VFkyWThWamFJZnA4MEVFIiwib3BlbmlkIjoib3Iya181WHl1NDllMW5pVWlzamR2Yi1iOWJ5MCIsInR5cGUiOiJ3eG1pbmkiLCJleHAiOjE2NjE5NDYwMTl9.LcopXS1dZPg_w1pPxt7SAH31uDRy7EOIGBwJ4lAVIQU')
    # result = jwt_decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOjYzNDMsInVzZXJuYW1lIjoiIiwidW5pb25pZCI6Im9KVkNNd3ZPNmZob1FFc1RYZ3M0aTJLbjU0NkEiLCJvcGVuaWQiOiJvWG5DRDVMS3NmNjdBN1ZjVlhhMkt2UFR2UWVjIiwibGl2ZV91c2VyaWQiOiIiLCJleHAiOjE2NjgzNzU0MjB9.Q81726QaXe-dMXIypp9ZliSfcRzvsj9gT0cIhBxx01o')
    result = []
    print(result)
