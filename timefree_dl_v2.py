import base64
from urllib.parse import urlparse
import subprocess
import random
import re

try:
    import requests
    import xml.etree.ElementTree as ET
    from const import *
    from radiko_dl_gui import select_input_method
    from custom_msgbox import CustomFileDialog, CustomMsgBox
except ImportError:
    import os
    from pathlib import Path
    import sys

    os.chdir(os.path.dirname(__file__))

    # 仮想環境で実行されていない場合、仮想環境で再実行する
    if not "--rerun" in sys.argv:
        for root, dirs, files in os.walk(os.path.dirname(__file__)):
            if "activate" in files:
                exec_dir = Path(os.path.abspath(root))
        if sys.platform == "win32":
            os.execl(exec_dir.joinpath("python.exe"), f"-u {__file__} --rerun")
        elif sys.platform == "linux":
            os.execl(exec_dir.joinpath("python3"), f"-u {__file__} --rerun")


def get_program_info(id, ft):
    res = requests.get(
        'https://radiko.jp/v3/program/station/date/{0}/{1}.xml'.format(ft[:8], id))
    raw_prog = res.content.decode('utf-8')
    root = ET.fromstring(raw_prog)
    prog = root.find('.//prog[@ft=\"{0}\"]'.format(ft))
    to = prog.get('to')
    title = prog[0].text
    return to, title

def gen_random_info():
    version = random.choice(tuple(VERSION_MAP.keys()))
    sdk = VERSION_MAP[version]["sdk"]
    build = random.choice(VERSION_MAP[version]["builds"])
    model = random.choice(MODEL_LIST)
    device = sdk + "." + model
    useragent = "Dalvik/2.1.0 (Linux; U; Android " + version + "; " + model + "/" + build + ")"
    appversion = random.choice(APP_VERSION)
    userid = hex(random.getrandbits(128)).removeprefix("0x")
    return useragent, appversion, device, userid

def gen_location(area = DEFAULT_AREA):
    # 元のスクリプトは何をやっているのかわからん COORDINATES[tuple(COORDINATES.keys())[int(area[2:]) - 1]]
    ido, keido = COORDINATES[area]
    ido += random.random() / 40 * (1 if random.random() > 0.5 else -1)
    keido += random.random() / 40 * (1 if random.random() > 0.5 else -1)
    return ido, keido

def get_authtoken():
    info = gen_random_info()
    ido, keido = gen_location()
    # get authtoken
    headers1 = {
        'User-Agent': info[0],
        'X-Radiko-App': 'aSmartPhone7a',
        'X-Radiko-App-Version': info[1],
        'X-Radiko-Device': info[2],
        'X-Radiko-User': info[3],
    }
    res = requests.get('https://radiko.jp/v2/api/auth1', headers=headers1)
    print(f"auth1 ({res.status_code}) header")
    print(res.headers)
    # activate authtoken
    authtoken = res.headers['X-Radiko-Authtoken']
    keyoffset = int(res.headers['X-Radiko-KeyOffset'])
    keylength = int(res.headers['X-Radiko-KeyLength']) + keyoffset
    partialkey = base64.b64encode(base64.b64decode(BASEKEY)[keyoffset:keylength]).decode('utf-8')
    headers2 = {
        'User-Agent': info[0],
        'X-Radiko-App': 'aSmartPhone7a',
        'X-Radiko-App-Version': info[1],
        'X-Radiko-AuthToken': authtoken,
        'X-Radiko-Location': f"{ido:0f},{keido:0f},gps",
        'X-Radiko-Device': info[2],
        'X-Radiko-Connection': 'wifi',
        'X-Radiko-Partialkey': partialkey,
        'X-Radiko-User': info[3],
    }
    res = requests.get('https://radiko.jp/v2/api/auth2', headers=headers2)
    print(f"auth2 ({res.status_code}) header")
    print(res.headers)
    return authtoken


def get_baseurl(location):
    import qt_browser
    return qt_browser.main(location)

if __name__ == "__main__":
    ans = select_input_method()
    if ans is None or ans["selection"] is None:
        raise CanceledInDialog()
    if ans["selection"] == "browser":
        baseurl = get_baseurl(gen_location())
        if baseurl == "":
            raise NoSelectedInBrowser()
    else:
        baseurl = ans["manual_input"]
        if baseurl == "":
            raise NoInputInDialog()
    if not re.match(r'https:\/\/radiko.jp\/#!\/ts\/(.*)', baseurl):
        raise InvalidURL(baseurl)
    # baseurlの例: https://radiko.jp/#!/ts/FMT/20241015050000
    parsedurl = urlparse(baseurl)
    station_id = parsedurl.fragment.split("/")[2]
    # fragmentは"!/ts/FMT/20241015050000"の部分
    if not station_id in tuple(STATION_MAP.keys()):
        # 仕様変更等で、放送局IDが変わったらエラーで停止する
        raise InvalidStationId(station_id)
    ft = parsedurl.fragment.split("/")[3]
    to, title = get_program_info(station_id, ft)
    filename = CustomFileDialog().asksaveasfilename(
        title="Save as",
        filetypes=[("AAC", ".aac")],
        defaultextension="aac",
        initialfile=f'{STATION_MAP[station_id]["name"]}_{title}_{ft[:8]}.aac'
    )
    if filename == "":
        raise CanceledInDialog()
    token = get_authtoken()
    area_id = random.choice(STATION_MAP[station_id]["area"])

    print(token)

    ret = subprocess.run(['ffmpeg', '-loglevel', 'error', '-fflags', '+discardcorrupt', '-headers', 'X-Radiko-Authtoken: {0}'.format(
        token), '-i', 'https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={0}&l=15&ft={1}&to={2}'.format(station_id, ft, to), '-acodec', 'copy', '-vn', '-y', filename], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    print(f"stdout: {ret.stdout}")
    print(f"stderr: {ret.stderr}")
    if len(ret.stderr) == 0:
        CustomMsgBox().showinfo("", "Done.")
    else:
        raise DownloadError()