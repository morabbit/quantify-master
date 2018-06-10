#coding=utf8

import os
import string
import tushare


BASIC_PATH = "E:/AllStocks"

class DataBasic:
    __all_stock_codes = None
    __basic_index = None
    __zz500s = None
    __hs300s = None
    __sz50s = None
    __sme = None
    __gem = None
    __save_mode = None
    __save_name = None
    __save_path = BASIC_PATH


    #期货数据
    @classmethod
    def get_futures(cls, startDate, endDate, market):
        print(startDate, endDate, market)
        cls.grep_futures(startDate,endDate, market)

    #历史复权数据
    @classmethod
    def get_all_stock_codes(cls):
        cls.grep_basic()
        yield cls.__all_stock_codes if cls.__all_stock_codes is not None else []

    #大盘行情指数列表
    @classmethod
    def get_basic_index(cls):
        cls.grep_basic_index()
        yield cls.__basic_index if cls.__basic_index is not None else []


    #中证500
    @classmethod
    def get_basic_zzs(cls):
        cls.grep_basic_zzs()
        yield cls.__zz500s if cls.__zz500s is not None else []

    #沪深300
    @classmethod
    def get_basic_hss(cls):
        cls.grep_basic_hss()
        yield cls.__hs300s if cls.__hs300s is not None else []

    #上证50
    @classmethod
    def get_basic_szs(cls):
        cls.grep_basic_szs()
        yield cls.__sz50s if cls.__sz50s is not None else []

    #中小板
    @classmethod
    def get_basic_sme(cls):
        cls.grep_basic_sme()
        yield cls.__sme if cls.__sme is not None else []

    #创业板
    @classmethod
    def get_basic_gem(cls):
        cls.grep_basic_gem()
        yield cls.__gem if cls.__gem is not None else []

#############################################################################
    @classmethod
    def grep_futures(cls, startDate, endDate, market):
        df = tushare.get_future_daily(startDate, endDate, market)
        cls.save(df, "futures", "csv_mode")

    @classmethod
    def grep_basic(cls):
        df = tushare.get_stock_basics()
        cls.save(df, "allBasics")
        cls.__all_stock_codes = df.index

    @classmethod
    def grep_basic_index(cls):
        df = tushare.get_index()
        cls.save(df, "allBasicsIndex")
        cls.__basic_index = df['code'].tolist()

    @classmethod
    def grep_basic_zzs(cls):
        df = tushare.get_zz500s()
        cls.save(df, "zz500s")
        cls.__zz500s = df['code'].tolist()


    @classmethod
    def grep_basic_hss(cls):
        df = tushare.get_hs300s()
        cls.save(df, "hs300s")
        cls.__hs300s = df['code'].tolist()

    @classmethod
    def grep_basic_szs(cls):
        df = tushare.get_sz50s()
        cls.save(df, "sz50s")
        cls.__sz50s = df['code'].tolist()

    @classmethod
    def grep_basic_sme(cls):
        df = tushare.get_sme_classified()
        cls.save(df, "sme")
        cls.__sme = df['code'].tolist()

    @classmethod
    def grep_basic_gem(cls):
        df = tushare.get_gem_classified()
        cls.save(df, "gem")
        cls.__gem = df['code'].tolist()

    @classmethod
    def save(cls, df, fileName, mode="csv_mode"):
        try:
            # save_path = os.path.join(BASIC_PATH) + os.path.join("/") + os.path.join(fileName)
            save_path = os.path.join(cls.__save_path) + os.path.join("/") + os.path.join(fileName)
            if "" != cls.save_mode_file(mode):
               save_path =os.path.join(save_path, cls.save_mode_file(mode))

            cls.save_mode_method(mode, df)(save_path)
        except BaseException as err:
            #logging Error exception
            pass

    @classmethod
    def save_mode_method(cls, mode, df):
        cls.__save_mode = { "csv_mode":   df.to_csv
                          , "excel_mode": df.to_excel
                          , "hdf_mode":   df.to_hdf
                          , "json_mode":  df.to_json
                          , "sql_mode":   df.to_sql}

        if not isinstance(mode, string):
            # record log is not a string
            raise Exception("is not a valid mode parameter", mode)
        return cls.__save_mode[mode]

    @classmethod
    def save_mode_file(cls, mode):
        cls.__save_name = { "csv_mode":   ".csv"
                          , "excel_mode": ".xlsx"
                          , "hdf_mode":   ".h5"
                          , "json_mode":  ".json"
                          , "sql_mode":   ""}

        if not isinstance(mode, string):
            # record log is not a string
            raise Exception("is not a valid mode parameter", mode)
        return cls.__save_name[mode]

    @classmethod
    def set_save_path(cls, path):
        cls.__save_path = path


if __name__ == "__main__":
    #df = tushare.get_sz50s()
    #print df['code'].tolist()
    # df.index = df['code'].tolist()
    # print df.index
    # df = tushare.get_stock_basics()
    # print df.index

    df = tushare.get_future_daily("20180301", "20180520")
