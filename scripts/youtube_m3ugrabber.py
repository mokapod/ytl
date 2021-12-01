#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/benmoose39     #
#########################################################################
'''

news = '''#EXTM3U
#EXTINF:-1 tvg-id="513" tvg-name="Al Jazeera English HD" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/int/aljazeera-int.png" group-title="新闻",Al Jazeera
https://live-hls-web-aje.getaj.net/AJE/01.m3u8
#EXTINF:-1 tvg-id="512" tvg-name="BBC World News HD" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/int/bbc-world-news-int.png" group-title="新闻",BBC World News
https://1111296894.rsc.cdn77.org/LS-ATL-54548-6/index.m3u8
#EXTINF:-1 tvg-id="" tvg-name="" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/us/cbsn-us.png" group-title="新闻",CBS News
https://cbsn-us-cedexis.cbsnstream.cbsnews.com/out/v1/55a8648e8f134e82a470f83d562deeca/master.m3u8
#EXTINF:-1 tvg-id="503" tvg-name="CGTN" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/int/cgtn-int.png" group-title="新闻",CGTN
https://live.cgtn.com/1000/prog_index.m3u8
#EXTINF:-1 tvg-id="515" tvg-name="CNA HD" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/int/cna-int.png" group-title="新闻",CNA
https://d2e1asnsl7br7b.cloudfront.net/7782e205e72f43aeb4a48ec97f66ebbe/index_5.m3u8
#EXTINF:-1 tvg-id="511" tvg-name="CNN HD" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/us/cnn-us.png" group-title="新闻",CNN
https://cnn-cnninternational-1-gb.samsung.wurl.com/manifest/playlist.m3u8
#EXTINF:-1 tvg-id="AGEC2" tvg-name="DW English" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/int/dw-int.png" group-title="新闻",Deutsche Welle
https://dwstream4-lh.akamaihd.net/i/dwstream4_live@131329/index_4_av-p.m3u8
#EXTINF:-1 tvg-id="AGEC3" tvg-name="France24" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/int/france-24-int.png" group-title="新闻",France 24
http://f24hls-i.akamaihd.net/hls/live/221147/F24_EN_HI_HLS/master.m3u8
#EXTINF:-1 tvg-id="398" tvg-name="NHK World" tvg-logo="https://raw.githubusercontent.com/mokapod/pl/main/lg/int/nhk-world-japan-int.png" group-title="新闻",NHK World
https://nhkwlive-ojp.akamaized.net/hls/live/2003459/nhkwlive-ojp-en/index.m3u8'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

#print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
#print(banner)
print(news)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
