try:
    import requests
    import xmltodict
    import coloredlogs
    from timefree_dl_v2 import get_authtoken
    from const import *
except ImportError:
    import os
    from pathlib import Path
    import sys

    os.chdir(os.path.dirname(__file__))

    # 仮想環境で実行されていない場合、仮想環境で再実行する
    if not "--rerun" in sys.argv:
        def find_exec_dir(directory):
            for root, dirs, files in os.walk(directory):
                if "activate" in files:
                    return Path(os.path.abspath(root))
        exec_dir = find_exec_dir(os.path.dirname(__file__))
        if sys.platform == "win32":
            os.execl(exec_dir.joinpath("python.exe"), f"-u {__file__} --rerun")
        elif sys.platform == "linux":
            os.execl(exec_dir.joinpath("python3"), f"-u {__file__} --rerun")

import logging
import subprocess
import os
from datetime import datetime, timedelta

os.chdir(os.path.dirname(__file__))

def get_this_sunday():
    # 今日を取得
    current_date = datetime.now()
    # 曜日を取得（日曜日が0、月曜日が1、...）
    weekday = current_date.weekday()
    # 今週の日曜日を計算（日曜日が週の始まりとして）
    sunday_date = current_date - timedelta(days=(weekday + 1) % 7)
    return sunday_date


def get_program_info():
    ft, to = None, None
    sunday_date = get_this_sunday()
    # 番組情報を取得
    res = requests.get(f"https://radiko.jp/v3/program/station/date/{datetime.strftime(sunday_date, r"%Y%m%d")}/FMI.xml")
    # xmlをjsonに変換
    prog_json = xmltodict.parse(res.text)

    for p in prog_json["radiko"]["stations"]["station"]["progs"]["prog"]:
        if PROGRAM_NAME in p["title"]:
            ft = p["@ft"]
            to = p["@to"]
    
    if ft == None or to == None:
        raise ProgramNotFound()

    return ft, to


def run_dl():
    ft, to = get_program_info()

    if not os.path.exists("./dl"):
        os.mkdir("./dl")
    
    sunday_date = get_this_sunday()
    filename = f"./dl/{PROGRAM_NAME}_{datetime.strftime(sunday_date, r"%Y%m%d")}.aac"
    token = get_authtoken()

    result = subprocess.run(['ffmpeg', '-loglevel', 'error', '-fflags', '+discardcorrupt', '-headers', 'X-Radiko-Authtoken: {0}'.format(
    token), '-i', 'https://radiko.jp/v2/api/ts/playlist.m3u8?station_id={0}&l=15&ft={1}&to={2}'.format("FMI", ft, to), '-acodec', 'copy', '-vn', '-y', filename], stderr=subprocess.PIPE)
    
    if len(result.stderr) > 0:
        raise DownloadError()


if __name__ == "__main__":
    if not os.path.exists("./log"):
        os.mkdir("./log")
    # 実行日時を取得して、ファイル名に使う
    now = datetime.datetime.now()
    current_time = now.strftime(r'%Y-%m-%d_%H-%M-%S')
    log_filename = f'log/log_{current_time}.log'

    # ロガーを取得（カスタムロガーを作成）
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)  # ログレベルを設定

    # ハンドラを作成（ファイルに出力するためのハンドラ）
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)  # ハンドラのログレベルを設定

    # フォーマッタを作成して、ハンドラに設定
    formatter = logging.Formatter(r'%(asctime)s [%(levelname)s] %(message)s', datefmt=r'%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    # ロガーにハンドラを追加
    logger.addHandler(file_handler)

    # colordlogを開始
    coloredlogs.install(level='DEBUG', logger=logger, fmt='%(asctime)s [%(levelname)s]\n%(message)s\n')

    # ログメッセージを出力
    logger.info('開始')

    run_dl()