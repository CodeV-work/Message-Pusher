from logging import getLogger

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.a_common.db import get_session
from apps.a_common.response import success_response
from apps.pusher import send_msg
from apps.crud.record import add_record, get_records_by_token
from apps.serializer.record import RecordSerializer, to_RecordSerializer, to_RecordListSerializer

record_router = APIRouter()
record_prefix = 'record'
logger = getLogger(__name__)


@record_router.post("/:send", summary="发送一个通知，push_type不填默认全部发送")
async def record(record_serializer: RecordSerializer, session: Session = Depends(get_session)):
    record = add_record(session=session, record_serializer=record_serializer)
    send_msg(session=session, record=record_serializer)
    session.commit()
    return success_response(to_RecordSerializer(record))


@record_router.post("/{token}", summary="查看某token的全部通知")
async def register_record(token: str, session: Session = Depends(get_session)):
    records = get_records_by_token(session, token=token)
    return success_response(to_RecordListSerializer(records))
