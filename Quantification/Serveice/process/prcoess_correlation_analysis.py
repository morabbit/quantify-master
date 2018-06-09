# coding=utf-8

from process.prcoess_basic import ProcessBasic


class ProcessCorrelationAnalysis(ProcessBasic):
    def __init__(self):
        ProcessBasic.__init__(self)

    # 对所有的股票数据进行相关系数的分析
    @classmethod
    def correlation_coefficient_analysis(cls):
        # 如果原始数据为空的话，直接停止分析，并返回-1
        if cls.__raw_data.empty:
            return -1

        # 获取所有的股票代码名
        socket_code_list = cls.__raw_data.columns.values.tolist()

        # 行循环，对新增的列进行逐行的数据添加
        for row, socket_code_row in enumerate(socket_code_list):
            # 创建一个空列表，用于存放每次需要插入的一列数据
            list = []

            # 列循环，每次添加新的一列，该列没有数据
            for col, socket_code_col in enumerate(socket_code_list):
                # 计算两支股票的相关系数
                correlation_coefficient = cls.__raw_data[socket_code_row].corrwith(cls.__raw_data[socket_code_col])
                # 将数据放入列表
                list.append(correlation_coefficient)

            # 插入一列新的数据
            cls.__analysed_data.append(list)

        # 修改所有的列columns的名字
        cls.__analysed_data.columns = socket_code_list
        cls.__analysed_data.index = socket_code_list


# 测试代码
if __name__ == "__main__":
    pass
