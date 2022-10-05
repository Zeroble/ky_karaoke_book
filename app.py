from fastapi import FastAPI
from database import *
from song_model import *

app = FastAPI()

engine = engineconn("sqlite:///./songs_test.db")
session = engine.sessionmaker()


@app.get("/search/name/{song_name}")
def read_item(song_name: str):
    if len(song_name) < 2:
        return "2자 이상 입력"
    ret = session.query(DBSong.seq, DBSong.name, DBSong.singer).filter(DBSong.name_joined.like(f"%{song_name}%")).all()
    print(ret)
    ret = {"cnt": len(ret), "data": ret}
    return ret


@app.get("/search/seq/{song_seq}")
def read_item(song_seq: int):
    return session.query(DBSong).get(song_seq)
