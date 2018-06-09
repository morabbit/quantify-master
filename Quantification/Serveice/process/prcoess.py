# coding=utf-8

# 本类用于实现对tushare获取数据的存放，记录以及分析
import time
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


class Process:
    def __init__(self):
        self.__raw_data = DataFrame()      # 爬取的股票原始数据，数据结构为DataFrame
        self.__analysed_data = DataFrame()      # 进行处理之后的分析统计数据，格式也是DataFrame

    # 传入原始数据
    def set_raw_data(self, data):
        self.__raw_data = data

    # 获取原始数据
    def get_raw_data(self):
        return self.__raw_data

    # 获取分析后的数据
    def get_analysed_data(self):
        return self.__analysed_data

    # 将原始数据保存到excel
    def save_raw_data_to_excel(self):
        # 创建一个输出文件，创建时间来命名
        writer = pd.ExcelWriter('%s-raw.xlsx' % time.strftime("%Y-%m-%d", time.localtime()))

        # 写入文件
        self.__raw_data.to_excel(writer, time.strftime("%H:%M:%S", time.localtime()), index=False)

    # 将分析后的数据保存到excel
    def save_analysed_data_to_excel(self):
        # 创建一个输出文件，创建时间来命名
        writer = pd.ExcelWriter('%s-analysed.xlsx' % time.strftime("%Y-%m-%d", time.localtime()))

        # 写入文件
        self.__analysed_data.to_excel(writer, time.strftime("%H:%M:%S", time.localtime()), index=False)

    # 对所有的股票数据进行相关系数的分析
    def correlation_coefficient_analysis(self):
        # 如果原始数据为空的话，直接停止分析，并返回-1
        if self.__raw_data.empty:
            return -1

        # 获取所有的股票代码名
        socket_code_list = self.__raw_data.columns.values.tolist()

        # 行循环，对新增的列进行逐行的数据添加
        for row, socket_code_row in enumerate(socket_code_list):
            # 创建一个空列表，用于存放每次需要插入的一列数据
            list = []

            # 列循环，每次添加新的一列，该列没有数据
            for col, socket_code_col in enumerate(socket_code_list):
                # 计算两支股票的相关系数
                correlation_coefficient = self.__raw_data[socket_code_row].corrwith(self.__raw_data[socket_code_col])
                # 将数据放入列表
                list.append(correlation_coefficient)

            # 插入一列新的数据
            self.__analysed_data.append(list)

        # 修改所有的列columns的名字
        self.__analysed_data.columns = socket_code_list
        self.__analysed_data.index = socket_code_list
