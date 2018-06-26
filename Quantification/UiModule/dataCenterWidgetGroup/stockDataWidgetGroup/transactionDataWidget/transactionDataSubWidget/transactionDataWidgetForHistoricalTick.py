# -*- coding: utf-8 -*-

import sys
import xlrd
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataSubWidget.transactionDataWidgetForRealTimeQuotation import \
    TransactionDataWidgetForRealTimeQuotation


class TransactionDataWidgetForHistoricalTick(TransactionDataWidgetForRealTimeQuotation):
    def __init__(self, parent=None):
        # print "StockDataWidgetForHistoricalTick: init"
        super(TransactionDataWidgetForHistoricalTick, self).__init__()

        # 创建本类管理的tab下的查询的参数
        self.__searchRefForHistoricalTick = {}

        # 存放批量股票代码数据的列表
        self.__codeListForHistoricalTick = []

        # 创建日历窗口，但是不显示
        self.__calenderForHistoricalTick = Calendar()

        # 当点击起始时间，结束时间lineEdit的时候，弹出日历
        self.lineEditTickTimeForHistoricalTick.LineEditClicked.connect(self.onLineEditTickTimeForHistoricalTickClicked)

        # 点击复选框，是否显示“批量导入按钮”
        self.onChkBoxBulkModeForHistoricalTickClicked()
        self.chkBoxBulkModeForHistoricalTick.clicked.connect(self.onChkBoxBulkModeForHistoricalTickClicked)

        # 批量导入按钮的信号与槽函数
        self.btnBulkModeForHistoricalTick.clicked.connect(self.onBtnBulkModeForHistoricalTickClicked)

        # 保存路径
        self.btnSavePathForHistoricalTick.clicked.connect(self.onBtnSavePathForHistoricalTickClicked)

    @QtCore.pyqtSlot()
    def onLineEditTickTimeForHistoricalTickClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calenderForHistoricalTick.setLineEditObj(self.lineEditTickTimeForHistoricalTick)

        # 显示日历窗口
        self.__calenderForHistoricalTick.show()

    @QtCore.pyqtSlot()
    def onChkBoxBulkModeForHistoricalTickClicked(self):
        """检查是否需要显示批量输入按钮"""
        if self.chkBoxBulkModeForHistoricalTick.isChecked():
            self.btnBulkModeForHistoricalTick.show()  # 显示批量输入按钮
            self.__searchRefForHistoricalTick["mode"] = "multiCode"
        else:
            self.btnBulkModeForHistoricalTick.hide()  # 隐藏批量输入按钮
            self.__searchRefForHistoricalTick["mode"] = "singleCode"

    @QtCore.pyqtSlot()
    def onBtnBulkModeForHistoricalTickClicked(self):
        """批量导入按钮的槽函数"""

        # 清空lineEdit
        self.lineEditStockCodeForHistoricalTick.clear()

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
                    self.__codeListForHistoricalTick += stockCodeList
                except:
                    QtWidgets.QMessageBox.warning(self, "错误！", "导入的股票代码表存在非法值", QtWidgets.QMessageBox.Cancel)
                    self.__codeListForHistoricalTick = []
                    return

    @QtCore.pyqtSlot()
    def onBtnSavePathForHistoricalTickClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePathForHistoricalTick.setText(path)

    def getRefSingleStockCodeForHistoricalTick(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.lineEditStockCodeForHistoricalTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写股票代码", QtWidgets.QMessageBox.Cancel)
            return None
        try:
            int(self.lineEditStockCodeForHistoricalTick.text())
        except:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码须为6位数字", QtWidgets.QMessageBox.Cancel)
            return None
        if 6 != len(self.lineEditStockCodeForHistoricalTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
            return None

        # 返回股票代码
        return self.lineEditStockCodeForHistoricalTick.text()

    def getRefMultiStockCodeForHistoricalTick(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.__codeListForHistoricalTick) or self.__codeListForHistoricalTick is None:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请导入股票代码文件", QtWidgets.QMessageBox.Cancel)
            return None
        for stockCode in self.__codeListForHistoricalTick:
            if 6 == len(stockCode):
                QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
                return None

        # 创建传参字典
        return self.__codeListForHistoricalTick

    def getRefDateTimeForHistoricalTick(self):
        """获取时间"""

        # 判断是否选择了时间
        if 0 == len(self.lineEditTickTimeForHistoricalTick.text()) or 0 == len(self.lineEditTickTimeForHistoricalTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写完整日期！", QtWidgets.QMessageBox.Cancel)
            return None

        # 获取参数
        date = self.lineEditTickTimeForHistoricalTick.text()

        return date

    def getRefSavePathForHistoricalTick(self):
        """获取文件保存路径"""

        # 容错
        if 0 == len(self.lineEditSavePathForHistoricalTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请设置保存路径", QtWidgets.QMessageBox.Cancel)
            return None

        return str(self.lineEditSavePathForHistoricalTick.text())

    def getRefDictForHistoricalTick(self):
        """获取复权数据参数字典"""

        # 如果是查询单只股票
        if self.__searchRefForHistoricalTick["mode"] == "singleCode":
            # 获取参数，创建传参字典
            if self.getRefSingleStockCodeForHistoricalTick() is not None:
                self.__searchRefForHistoricalTick["code"] = self.getRefSingleStockCodeForHistoricalTick()
            else:
                return None

        # 如果是查询多只股票
        if self.__searchRefForHistoricalTick["mode"] == "multiCode":
            # 获取参数，创建传参字典
            if self.getRefMultiStockCodeForHistoricalTick() is not None:
                self.__searchRefForHistoricalTick["code"] = self.getRefMultiStockCodeForHistoricalTick()
            else:
                return None

        # 获取时间
        date = self.getRefDateTimeForHistoricalTick()
        if date is not None:
            self.__searchRefForHistoricalTick["date"] = date
        else:
            return None

        # 获取文件保存路径
        self.__searchRefForHistoricalTick["path"] = self.getRefSavePathForHistoricalTick()

        # 回返一个参数字典
        return self.__searchRefForHistoricalTick


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = TransactionDataWidgetForHistoricalTick()
    window.show()

    sys.exit(app.exec_())
