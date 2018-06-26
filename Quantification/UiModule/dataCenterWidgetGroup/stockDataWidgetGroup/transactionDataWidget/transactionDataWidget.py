# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataSubWidget.transactionDataWidgetForBigSingleTransactionData import \
    TransactionDataWidgetForBigSingleTransactionData


class StockDataWidget(TransactionDataWidgetForBigSingleTransactionData):
    def __init__(self, parent=None):
        # 调用各个父类的实例化方法
        super(StockDataWidget, self).__init__()

        # 查询数据的传参字典
        self.__refDict = {}

        # 所有的按钮事件
        self.btnShowData.clicked.connect(self.onBtnShowDataClicked)
        self.btnSaveToCSV.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToExcel.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToHDF5.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToJSON.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToMySQL.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToMongoDB.clicked.connect(self.onBtnSaveClicked)

    def getRefDict(self):
        """获取用户选择的数据，如果数据有误，返回None， 数据正确，返回字典"""

        # 判断当前是哪一个tab， todo
        if 0 == self.tabWidget.currentIndex():      # 历史行情
            self.__refDict = self.getRefDictForHistoricalQuotation()
            print(self.__refDict)
        elif 1 == self.tabWidget.currentIndex():    # 复权数据
            self.__refDict = self.getRefDictForRehabilitationData()
            print(self.__refDict)
        elif 2 == self.tabWidget.currentIndex():    # 实时行情
            self.__refDict = self.getRefDictForRealTimeQuotation()
            print(self.__refDict)
        elif 3 == self.tabWidget.currentIndex():    # 历史分笔
            self.__refDict = self.getRefDictForHistoricalTick()
            print(self.__refDict)
        elif 4 == self.tabWidget.currentIndex():    # 实时分笔
            self.__refDict = self.getRefDictForRealTimeTick()
            print(self.__refDict)
        elif 5 == self.tabWidget.currentIndex():    # 当日历史分笔
            self.__refDict = self.getRefDictForSameDayHistoricalTick()
            print(self.__refDict)
        elif 6 == self.tabWidget.currentIndex():    # 大盘指数行情列表
            self.__refDict = self.getRefDictForMarketIndexList()
            print(self.__refDict)
        elif 7 == self.tabWidget.currentIndex():    # 大单交易数据
            self.__refDict = self.getRefDictForBigSingleTransactionData()
            print(self.__refDict)
        else:
            return None

    @QtCore.pyqtSlot()
    def onBtnShowDataClicked(self):
        """显示数据"""
        pass

    @QtCore.pyqtSlot()
    def onBtnSaveClicked(self):
        """各个保存按钮按下的时候的槽函数"""

        # 先获取一下需要传递的参数，如果数据有误，退出函数
        self.__refDict = {}
        if not self.getRefDict():
            return

        # 获取用户想要保存的数据路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())
        self.__refDict["path"] = path

        # 调取数据模块的接口


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = StockDataWidget()
    window.show()

    sys.exit(app.exec_())
