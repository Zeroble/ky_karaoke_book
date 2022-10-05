import re
import sqlite3


def parseSong(song_data):
    song_name = song_data.find("songname").text
    song_seq = song_data.find("songseq").text
    song_writer = song_data.find("songwriter").text
    song_compose = song_data.find("songcompos").text
    song_singer = song_data.find("songperson").text
    song_lyrics = song_data.find("songlyrics").text
    song_release_month = song_data.find("songrelmon").text
    song_country = song_data.find("songctry").text
    song_key_sex = song_data.find("s_key_sex").text
    song_m_key = song_data.find("s_m_key").text
    song_f_key = song_data.find("s_f_key").text
    return (
        int(song_seq), song_name, song_singer, song_writer, song_compose, song_lyrics, song_country, song_release_month,
        song_key_sex, song_m_key, song_f_key)


conn = sqlite3.connect("songs_test.db", isolation_level=None)
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
