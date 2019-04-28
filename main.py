# 魔改by Sshwy
# 从网易云音乐下载歌单歌曲
# 参考了这些网址
# https://blog.csdn.net/Ciiiiiing/article/details/62434438
# https://github.com/kunkun1230/Python-/tree/master/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%20%E4%B8%8D%E5%86%8D%E7%8A%B9%E8%B1%AB%20%E8%AF%84%E8%AE%BA%E5%88%86%E6%9E%90
# https://www.zhihu.com/question/36081767
# https://www.bbsmax.com/A/kPzOXYVeJx/

from bs4 import BeautifulSoup
import requests
import time
import json
import console  # My module
from headers import headers  # My module
from getlyric import get_lrc  # My module
from getmp3 import get_mp3  # My module

with open("./config.json", 'r') as load_f:
    cfg = json.load(load_f)

play_url = cfg['play_url']

if __name__ == "__main__":
    console.sig('NCM Playlist Download Start!')
    console.info('Your Playlist: %s' % play_url)
    start_time = time.time()  # 开始时间

    s = requests.session()
    s = BeautifulSoup(s.get(play_url, headers=headers).content, "html5lib")
    main = s.select('ul.f-hide li a')

    for music in main:
        song_id = music['href'][music['href'].find('id=') + len('id=')]
        name = music.text.replace('/', '|')
        get_mp3(name, song_id)
        get_lrc(name, song_id)

    end_time = time.time()  # 结束时间
    console.sig("Total time: %fs." % (end_time - start_time))
