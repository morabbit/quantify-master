# -*- coding: utf-8 -*-

import sys
import xlrd

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataSubWidget.transactionDataWidgetForMarketIndexList import \
    TransactionDataWidgetForMarketIndexList


class TransactionDataWidgetForBigSingleTransactionData(TransactionDataWidgetForMarketIndexList):
    def __init__(self, parent=None):
        # print "StockDataWidgetForBigSingleTransactionData: init"
        super(TransactionDataWidgetForBigSingleTransactionData, self).__init__()

        # 创建本类管理的tab下的查询的参数
        self.__searchRefForBigSingleTransactionData = {}

        # 存放批量股票代码数据的列表
        self.__codeListForBigSingleTransactionData = []

        # 创建日历窗口，但是不显示
        self.__calenderForBigSingleTransactionData = Calendar()

        # 当点击起始时间，结束时间lineEdit的时候，弹出日历
        self.lineEditTransactionTimeForBigSingleTransactionData.LineEditClicked.connect(
            self.onLineEditStartTimeForBigSingleTransactionDataClicked)

        # 勾选上股票代码的时候，再显示是否显示需要输入具体的信息
        self.onChkBoxBulkModeForBigSingleTransactionDataClicked()
        self.chkBoxBulkModeForBigSingleTransactionData.clicked.connect(self.onChkBoxBulkModeForBigSingleTransactionDataClicked)

        # 批量导入按钮的信号与槽函数
        self.btnBulkModeForBigSingleTransactionData.clicked.connect(self.onBtnBulkModeForBigSingleTransactionDataClicked)

        # 保存路径
        self.btnSavePathForBigSingleTransactionData.clicked.connect(self.onBtnSavePathForBigSingleTransactionDataClicked)

    @QtCore.pyqtSlot()
    def onLineEditStartTimeForBigSingleTransactionDataClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calenderForBigSingleTransactionData.setLineEditObj(self.lineEditTransactionTimeForBigSingleTransactionData)

        # 显示日历窗口
        self.__calenderForBigSingleTransactionData.show()

    @QtCore.pyqtSlot()
    def onChkBoxBulkModeForBigSingleTransactionDataClicked(self):
        """检查是否需要调用批接口，显示批接口数据导入按钮"""

        # 检测“批量模式”复选框是否被选中，如果选中，显示“批量导入”按钮，并设置模式
        if self.chkBoxBulkModeForBigSingleTransactionData.isChecked():
            self.btnBulkModeForBigSingleTransactionData.show()
            self.__searchRefForBigSingleTransactionData["mode"] = "multiCode"
        else:
            self.btnBulkModeForBigSingleTransactionData.hide()
            self.__searchRefForBigSingleTransactionData["mode"] = "singleCode"

            # 清空lineEdit
            self.lineEditStockCodeForBigSingleTransactionData.clear()

        # 清空股票代码列表
        self.__codeListForBigSingleTransactionData = []

    @QtCore.pyqtSlot()
    def onBtnBulkModeForBigSingleTransactionDataClicked(self):
        """批量导入按钮的槽函数"""

        # 清空lineEdit
        self.lineEditStockCodeForBigSingleTransactionData.clear()

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
                    self.__codeListForBigSingleTransactionData += stockCodeList
                except:
                    QtWidgets.QMessageBox.warning(self, "错误！", "导入的股票代码表存在非法值", QtWidgets.QMessageBox.Cancel)
                    self.__codeListForBigSingleTransactionData = []
                    return

        # 将股票列表的代码号填写到linEdit中
        for stockCode in self.__codeListForBigSingleTransactionData:
            self.lineEditStockCodeForBigSingleTransactionData.insert("\"%s\", " % stockCode)

    @QtCore.pyqtSlot()
    def onBtnSavePathForBigSingleTransactionDataClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePathForBigSingleTransactionData.setText(path)

    def getRefSingleStockCodeForBigSingleTransactionData(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.lineEditStockCodeForBigSingleTransactionData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写股票代码", QtWidgets.QMessageBox.Cancel)
            return None
        try:
            int(self.lineEditStockCodeForBigSingleTransactionData.text())
        except:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码须为6位数字", QtWidgets.QMessageBox.Cancel)
            return None
        if 6 != len(self.lineEditStockCodeForBigSingleTransactionData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
            return None

        # 创建传参字典
        return self.lineEditStockCodeForBigSingleTransactionData.text()

    def getRefMultiStockCodeForBigSingleTransactionData(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.__codeListForBigSingleTransactionData) or self.__codeListForBigSingleTransactionData is None:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请导入股票代码文件", QtWidgets.QMessageBox.Cancel)
            return None
        for stockCode in self.__codeListForBigSingleTransactionData:
            if 6 == len(stockCode):
                QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
                return None

        # 返回股票代码列表
        return self.__codeListForBigSingleTransactionData

    def getRefDateTimeForBigSingleTransactionData(self):
        """获取时间"""

        # 判断是否选择了时间
        if 0 == len(self.lineEditTransactionTimeForBigSingleTransactionData.text()) or 0 == len(self.lineEditTransactionTimeForBigSingleTransactionData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写完整日期！", QtWidgets.QMessageBox.Cancel)
            return None

        # 获取参数
        date = self.lineEditTransactionTimeForBigSingleTransactionData.text()

        return date

    def getRefVolForBigSingleTransactionData(self):
        """获取手数"""

        # 判断是否输入了参数
        if 0 == len(self.lineEditLots.text()) or 0 == len(self.lineEditLots.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写手数！", QtWidgets.QMessageBox.Cancel)
            return None

        # 获取参数
        vol = self.lineEditLots.text()

        # 判断参数是否合法
        try:
            assert int(vol) >= 0
        except:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"手数需要填写一个正整数！", QtWidgets.QMessageBox.Cancel)
            return None

        return vol

    def getRefSavePathForBigSingleTransactionData(self):
        """获取文件保存路径"""

        # 容错
        if 0 == len(self.lineEditSavePathForBigSingleTransactionData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请设置保存路径", QtWidgets.QMessageBox.Cancel)
            return None

        return str(self.lineEditSavePathForBigSingleTransactionData.text())

    def getRefDictForBigSingleTransactionData(self):
        """获取历史行情参数字典"""

        # 如果是查询单只股票
        if self.__searchRefForBigSingleTransactionData["mode"] == "singleCode":
            # 获取参数，创建传参字典
            if self.getRefSingleStockCodeForBigSingleTransactionData() is not None:
                self.__searchRefForBigSingleTransactionData[
                    "code"] = self.getRefSingleStockCodeForBigSingleTransactionData()
            else:
                return None

        # 如果是查询多只股票
        if self.__searchRefForBigSingleTransactionData["mode"] == "multiCode":
            # 获取参数，创建传参字典
            if self.getRefMultiStockCodeForBigSingleTransactionData() is not None:
                self.__searchRefForBigSingleTransactionData[
                    "code"] = self.getRefMultiStockCodeForBigSingleTransactionData()
            else:
                return None

        # 获取日期
        date = self.getRefDateTimeForBigSingleTransactionData()
        if date is not None:
            self.__searchRefForBigSingleTransactionData["date"] = date
        else:
            return None

        # 获取手数
        vol = self.getRefVolForBigSingleTransactionData()
        if vol is not None:
            self.__searchRefForBigSingleTransactionData["vol"] = vol
        else:
            return None

        # 获取文件保存路径
        self.__searchRefForBigSingleTransactionData["path"] = self.getRefSavePathForBigSingleTransactionData()

        # 回返一个参数字典
        return self.__searchRefForBigSingleTransactionData


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = TransactionDataWidgetForBigSingleTransactionData()
    window.show()

    sys.exit(app.exec_())
