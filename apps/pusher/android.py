import requests


def send_msg(title, content, to_user):
    if to_user is not None:
        result = requests.post(
            url="https://api.nextrt.com/api/push/send",
            json={
                "title": title,
                "content": content,
                "type": "Android",
                "token": to_user
            }
        )
        return result.json()


if __name__ == '__main__':
    print(send_msg(title="标题", content="内容", to_user="786ae431a778cc9b5260ce78f8a35ac8"))
