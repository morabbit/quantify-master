# coding=utf8

import threading
import tushare
import os

BASIC_STOCK_PATH = 'F:/AllStocks/'

class DataCollect(object):
    __hist_data_df = None
    __cur_start = None
    __cur_end = None

    @classmethod
    def save_data(cls, stockCode, dataFrame):
        save_path = os.path.join(BASIC_STOCK_PATH) + os.path.join(str(stockCode)) + os.path.join('.csv')
        dataFrame.to_csv(save_path)

    @classmethod
    def grep_hist_data_original(cls, stockCode, startDate, endDate):
         return tushare.get_hist_data(stockCode, startDate, endDate)

    @classmethod
    def grep_hist_data(cls, stockCode, startDate = None, endDate = None):
        return cls.grep_hist_data_i(stockCode, startDate, endDate) if cls.check_flash_cond(startDate, endDate) else cls.__hist_data_df


    @classmethod
    def grep_hist_data_i(cls, stockCode, startDate, endDate):
        if startDate is not None and endDate is not None:
            df = tushare.get_hist_data(stockCode, startDate, endDate)
            cls.flash_hist_data(df, startDate, endDate)
            return df
        else:
            df = tushare.get_hist_data(stockCode)
            cls.flash_hist_data(df, startDate, endDate)
            return df

    @classmethod
    def flash_hist_data(cls, df, startDate, endDate):
        cls.__hist_data_df = df
        cls.__cur_start = startDate
        cls.__cur_end = endDate

    @classmethod
    def check_flash_cond(cls, startDate, endDate):
        if cls.__hist_data_df is None:
            return True
        elif startDate is not None and endDate is not None:
            return startDate != cls.__cur_start or endDate != cls.__cur_end
        else:
            return False


if __name__ == "__main__":
    # DataCollect.grep_hist_data("600848")
    # print DataCollect.grep_hist_data("600848")
    save_path = os.path.join(BASIC_STOCK_PATH) + os.path.join('600848') + os.path.join('.csv')

    print save_path

