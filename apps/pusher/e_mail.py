import yagmail
from config import TO_MAIL, SMTP_SERVER, SMTP_USER, SMTP_PWD


def send_msg(title: str, content: str, to_user: str):
    if not TO_MAIL:
        return None
    yag = yagmail.SMTP(user=SMTP_USER, password=SMTP_PWD, host=SMTP_SERVER)
    yag.send([to_user], title, content)


if __name__ == '__main__':
    print(send_msg(title="标题", content="内容", to_user="x@lyleshaw.com"))
