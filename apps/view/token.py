from logging import getLogger

from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from apps.a_common.db import get_session
from apps.a_common.response import success_response
from apps.crud.token import add_token
from apps.serializer.token import TokenSerializer, to_TokenSerializer

token_router = APIRouter()
token_prefix = 'token'
logger = getLogger(__name__)


@token_router.post("/", summary="注册一个token")
async def register(token_data: TokenSerializer, session: Session = Depends(get_session)):
    token = add_token(session, token_data)
    session.commit()
    return success_response(to_TokenSerializer(token))
