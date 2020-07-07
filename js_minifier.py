# -*- coding: utf-8 -*-

import sys
import requests
import argparse
import os
import pytz
import datetime as dtime
import shutil

from LoggingHelper import LoggingHelper


url = 'https://javascript-minifier.com/raw'

parser = argparse.ArgumentParser()

''' 建立來源參數 '''
parser.add_argument("-i","--input", type=str,
                    help="set a js files path string.",required=True)
''' 取得配置參數組合 '''
args = parser.parse_args()

output_path = os.path.join(os.getcwd(),"compression")

time_format_config = '%Y-%m-%d'

LogHelper = LoggingHelper(root_path= os.getcwd() , LogFile="RunLog{}.txt".format(dtime.datetime.now(pytz.timezone("Asia/Taipei")).strftime(time_format_config)))

def __RunWithMinified(path_input , is_subdir = False):
    '''
    執行混淆封裝
    '''
    
    # 取得檔案名稱
    filename = os.path.split(path_input)[-1]

    if is_subdir:

        # 第一階層目錄名稱
        subdir_name = os.path.basename(os.path.split(path_input)[-2])

        # 建立在輸出根目錄內第一階層目錄，如果未存在情況下
        if not os.path.exists(os.path.join(output_path,subdir_name)):
            os.mkdir(os.path.join(output_path,subdir_name))

        old_js = os.path.join(subdir_name,filename)
        new_js = "{}_min.js".format(filename.split(".")[0])
        new_js = os.path.join(subdir_name,new_js)

        LogHelper.info(f"{old_js}\n--> {os.path.join(output_path,new_js)}")

    else:

        subdir_name = ""
        old_js = filename
        new_js = "{}_min.js".format(old_js.split(".")[0])

        LogHelper.info(f"{old_js}\n--> {os.path.join(output_path,new_js)}")

    try:

        js_content = ""
        
        # 讀取檔案
        with open(path_input,'r',encoding="utf-8") as c:
            js_content = c.read()

        # 封裝上傳資料內容
        payload = {'input': js_content}

        LogHelper.info("Requesting mini-me of {}. . .".format(filename))

        r = requests.post(url, payload)

        if r.status_code == 200:
            
            # 輸出已完成封裝js
            with open(os.path.join(output_path,new_js),'w',encoding="utf-8") as m:
                m.write(r.text)
            
            LogHelper.info("該檔案已完成壓縮封裝.")

    except Exception as err:

        LogHelper.error("{}\n{}".format(err,err.with_traceback()))
        
        raise Exception(err)
    


def __ScanFile(input):
    '''
    掃描指定位置下檔案內容，預設內部目錄只會在往下一層掃描
    '''

    # 清理輸出目錄，如果有存在
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    # 如果輸出目錄不存在就建立
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    LogHelper.info(f"輸出根目錄位置: {output_path}")

    if os.path.isdir(get_input): # 執行目錄內部掃描
       
        # 根目錄
        for root_item in os.listdir(get_input):

            sub_item = os.path.join(get_input,root_item)
            
            if os.path.isdir(sub_item):  # 第一階層目錄

                # 第一階層目錄內容
                for sub_dir in os.listdir(sub_item):

                    sub_dir_item = os.path.join(sub_item,sub_dir)

                    if os.path.isfile(sub_dir_item): # 檔案

                        __RunWithMinified(sub_dir_item,is_subdir = True)

            elif os.path.isfile(sub_item): # 檔案

                __RunWithMinified(sub_item,is_subdir = False)

    else:  # 執行單獨檔案掃描，來源為一個單獨實體檔案
       
        __RunWithMinified(get_input,is_subdir = False)

if __name__ == "__main__":

    try:        
        
        get_input = str(args.input)

        # 判斷輸入位置是否存在
        if os.path.exists(get_input):

            LogHelper.info("{} 位置存在，開始執行.".format(get_input))

            __ScanFile(get_input)

            LogHelper.info("全部作業執行完畢.")

        else:

            LogHelper.waring("輸入位置不存在!! 結束執行.")
        
    except Exception as err:
        LogHelper.info("執行異常，終止作業.")
        LogHelper.error("{}\n{}".format(err,err.with_traceback()))

