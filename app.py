from fastapi import FastAPI
from database import *
from song_model import *

app = FastAPI()

engine = engineconn("sqlite:///./songs_test.db")
session = engine.sessionmaker()
defSongRetQery = session.query(SONG.seq, SONG.name, SONG.singer)


# 노래 제목으로 검색
@app.get("/search/name/{song_name}")
def read_item(song_name: str):
    if len(song_name) == 1:
        ret = defSongRetQery.filter(SONG.name_joined == song_name).all()
    else:
        ret = defSongRetQery.filter(SONG.name_joined.like(f"%{song_name}%")).all()
    return {"cnt": len(ret), "data": ret}


# 가수로 검색
@app.get("/search/singer/{song_singer}")
def read_item(song_singer: str):
    ret = defSongRetQery.filter(SONG.singer_joined.like(f"%{song_singer}%")).all()
    return {"cnt": len(ret), "data": ret}


#번호로 검색
@app.get("/search/seq/{song_seq}")
def read_item(song_seq: int):
    ret = session.query(SONG).get(song_seq)
