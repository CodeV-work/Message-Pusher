import time
import requests

from config import appID, appsecret, msg_id

token = ''
token_expires_at = 0


def grant_token():
    result = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": appID,
            "secret": appsecret
        }
    )
    return result.json()


def get_access_token():
    global token
    global token_expires_at
    if token != '':
        now = time.time()
        if token_expires_at - now > 60:
            return token
    json = grant_token()
    token = json["access_token"]
    token_expires_at = int(time.time()) + json["expires_in"]
    return token


def send_msg(title, content, to_user, url=None):
    access_token = get_access_token()
    if to_user is not None:
        result = requests.post(
            url=f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}",
            json={
                "touser": to_user,
                "template_id": msg_id,
                "url": url,
                "data": {
                    "title": {
                        "value": title,
                        "color": "#173177"
                    },
                    "content": {
                        "value": content,
                        "color": "#000000"
                    }
                }
            }
        )
        return result.json()


if __name__ == '__main__':
    print(send_msg(title="标题", content="内容", to_user="oSk1753Uhqlo2FxThIUj1lT15daI"))
