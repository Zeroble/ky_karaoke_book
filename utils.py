import re
import xml
import requests
import xml.etree.ElementTree as ET

def requestDataBySongSequence(seq: int):
    req = requests.get(f"https://kyapi.kyentertainment.kr/xml_data/Web_songsearch_lst.asp?s_cd=1&max=1&s_value={seq}")
    if req.status_code == 200:
        return ET.fromstring(req.text)
    else:
        print(f"ERROR : {req.status_code}, seq : {seq}")
        exit(1)

def requestDataByUpdateDate(date: str):
    req = requests.get(f"http://www.kumyoung.com/otr_svc/mobileWeb_songlist.asp?gb=3&s_cd=04&s_value={date}&max=100")
    if req.status_code == 200:
        return ET.fromstring(req.text)
    else:
        print(f"ERROR : {req.status_code}, seq : {date}")
        exit(1)

def parseSong(song_data: xml.etree.ElementTree.Element):
    song_name = song_data.find("songname").text
    song_seq = song_data.find("songseq").text
    song_writer = song_data.find("songwriter").text.replace("작사", "").strip()
    song_compose = song_data.find("songcompos").text.replace("작곡", "").strip()
    song_singer = song_data.find("songperson").text
    song_lyrics = song_data.find("songlyrics").text
    song_release_month = song_data.find("songrelmon").text
    song_country = song_data.find("songctry").text
    song_key_sex = song_data.find("s_key_sex").text
    song_m_key = song_data.find("s_m_key").text.strip()
    song_f_key = song_data.find("s_f_key").text.strip()
    name_joined = (re.sub('\s', "", song_name))
    singer_joined = re.sub('\s', "", song_singer)
    return (
    int(song_seq), song_name, song_singer, song_writer, song_compose, song_lyrics, song_country, song_release_month,
    song_key_sex, song_m_key, song_f_key, name_joined, singer_joined)