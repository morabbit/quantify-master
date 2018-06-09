#coding=utf8

import os
import tushare


BASIC_PATH = "F:/AllStocks"

class DataBasic:
    __all_stock_codes = None
    __basic_index = None
    __zz500s = None
    __hs300s = None
    __sz50s = None
    __sme = None
    __gem = None

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
    def grep_basic(cls):
        df = tushare.get_stock_basics()
        cls.save(df, "allBasics.csv")
        cls.__all_stock_codes = df.index

    @classmethod
    def grep_basic_index(cls):
        df = tushare.get_index()
        cls.save(df, "allBasicsIndex.csv")
        cls.__basic_index = df['code'].tolist()

    @classmethod
    def grep_basic_zzs(cls):
        df = tushare.get_zz500s()
        cls.save(df, "zz500s.csv")
        cls.__zz500s = df['code'].tolist()


    @classmethod
    def grep_basic_hss(cls):
        df = tushare.get_hs300s()
        cls.save(df, "hs300s.csv")
        cls.__hs300s = df['code'].tolist()

    @classmethod
    def grep_basic_szs(cls):
        df = tushare.get_sz50s()
        cls.save(df, "sz50s.csv")
        cls.__sz50s = df['code'].tolist()

    @classmethod
    def grep_basic_sme(cls):
        df = tushare.get_sme_classified()
        cls.save(df, "sme.csv")
        cls.__sme = df['code'].tolist()

    @classmethod
    def grep_basic_gem(cls):
        df = tushare.get_gem_classified()
        cls.save(df, "gem.csv")
        cls.__gem = df['code'].tolist()

    @classmethod
    def save(cls, df, fileName):
        save_path = os.path.join(BASIC_PATH) + os.path.join("/") + os.path.join(fileName)
        print save_path
        df.to_csv(save_path)

if __name__ == "__main__":
    df = tushare.get_sz50s()
    print df['code'].tolist()
    # df.index = df['code'].tolist()
    # print df.index
    # df = tushare.get_stock_basics()
    # print df.index
