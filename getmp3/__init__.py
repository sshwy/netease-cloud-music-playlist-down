import requests
import json
import urllib.request
import os
from getparams import get_params, get_encSecKey
from headers import headers
import console

with open("./config.json", 'r') as load_f:
    cfg = json.load(load_f)

store_path = cfg['save_path']  # 保存目录

if not os.path.exists(store_path):
    os.mkdir(store_path)


def get_mp3(name, song_id):
    # 网易歌曲前缀
    url = "http://music.163.com/weapi/song/enhance/player/urlcsrf_token="

    first_param = '{ids:"[%s]", br:"128000", csrf_token:""}' % song_id
    data = {
        "params": get_params(first_param).encode('utf-8'),
        "encSecKey": get_encSecKey()
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.json()

        if result['code'] != 200:
            console.warn('歌曲[%s]下载失败[返回值: %s]' % (name, result['code']))
            return

        mp3_url = result['data'][0]['url']
        urllib.request.urlretrieve(
            mp3_url, os.path.join(store_path, name + '.mp3'))
        console.info('歌曲[%s]下载完成...' % name)
    except json.decoder.JSONDecodeError:
        console.err('歌曲[%s]返回值无法解析为Json' % name)
        console.info("data:")
        console.info(str(data))
