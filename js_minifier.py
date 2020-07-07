# -*- coding: utf-8 -*-

import sys
import requests
import argparse
import os
import pytz
import datetime as dtime

from LoggingHelper import LoggingHelper

parser = argparse.ArgumentParser()

''' 建立來源參數 '''
parser.add_argument("-i","--input", type=str,
                    help="set a js files path string.",required=True)
''' 取得配置參數組合 '''
args = parser.parse_args()

time_format_config = '%Y-%m-%d %H:%M:%S'

def __get_current_datetime():
    '''
    取得當前時間
    '''
    return dtime.datetime.now(pytz.timezone("Asia/Taipei")).strftime(time_format_config)

def __GenLogFileName():
    
    return "RunLog{}.txt".format(__get_current_datetime())


if __name__ == "__main__":

    LogHelper = LoggingHelper(root_path= os.getcwd() , LogFile=__GenLogFileName())

    get_input = str(args.input)

    # 判斷輸入位置是否存在
    if os.path.exists(get_input):
        LogHelper.info("{} 位置存在，開始執行.".format(get_input))
    else:
        LogHelper.waring("輸入位置不存在!! 結束執行.")


# try:
#     js_file = sys.argv[1]
# except:
#     print("Missing input file")
#     sys.exit()

# # Grab the file contents
# with open(js_file, 'r') as c:
#     js = c.read()

# # Pack it, ship it
# payload = {'input': js}
# url = 'https://javascript-minifier.com/raw'
# print("Requesting mini-me of {}. . .".format(c.name))
# r = requests.post(url, payload)

# # Write out minified version
# minified = js_file.rstrip('.js')+'.min.js'
# with open(minified, 'w') as m:
#     m.write(r.text)

# print("Minification complete. See {}".format(m.name))

