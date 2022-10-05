import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

# DB 생성 (오토 커밋)
conn = sqlite3.connect("songs.db", isolation_level=None)
# 커서 획득
c = conn.cursor()
# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS songs \
    (seq integer PRIMARY KEY, name text, singer text, writer text, compose text, lyrics text, country text, release_month text, key_sex text, m_key text, f_key text)")