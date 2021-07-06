from pydantic import BaseModel, Field
from typing import List

from apps.a_common.constants import PUSHER_TYPE_LITERAL
from apps.model.record import RecordDB


class RecordSerializer(BaseModel):
    id: int = None
    title: str
    content: str = None
    token: str
    push_type: PUSHER_TYPE_LITERAL = Field(None)
    create_at: int = None
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example":
                {
                    "token": "lyleshaw",
                    "push_type": 1,
                    "title": "标题",
                    "content": "内容"
                }
        }


def to_RecordSerializer(r: RecordDB) -> dict:
    return {
        'id': r.id,
        'token': r.token,
        "push_type": r.push_type,
        "title": r.title,
        "content": r.content,
        'create_at': r.create_at
    }


def to_RecordListSerializer(rs: List[RecordDB]) -> List[dict]:
    return [to_RecordSerializer(r) for r in rs]
