from logging import getLogger

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.a_common.db import get_session
from apps.a_common.response import success_response
from apps.crud.pusher import add_pusher, get_pushers_by_token
from apps.serializer.pusher import PusherSerializer, to_PusherSerializer, to_PusherListSerializer

pusher_router = APIRouter()
pusher_prefix = 'pusher'
logger = getLogger(__name__)


@pusher_router.get("/{token}", summary="查询一个token的全部推送方式")
async def query_pushers_by_token(token: str, session: Session = Depends(get_session)):
    pushers = get_pushers_by_token(session, token=token)
    return success_response(to_PusherListSerializer(pushers))


@pusher_router.post("/", summary="配置一个pusher")
async def register_pusher(pusher_data: PusherSerializer, session: Session = Depends(get_session)):
    pusher = add_pusher(session, pusher_serializer=pusher_data)
    session.commit()
    return success_response(to_PusherSerializer(pusher))
