import re
import sqlite3

conn = sqlite3.connect("../songs_test.db", isolation_level=None)
c = conn.cursor()
e = conn.cursor()
c.execute('SELECT * FROM songs')
for row in c:
    row = list(row)
    row[-2] = (re.sub('\s', "", row[1]))
    row[-1] = None if row[2] is None else re.sub('\s', "", row[2])
    row[-3] = None if row[-3] is None else row[-3].strip()
    row[-4] = None if row[-4] is None else row[-4].strip()
    row[3] = None if row[3] is None else row[3].replace("작사", "").strip()
    row[4] = None if row[4] is None else row[4].replace("작곡", "").strip()
    print(row)
    e.execute("INSERT OR REPLACE INTO songs(seq, name, singer, writer, compose, lyrics, country, release_month, key_sex, m_key, f_key, name_joined, singer_joined) "
                "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", tuple(row))
