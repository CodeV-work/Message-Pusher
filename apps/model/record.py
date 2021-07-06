from sqlalchemy import Column, Integer, VARCHAR, SMALLINT, TEXT

from utils.time import int_timestamp
from apps.a_common.db import Base


class RecordDB(Base):
    __tablename__ = 'record'
    
    id = Column(Integer(), primary_key=True)
    title = Column(VARCHAR(126))
    content = Column(TEXT)
    token = Column(VARCHAR(126))
    push_type = Column(SMALLINT)
    create_at = Column(Integer, default=int_timestamp)
