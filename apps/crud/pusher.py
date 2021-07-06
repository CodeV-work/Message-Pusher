from typing import List
from sqlalchemy.orm import Session

from apps.model.pusher import PusherDB
from apps.serializer.pusher import PusherSerializer


def add_pusher(session: Session, pusher_serializer: PusherSerializer) -> PusherDB:
    pusher = PusherDB(
        token=pusher_serializer.token,
        push_type=pusher_serializer.push_type,
        params1=pusher_serializer.params1,
        params2=pusher_serializer.params2
    )
    session.add(pusher)
    return pusher


def get_pushers_by_token(session: Session, token: str) -> List[PusherDB]:
    return session.query(PusherDB).filter(PusherDB.token == token).all()


def get_pushers_by_token_and_type(session: Session, token: str, push_type: int) -> PusherDB:
    return session.query(PusherDB).filter(PusherDB.token == token).filter(PusherDB.push_type == push_type).first()


def update_pusher_by_token_and_type(session: Session, pusher_serializer: PusherSerializer):
    session.query(PusherDB).filter(PusherDB.token == pusher_serializer.token).filter(PusherDB.push_type == pusher_serializer.push_type). \
        update({PusherDB.params1: pusher_serializer.params1, PusherDB.params2: pusher_serializer.params2, }, synchronize_session=False)
