from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class SONG(Base):
    __tablename__ = 'songs'
    seq = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    singer = Column(String, nullable=True)
    writer = Column(String, nullable=True)
    compose = Column(String, nullable=True)
    lyrics = Column(String, nullable=True)
    country = Column(String, nullable=True)
    release_month = Column(String, nullable=True)
    key_sex = Column(String, nullable=True)
    m_key = Column(String, nullable=True)
    f_key = Column(String, nullable=True)
    name_joined = Column(String, nullable=True)
    singer_joined = Column(String, nullable=True)
