# -*- coding:utf8 -*-

import datetime as dtime
import pytz
import os


class LoggingHelper():
    '''
    紀錄檔寫入模組
    '''

    def __init__(self, LogFile, root_path):

        # 時間格式參數設置
        self.time_format_config = '%Y-%m-%d %H:%M:%S'
        self.LogFiles = os.path.join(
            root_path,
            "Log",
            LogFile
        )

        # 如果當前位置底下不存在"Log/"就建立
        if not os.path.exists(os.path.join(root_path,"Log")):
            os.mkdir(os.path.join(root_path,"Log"))

    def __get_current_datetime(self):
        '''
        取得當前時間
        '''
        return dtime.datetime.now(pytz.timezone("Asia/Taipei")).strftime(self.time_format_config)

    def __write_log(self, time, level, text):
        '''
        執行Log寫檔作業
        '''

        print("[{}] {}: {}\n".format(
            time, str(level), str(text)
        ))

        # 開啟記錄檔延續寫檔
        with open(self.LogFiles, "a", encoding="utf-8") as file:
            file.write(
                "[{}] {}: {}\n".format(
                    time, str(level), str(text)
                )
            )

    def info(self, text):
        '''
        寫入Log紀錄-層級為基本資訊
        '''
        self.__write_log(
            time=self.__get_current_datetime(),
            level='Info',
            text=str(text)
        )

    def waring(self, text):
        '''
        寫入Log紀錄-層級為警告資訊
        '''
        self.__write_log(
            time=self.__get_current_datetime(),
            level='Waring',
            text=str(text)
        )

    def error(self, text):
        '''
        寫入Log紀錄-層級為錯誤資訊
        '''
        self.__write_log(
            time=self.__get_current_datetime(),
            level='Error',
            text=str(text)
        )

    def debug(self, text):
        '''
        寫入Log紀錄-層級為偵錯資訊
        '''
        self.__write_log(
            time=self.__get_current_datetime(),
            level='Debug',
            text=str(text)
        )
