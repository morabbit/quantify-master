# -*- coding: utf-8 -*-

import sys
import xlrd

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataSubWidget.transactionDataWidgetForRealTimeTick import \
    TransactionDataWidgetForRealTimeTick


class TransactionDataWidgetForSameDayHistoricalTick(TransactionDataWidgetForRealTimeTick):
    def __init__(self, parent=None):
        # print "StockDataWidgetForSameDayHistoricalTick: init"
        super(TransactionDataWidgetForSameDayHistoricalTick, self).__init__()

        # 创建本类管理的tab下的查询的参数
        self.__searchRefForSameDayHistoricalTick = {}

        # 存放批量股票代码数据的列表
        self.__codeListForSameDayHistoricalTick = []

        # 创建日历窗口，但是不显示
        self.__calenderForSameDayHistoricalTick = Calendar()

        # 勾选上股票代码的时候，再显示是否显示需要输入具体的信息
        self.onChkBoxBulkModeForSameDayHistoricalTickClicked()
        self.chkBoxBulkModeForSameDayHistoricalTick.clicked.connect(self.onChkBoxBulkModeForSameDayHistoricalTickClicked)

        # 批量导入按钮的信号与槽函数
        self.btnBulkModeForSameDayHistoricalTick.clicked.connect(self.onBtnBulkModeForSameDayHistoricalTickClicked)

        # 保存路径
        self.btnSavePathForSameDayHistoricalTick.clicked.connect(self.onBtnSavePathForSameDayHistoricalTickClicked)

    @QtCore.pyqtSlot()
    def onChkBoxBulkModeForSameDayHistoricalTickClicked(self):
        """检查是否需要调用批接口，显示批接口数据导入按钮"""

        # 检测“批量模式”复选框是否被选中，如果选中，显示“批量导入”按钮，并设置模式
        if self.chkBoxBulkModeForSameDayHistoricalTick.isChecked():
            self.btnBulkModeForSameDayHistoricalTick.show()
            self.__searchRefForSameDayHistoricalTick["mode"] = "multiCode"
        else:
            self.btnBulkModeForSameDayHistoricalTick.hide()
            self.__searchRefForSameDayHistoricalTick["mode"] = "singleCode"

            # 清空lineEdit
            self.lineEditStockCodeForSameDayHistoricalTick.clear()

        # 清空股票代码列表
        self.__codeListForSameDayHistoricalTick = []

    @QtCore.pyqtSlot()
    def onBtnBulkModeForSameDayHistoricalTickClicked(self):
        """批量导入按钮的槽函数"""

        # 清空lineEdit
        self.lineEditStockCodeForSameDayHistoricalTick.clear()

        # 获取用户设置的批量股票代码的Excel文件
        qFilePathName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, u'导入股票列表', './', "excel(*.xls *.xlsx)")

        # 如果获取的文件名为空，或者用户点击了取消，直接退出本方法
        if 0 == len(qFilePathName):
            return

        # 将QString转换为string
        filePathName = qFilePathName

        # 循环遍历该Excel文件中所有的数据表
        workbook = xlrd.open_workbook(filePathName)
        for sheet_name in workbook.sheets():
            # 读取该工作表中有多少列数据
            ncols = sheet_name.ncols
            for index in range(ncols):
                # 如果数据有非法值，报错
                try:
                    stockCodeList = map(str, map(int, sheet_name.col_values(index)))
                    self.__codeListForSameDayHistoricalTick += stockCodeList
                except:
                    QtWidgets.QMessageBox.warning(self, "错误！", "导入的股票代码表存在非法值", QtWidgets.QMessageBox.Cancel)
                    self.__codeListForSameDayHistoricalTick = []
                    return

        # 将股票列表的代码号填写到linEdit中
        for stockCode in self.__codeListForSameDayHistoricalTick:
            self.lineEditStockCodeForSameDayHistoricalTick.insert("\"%s\", " % stockCode)

    @QtCore.pyqtSlot()
    def onBtnSavePathForSameDayHistoricalTickClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePathForSameDayHistoricalTick.setText(path)

    def getRefSingleStockCodeForSameDayHistoricalTick(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.lineEditStockCodeForSameDayHistoricalTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写股票代码", QtWidgets.QMessageBox.Cancel)
            return None
        try:
            int(self.lineEditStockCodeForSameDayHistoricalTick.text())
        except:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码须为6位数字", QtWidgets.QMessageBox.Cancel)
            return None
        if 6 != len(self.lineEditStockCodeForSameDayHistoricalTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
            return None

        # 创建传参字典
        return self.lineEditStockCodeForSameDayHistoricalTick.text()

    def getRefMultiStockCodeForSameDayHistoricalTick(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.__codeListForSameDayHistoricalTick) or self.__codeListForSameDayHistoricalTick is None:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请导入股票代码文件", QtWidgets.QMessageBox.Cancel)
            return None
        for stockCode in self.__codeListForSameDayHistoricalTick:
            if 6 == len(stockCode):
                QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
                return None

        # 返回股票代码列表
        return self.__codeListForSameDayHistoricalTick

    def getRefSavePathForSameDayHistoricalTick(self):
        """获取文件保存路径"""

        # 容错
        if 0 == len(self.lineEditSavePathForSameDayHistoricalTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请设置保存路径", QtWidgets.QMessageBox.Cancel)
            return None

        return str(self.lineEditSavePathForSameDayHistoricalTick.text())

    def getRefDictForSameDayHistoricalTick(self):
        """获取历史行情参数字典"""

        # 如果是查询单只股票
        if self.__searchRefForSameDayHistoricalTick["mode"] == "singleCode":
            # 获取参数，创建传参字典
            if self.getRefSingleStockCodeForSameDayHistoricalTick() is not None:
                self.__searchRefForSameDayHistoricalTick["code"] = self.getRefSingleStockCodeForSameDayHistoricalTick()
            else:
                return None

        # 如果是查询多只股票
        if self.__searchRefForSameDayHistoricalTick["mode"] == "multiCode":
            # 获取参数，创建传参字典
            if self.getRefMultiStockCodeForSameDayHistoricalTick() is not None:
                self.__searchRefForSameDayHistoricalTick["code"] = self.getRefMultiStockCodeForSameDayHistoricalTick()
            else:
                return None

        # 获取文件保存路径
        self.__searchRefForSameDayHistoricalTick["path"] = self.getRefSavePathForSameDayHistoricalTick()

        # 回返一个参数字典
        return self.__searchRefForSameDayHistoricalTick


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = TransactionDataWidgetForSameDayHistoricalTick()
    window.show()

    sys.exit(app.exec_())
