from pydantic import BaseModel, Field
from typing import List

from apps.a_common.constants import PUSHER_TYPE_LITERAL
from apps.model.pusher import PusherDB


class PusherSerializer(BaseModel):
    id: int = None
    token: str
    push_type: PUSHER_TYPE_LITERAL = Field(...)
    params1: str = None
    params2: str = None
    create_at: int = None
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example":
                {
                    "token": "lyleshaw",
                    "push_type": 1,
                    "params1": "oSk1753Uhqlo2FxThIUj1lT15daI"
                }
        }


def to_PusherSerializer(p: PusherDB) -> dict:
    return {
        'id': p.id,
        'token': p.token,
        "push_type": p.push_type,
        "params1": p.params1,
        "params2": p.params2,
        'create_at': p.create_at
    }


def to_PusherListSerializer(ps: List[PusherDB]) -> List[dict]:
    return [to_PusherSerializer(p) for p in ps]
