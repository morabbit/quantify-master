# coding=utf8

import threading
import os
import time
from data_collect import DataCollect
from data_basic import DataBasic
import tushare

START_DATE = '2018-01-25'
END_DATE   = '2018-03-25'
BASIC_STOCK_PATH = 'F:/AllStocks/'
MAX_THREADS_NUM = 20

import sys
reload(sys)
sys.setdefaultencoding("utf8")

class DataMgr:
    threads = []
    DIC = {"all": DataBasic.get_all_stock_codes()
            , "zz500s": DataBasic.get_basic_zzs()
            , "hs300s": DataBasic.get_basic_hss()
            , "sz50s": DataBasic.get_basic_szs()
            , "sme": DataBasic.get_basic_sme()
            , "gem": DataBasic.get_basic_gem()}

    @classmethod
    def handle(cls, kType):
        # DataBasic.grep_basic()
        # all_codes = DataBasic.get_all_stock_codes().next()
        all_codes = cls.DIC[kType].next()

        for codeNum in all_codes:
            thread_process = threading.Thread(group=None, target=cls.process_original, args=(codeNum, kType, ))
            cls.threads.append(thread_process)

        slice_begin = 0
        slice_end = MAX_THREADS_NUM
        while len(cls.threads) > MAX_THREADS_NUM:
            time.sleep(0.1)
            threads_handle = cls.threads[slice_begin : slice_end]

            for t in threads_handle:
                t.start()

            for t in threads_handle:
                t.join()

            cls.threads = cls.threads[slice_end:]

        for t in cls.threads:
            t.start()

        for t in cls.threads:
            t.join()


    @classmethod
    def process_original(cls, codeNum, kType):
        # dataFrame = DataCollect.grep_hist_data_original(codeNum, START_DATE, END_DATE)
        # DataCollect.save_data(codeNum, dataFrame)
        save_path = os.path.join(BASIC_STOCK_PATH) + os.path.join("/") + os.path.join(kType) + os.path.join("/") + os.path.join(str(codeNum)) + os.path.join('.csv')
        df = tushare.get_hist_data(codeNum, START_DATE, END_DATE)
        if df is not None:
            df.to_csv(save_path)
        print ("finished %s\n" % codeNum)
        # pass


if __name__ == "__main__":
    DataMgr.handle("zz500s")
    # df = DataCollect.grep_hist_data_original("603619", START_DATE, END_DATE)
    # print("startsave")
    # DataCollect.save_data("603619", df)
    # print("endsave")
    # begin = 0
    # end = 5
    # a = [1,2,3,4, 5, 6, 7, 8, 9, 10]\
    # a = a[end:]
    # print a
    # print tushare.get_hist_data('sh')