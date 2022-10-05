from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


class engineconn:
    def __init__(self, DB_URL):
        self.engine = create_engine(DB_URL, connect_args={"check_same_thread": False}, echo=True)

    def sessionmaker(self) -> Session:
        session_local = sessionmaker(bind=self.engine)
        session = session_local()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn

