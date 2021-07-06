from sqlalchemy import Column, Integer, VARCHAR, SMALLINT

from utils.time import int_timestamp
from apps.a_common.db import Base


class PusherDB(Base):
    __tablename__ = 'pusher'
    
    id = Column(Integer(), primary_key=True)
    token = Column(VARCHAR(126), nullable=False)
    push_type = Column(SMALLINT)
    params1 = Column(VARCHAR(126), nullable=False)
    params2 = Column(VARCHAR(126))
    create_at = Column(Integer, default=int_timestamp)
