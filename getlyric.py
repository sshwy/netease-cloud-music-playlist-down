import requests
import json
import console
import os
from mess import *
from headers import *

with open("./config.json",'r') as load_f:
    cfg=json.load(load_f)

save_path = cfg['lyric_save_path']

if not os.path.exists(save_path):
    os.mkdir(save_path)

def get_lrc(name,song_id):
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url,headers=headers)
    j = json.loads(lyric.text)
    if not 'lrc' in j:
        console.warn(name+"没有歌词!")
        return
    lrc = j['lrc']['lyric']
    with open(save_path+".lyric/"+name+'.lrc','w') as f:
        f.write(j['lrc']['lyric'])