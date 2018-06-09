# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.stockDataWidget.stockDataSubWidget.stockDataWidgetForBigSingleTransactionData import \
    StockDataWidgetForBigSingleTransactionData
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.stockDataWidget.stockDataSubWidget.stockDataWidgetForHistoricalQuotation import \
    StockDataWidgetForHistoricalQuotation
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.stockDataWidget.stockDataSubWidget.stockDataWidgetForHistoricalTick import \
    StockDataWidgetForHistoricalTick
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.stockDataWidget.stockDataSubWidget.stockDataWidgetForRealTimeTick import \
    StockDataWidgetForRealTimeTick
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.stockDataWidget.stockDataSubWidget.stockDataWidgetForRehabilitationData import \
    StockDataWidgetForRehabilitationData
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.stockDataWidget.stockDataSubWidget.stockDataWidgetForSameDayHistoricalTick import \
    StockDataWidgetForSameDayHistoricalTick


class StockDataWidget(StockDataWidgetForHistoricalQuotation,
                      StockDataWidgetForRehabilitationData,
                      StockDataWidgetForHistoricalTick,
                      StockDataWidgetForRealTimeTick,
                      StockDataWidgetForSameDayHistoricalTick,
                      StockDataWidgetForBigSingleTransactionData):
    def __init__(self, parent=None):
        # 先实例化界面，然后调用各个父类的实例化方法
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        super(StockDataWidget,self).__init__()

        # 查询数据的传参字典
        self.__refDict = {}

        # 创建日历窗口，但是不显示
        self.__calender = Calendar()

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
        if 0 == self.tabWidget.currentIndex():
            print self.getRefDictForHistoricalQuotation()
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
        path = unicode(QtGui.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath()), 'utf-8', 'ignore')
        self.__refDict["path"] = path

        # 调取数据模块的接口


# 测试代码
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    window = StockDataWidget()
    window.show()

    sys.exit(app.exec_())
