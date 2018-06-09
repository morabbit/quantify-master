# coding=utf-8

# 本类用于实现对tushare获取数据的预处理，集合成为一个完整的全数据的dataframe
import os
import csv
import pandas as pd

BASIC_STOCK_PATH = 'D:/AllStocks/'


class PreProcess:
    __file_size = 0         # csv文件的大小
    __cur_start = None      # 数据的起始时间
    __cur_end = None        # 数据的结束时间
    __data_amount = 0       # 包含多少个数据

    __file_list = []        # 存储所有的文件名
    __data_list = []        # 存储所有的dataframe数据

    def __init__(self):
        pass

    # 设置文件的校验规则
    @classmethod
    def set_rule(cls, file_size=0, cur_start=None, cur_end=None, data_amount=0):
        cls.__file_size = file_size      # csv文件的大小
        cls.__cur_start = cur_start      # 数据的起始时间
        cls.__cur_end = cur_end          # 数据的结束时间
        cls.__data_amount = data_amount  # 包含多少个数据

    # 拼接所有的数据，获取一个包含所有股票数据的dataframe
    @classmethod
    def split_all_csv_data(cls):
        # 循环遍历文件存储路径下的所有文件，将csv文件筛选出来
        for file_name in os.listdir(BASIC_STOCK_PATH):
            # 选出csv文件，并判断其是否合法，然后添加入列表中
            if ".csv" in file_name and cls.filter_csv(file_name):
                cls.__file_list.append(file_name)

        # 循环遍历列表，将csv文件转换为dataframe
        for file_name in cls.__file_list:
            cls.__data_list.append(cls.csv_to_df(file_name))

        # 将所有的dataframe单个数据拼接起来
        df = pd.concat(cls.__data_list, axis=1)

        return df

    # 判断csv文件数据是否合法
    @classmethod
    def filter_csv(cls, file_name):
        # 判断文件大小
        if cls.__file_size <= 0:
            pass
        elif cls.__file_size != os.path.getsize(os.path.join(BASIC_STOCK_PATH, file_name)):
            return False
        else:
            pass

        # 读取csv文件
        reader = csv.reader(open(os.path.join(BASIC_STOCK_PATH, file_name), "r"))
        context_list = list(reader)
        if len(context_list) <= 1:
            return False

        # 判断时起始间
        if cls.__cur_start is None:
            pass
        elif cls.__cur_start not in context_list[1]:
            return False
        else:
            pass

        # 判断结束始间
        if cls.__cur_end is None:
            pass
        elif cls.__cur_end not in context_list[reader.line_num - 1]:
            return False
        else:
            pass

        # 判断数据个数
        if cls.__data_amount <= 0:
            pass
        elif cls.__data_amount != reader.line_num:
            return False
        else:
            pass

        return True

    # 读取csv文件，并将它转换为dataframe
    @classmethod
    def csv_to_df(cls, file_name):
        # 传来的只有文件名，先做一个路径拼接，然后读取数据
        stock = pd.read_csv(os.path.join(BASIC_STOCK_PATH, file_name))

        # 生成的数据index是0开始的数字，column共两列，一个时间，一个收盘价，将时间值赋给index
        stock.index = stock['date'].tolist()

        # 删除时间column
        del stock['date']

        # 将收盘价的column名，由“close”改为股票代码
        stock.columns = [file_name.replace(".csv", '')]

        return stock


# 测试代码
if __name__ == "__main__":
    print PreProcess.split_all_csv_data()
    # PreProcess.split_all_csv_data()
