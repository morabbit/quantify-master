# -*- coding: utf-8 -*-

import sys
import xlrd

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataSubWidget.transactionDataWidgetForHistoricalTick import \
    TransactionDataWidgetForHistoricalTick


class TransactionDataWidgetForRealTimeTick(TransactionDataWidgetForHistoricalTick):
    def __init__(self, parent=None):
        # print "StockDataWidgetForRealTimeTick: init"
        super(TransactionDataWidgetForRealTimeTick, self).__init__()

        # 创建本类管理的tab下的查询的参数
        self.__searchRefForRealTimeTick = {}

        # 存放批量股票代码数据的列表
        self.__codeListForRealTimeTick = []

        # 创建日历窗口，但是不显示
        self.__calenderForRealTimeTick = Calendar()

        # 统一管理所有的复选框
        self.__chkBoxDictForRealTimeTick = {}
        self.__chkBoxDictForRealTimeTick[self.chkBoxSHForRealTimeTick] = "sh"
        self.__chkBoxDictForRealTimeTick[self.chkBoxSZForRealTimeTick] = "sz"
        self.__chkBoxDictForRealTimeTick[self.chkBoxHS300ForRealTimeTick] = "hs300"
        self.__chkBoxDictForRealTimeTick[self.chkBoxSZ50ForRealTimeTick] = "sz50"
        self.__chkBoxDictForRealTimeTick[self.chkBoxZXBForRealTimeTick] = "zxb"
        self.__chkBoxDictForRealTimeTick[self.chkBoxCYBForRealTimeTick] = "cyb"

        # 勾选上股票代码的时候，再显示是否显示需要输入具体的信息
        self.isShowTheStockCodeInputForRealTimeTick()
        self.chkBoxStockCodeForRealTimeTick.clicked.connect(self.isShowTheStockCodeInputForRealTimeTick)
        self.chkBoxBulkModeForRealTimeTick.clicked.connect(self.onChkBoxBulkModeForRealTimeTickClicked)

        # 批量导入按钮的信号与槽函数
        self.btnBulkModeForRealTimeTick.clicked.connect(self.onBtnBulkModeForRealTimeTickClicked)

        # 保存路径
        self.btnSavePathForRealTimeTick.clicked.connect(self.onBtnSavePathForRealTimeTickClicked)

    @QtCore.pyqtSlot()
    def isShowTheStockCodeInputForRealTimeTick(self):
        """检查是否需要显示股票代码输入接口"""
        if self.chkBoxStockCodeForRealTimeTick.isChecked():
            self.labStockCodeForRealTimeTick.show()          # 显示股票代码输入标签
            self.lineEditStockCodeForRealTimeTick.show()     # 显示股票代码输入栏
            self.chkBoxBulkModeForRealTimeTick.show()        # 显示批量输入复选框
        else:
            self.labStockCodeForRealTimeTick.hide()          # 隐藏股票代码输入标签
            self.lineEditStockCodeForRealTimeTick.hide()     # 隐藏股票代码输入栏
            self.chkBoxBulkModeForRealTimeTick.hide()        # 隐藏批量输入复选框

        # 是否显示批量输入按钮
        self.onChkBoxBulkModeForRealTimeTickClicked()

    @QtCore.pyqtSlot()
    def onChkBoxBulkModeForRealTimeTickClicked(self):
        """检查是否需要调用批接口，显示批接口数据导入按钮"""

        # 检测“批量模式”复选框是否被选中，如果选中，显示“批量导入”按钮
        if self.chkBoxBulkModeForRealTimeTick.isChecked():
            self.btnBulkModeForRealTimeTick.show()
        else:
            self.btnBulkModeForRealTimeTick.hide()

            # 清空lineEdit
            self.lineEditStockCodeForRealTimeTick.clear()

        # 清空股票代码列表
        self.__codeListForRealTimeTick = []

    @QtCore.pyqtSlot()
    def onBtnBulkModeForRealTimeTickClicked(self):
        """批量导入按钮的槽函数"""

        # 清空lineEdit
        self.lineEditStockCodeForRealTimeTick.clear()

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
                    stockCodeList = list(map(str, map(int, sheet_name.col_values(index))))
                    self.__codeListForRealTimeTick += stockCodeList
                except:
                    QtWidgets.QMessageBox.warning(self, "错误！", "导入的股票代码表存在非法值", QtWidgets.QMessageBox.Cancel)
                    self.__codeListForRealTimeTick = []
                    return

        # 将股票列表的代码号填写到linEdit中
        for stockCode in self.__codeListForRealTimeTick:
            self.lineEditStockCodeForRealTimeTick.insert("\"%s\", " % stockCode)

    def onBtnSavePathForRealTimeTickClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePathForRealTimeTick.setText(path)

    def getRefDateSourceForRealTimeTick(self):
        """获取数据源"""

        # 判断哪个复选框被选中
        for chkBox in self.__chkBoxDictForRealTimeTick:
            if chkBox.isChecked():
                return "index", self.__chkBoxDictForRealTimeTick[chkBox]

        # 如果用户选择为“股票代码”， 进一步判断是否为批量模式
        if self.chkBoxStockCodeForRealTimeTick.isChecked() and not self.chkBoxBulkModeForRealTimeTick.isChecked():
            return "singleCode", None
        elif self.chkBoxStockCodeForRealTimeTick.isChecked() and not self.chkBoxBulkModeForRealTimeTick.isChecked():
            return "multiCode", None

        # 如果没有复选框被选中
        QtWidgets.QMessageBox.warning(self, u"错误！", u"请选择一个数据源", QtWidgets.QMessageBox.Cancel)
        return None, None

    def getRefSingleStockCodeForRealTimeTick(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.lineEditStockCodeForRealTimeTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写股票代码", QtWidgets.QMessageBox.Cancel)
            return None
        try:
            int(self.lineEditStockCodeForRealTimeTick.text())
        except:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码须为6位数字", QtWidgets.QMessageBox.Cancel)
            return None
        if 6 != len(self.lineEditStockCodeForRealTimeTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
            return None

        # 创建传参字典
        return self.lineEditStockCodeForRealTimeTick.text()

    def getRefMultiStockCodeForRealTimeTick(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.__codeListForRealTimeTick) or self.__codeListForRealTimeTick is None:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请导入股票代码文件", QtWidgets.QMessageBox.Cancel)
            return None
        for stockCode in self.__codeListForRealTimeTick:
            if 6 == len(stockCode):
                QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
                return None

        # 返回股票代码列表
        return self.__codeListForRealTimeTick

    def getRefSavePathForRealTimeTick(self):
        """获取文件保存路径"""

        # 容错
        if 0 == len(self.lineEditSavePathForRealTimeTick.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请设置保存路径", QtWidgets.QMessageBox.Cancel)
            return None

        return str(self.lineEditSavePathForRealTimeTick.text())

    def getRefDictForRealTimeTick(self):
        """获取历史行情参数字典"""

        # 获取数据源
        mode, code = self.getRefDateSourceForRealTimeTick()
        if mode is not None:
            self.__searchRefForRealTimeTick["mode"] = mode
            self.__searchRefForRealTimeTick["symbols"] = code
        else:
            return None

        # 如果是查询单只股票
        if self.__searchRefForRealTimeTick["mode"] == "singleCode":
            # 获取参数，创建传参字典
            if self.getRefSingleStockCodeForRealTimeTick() is not None:
                self.__searchRefForRealTimeTick["symbols"] = self.getRefSingleStockCodeForRealTimeTick()
            else:
                return None

        # 如果是查询多只股票
        if self.__searchRefForRealTimeTick["mode"] == "multiCode":
            # 获取参数，创建传参字典
            if self.getRefMultiStockCodeForRealTimeTick() is not None:
                self.__searchRefForRealTimeTick["symbols"] = self.getRefMultiStockCodeForRealTimeTick()
            else:
                return None

        # 获取文件保存路径
        self.__searchRefForRealTimeTick["path"] = self.getRefSavePathForRealTimeTick()

        # 回返一个参数字典
        return self.__searchRefForRealTimeTick


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = TransactionDataWidgetForRealTimeTick()
    window.show()

    sys.exit(app.exec_())
