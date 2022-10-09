import datetime
import sqlite3
from utils import *

conn = sqlite3.connect("./songs_test.db", isolation_level=None)
cur = conn.cursor()

# UPDATE ALL
# for i in range(101, 99999):
#     data = requestDataBySongSequence(i)
#     print(f'prograss : {i}/99999({i / 99999 * 100:0.4f}%)')
#     if data.find("record").find("songcnt").text != "0":
#         parsed_data = parseSong(data.find("record"))
#         print("searched! :", parsed_data[0], "-", parsed_data[1])
#         cur.execute(
#             "INSERT OR REPLACE INTO songs(seq, name, singer, writer, compose, lyrics, country, release_month, key_sex, m_key, f_key, name_joined, singer_joined) "
#             "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", parsed_data)

# update by duration
START_DATE = datetime.datetime(2022, 10, 4)
END_DATE = datetime.datetime(2022, 10, 9)
while START_DATE <= END_DATE:
    DATE = START_DATE.strftime("%Y%m%d")
    print(DATE)
    for item in requestDataByUpdateDate(DATE).findall("record"):
        seq = item.find("songseq").text
        if cur.execute(f"SELECT count(*) FROM songs where seq == {seq}").fetchall()[0][0] == 1:
            print(f"{seq} - 존재")
            continue
        data = requestDataBySongSequence(seq)
        if data.find("record").find("songcnt").text != "0":
            parsed_data = parseSong(data.find("record"))
            print(parsed_data)
            cur.execute(
                "INSERT INTO songs(seq, name, singer, writer, compose, lyrics, country, release_month, key_sex, m_key, f_key, name_joined, singer_joined) "
                "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", parsed_data)
    START_DATE += datetime.timedelta(days=1)
