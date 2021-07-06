from typing import List
from sqlalchemy.orm import Session

from apps.model.record import RecordDB
from apps.serializer.record import RecordSerializer


def add_record(session: Session, record_serializer: RecordSerializer) -> RecordDB:
    record = RecordDB(
        token=record_serializer.token,
        push_type=record_serializer.push_type,
        title=record_serializer.title,
        content=record_serializer.content
    )
    session.add(record)
    return record


def get_records_by_token(session: Session, token: str) -> List[RecordDB]:
    return session.query(RecordDB).filter(RecordDB.token == token).all()


def get_records_by_token_and_type(session: Session, token: str, push_type: int) -> List[RecordDB]:
    return session.query(RecordDB).filter(RecordDB.token == token).filter(RecordDB.push_type == push_type).all()
