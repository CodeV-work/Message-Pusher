from sqlalchemy.orm import Session

from utils.encode import uuid
from apps.model.token import TokenDB
from apps.serializer.token import TokenSerializer


def add_token(session: Session, token_serializer: TokenSerializer) -> TokenDB:
    if token_serializer.token is not None:
        token = TokenDB(token=token_serializer.token)
    else:
        token = TokenDB(token=uuid())
    session.add(token)
    return token


def get_token_by_id(session: Session, t_id: int) -> TokenDB:
    permission = session.query(TokenDB).filter(TokenDB.id == t_id).first()
    return permission
