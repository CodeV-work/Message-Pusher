from sqlalchemy import Column, Integer, VARCHAR

from utils.time import int_timestamp
from apps.a_common.db import Base


class TokenDB(Base):
    __tablename__ = 'token'
    
    id = Column(Integer(), primary_key=True)
    token = Column(VARCHAR(126), unique=True, nullable=False)
    create_at = Column(Integer, default=int_timestamp)
