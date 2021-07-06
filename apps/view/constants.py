from fastapi import APIRouter

from apps.a_common.constants import ZH_PUSHER_TYPE_MAP, PUSHER_TYPE_MAP
from apps.a_common.response import success_response

constants_router = APIRouter()
constants_prefix = 'constants'


@constants_router.get("", summary="用于查询所有的constants")
async def get_constants():
    data = {
        'pusher_type': PUSHER_TYPE_MAP,
        'zh_pusher_type': ZH_PUSHER_TYPE_MAP
    }
    return success_response(data)
