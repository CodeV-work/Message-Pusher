from sqlalchemy.orm import Session

from apps.crud.pusher import get_pushers_by_token, get_pushers_by_token_and_type
from apps.serializer.record import RecordSerializer

from apps.pusher import test_wechat, official_wechat, e_mail, android, wechat, qq

type_func_dict = {
    1: test_wechat.send_msg,
    2: official_wechat.send_msg,
    3: e_mail.send_msg,
    4: android.send_msg,
    5: wechat.send_msg,
    6: qq.send_msg,
}


def send_msg(session: Session, record: RecordSerializer):
    if record.push_type is not None:
        pusher = get_pushers_by_token_and_type(session=session, token=record.token, push_type=record.push_type)
        type_func_dict[pusher.push_type](title=record.title, content=record.content, to_user=pusher.params1)
    else:
        pushers = get_pushers_by_token(session=session, token=record.token)
        for p in pushers:
            type_func_dict[p.push_type](title=record.title, content=record.content, to_user=p.params1)
