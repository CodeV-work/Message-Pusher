from pydantic import BaseModel

from apps.model.token import TokenDB


class TokenSerializer(BaseModel):
    id: int = None
    token: str = None
    create_at: int = None
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example":
                {
                    "token": "lyleshaw",
                }
        }


def to_TokenSerializer(t: TokenDB) -> dict:
    return {
        'id': t.id,
        'token': t.token,
        'create_at': t.create_at
    }
