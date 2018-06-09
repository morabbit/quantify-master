# coding=utf-8

# 本类用于实现对tushare获取数据的存放，记录以及分析的基类
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame


class ProcessBasic:
    __raw_data = DataFrame()  # 爬取的股票原始数据，数据结构为DataFrame
    __analysed_data = DataFrame()  # 进行处理之后的分析统计数据，格式也是DataFrame

    def __init__(self):
        pass

    # 传入原始数据
    @classmethod
    def set_raw_data(cls, data):
        cls.__raw_data = data

    # 获取原始数据
    @classmethod
    def get_raw_data(cls):
        return cls.__raw_data

    # 获取分析后的数据
    @classmethod
    def get_analysed_data(cls):
        return cls.__analysed_data

    # 将原始数据保存到excel
    @classmethod
    def save_raw_data_to_excel(cls):
        # 创建一个输出文件，创建时间来命名
        writer = pd.ExcelWriter('%s-raw.xlsx' % time.strftime("%Y-%m-%d", time.localtime()))

        # 写入文件
        cls.__raw_data.to_excel(writer, time.strftime("%H:%M:%S", time.localtime()), index=False)

    # 将分析后的数据保存到excel
    @classmethod
    def save_analysed_data_to_excel(cls):
        # 创建一个输出文件，创建时间来命名
        writer = pd.ExcelWriter('%s-analysed.xlsx' % time.strftime("%Y-%m-%d", time.localtime()))

        # 写入文件
        cls.__analysed_data.to_excel(writer, time.strftime("%H:%M:%S", time.localtime()), index=False)

    # 将分析完后的数据转换成为矩阵图表
    @classmethod
    def show_the_analysed_data_map(cls):
        # 如果数据没有进行分析，直接退出，不绘制
        if cls.__analysed_data.empty:
            return -1

        # 图片绘制
        img = np.array(cls.__analysed_data)
        plt.matshow(img, cmap=plt.cm.cool, vmin=0, vmax=1)
        plt.colorbar()
        plt.show()


# 测试代码
if __name__ == "__main__":
    pass
