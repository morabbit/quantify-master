# -*- coding: utf-8 -*-

import sys
import xlrd
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataWidgetBase import TransactionDataWidgetBase

# 历史行情数据的查询数据类型列表
ktypeList = ["D", "W", "M", "5", "15", "30", "60"]


class TransactionDataWidgetForHistoricalQuotation(TransactionDataWidgetBase):
    '''历史行情tab'''

    def __init__(self, parent=None):
        # 调用父类方法
        # print "StockDataWidgetForHistoricalQuotation: init"
        super(TransactionDataWidgetForHistoricalQuotation, self).__init__()

        # 创建本类管理的tab下的查询的参数
        self.__searchRefForHistoricalQuotation = {}

        # 存放批量股票代码数据的列表
        self.__codeListForHistoricalQuotation = []

        # 创建日历窗口，但是不显示
        self.__calenderForHistoricalQuotation = Calendar()

        # 勾选上股票代码的时候，再显示是否显示需要输入具体的信息
        self.isShowTheStockCodeInputForHistoricalQuotation()

        # 统一管理所有的复选框
        self.__chkBoxDictForHistoricalQuotation = {}
        self.__chkBoxDictForHistoricalQuotation[self.chkBoxSH] = "sh"
        self.__chkBoxDictForHistoricalQuotation[self.chkBoxSZ] = "sz"
        self.__chkBoxDictForHistoricalQuotation[self.chkBoxHS300] = "hs300"
        self.__chkBoxDictForHistoricalQuotation[self.chkBoxSZ50] = "sz50"
        self.__chkBoxDictForHistoricalQuotation[self.chkBoxZXB] = "zxb"
        self.__chkBoxDictForHistoricalQuotation[self.chkBoxCYB] = "cyb"

        # 所有的checkBox的信号和槽函数
        self.chkBoxSH.clicked.connect(self.onChkBoxClicked)
        self.chkBoxSZ.clicked.connect(self.onChkBoxClicked)
        self.chkBoxHS300.clicked.connect(self.onChkBoxClicked)
        self.chkBoxSZ50.clicked.connect(self.onChkBoxClicked)
        self.chkBoxZXB.clicked.connect(self.onChkBoxClicked)
        self.chkBoxCYB.clicked.connect(self.onChkBoxClicked)
        self.chkBoxStockCode.clicked.connect(self.onChkBoxClicked)

        self.chkBoxBulkModeForHistoricalQuotation.clicked.connect(self.onChkBoxBulkModeForHistoricalQuotationClicked)

        # 当点击起始时间，结束时间lineEdit的时候，弹出日历
        self.lineEditStartTimeForHistoricalQuotation.LineEditClicked.connect(self.onLineEditStartTimeForHistoricalQuotationClicked)
        self.lineEditEndTimeForHistoricalQuotation.LineEditClicked.connect(self.onLineEditEndTimeForHistoricalQuotationClicked)

        # 批量导入按钮的信号与槽函数
        self.btnBulkModeForHistoricalQuotation.clicked.connect(self.onBtnBulkModeForHistoricalQuotationClicked)

        # 保存路径
        self.btnSavePathForHistoricalQuotation.clicked.connect(self.onBtnSavePathForHistoricalQuotationClicked)

    def getRefDateSourceForHistoricalQuotation(self):
        """获取数据源"""

        # 判断哪个复选框被选中
        for chkBox in self.__chkBoxDictForHistoricalQuotation:
            if chkBox.isChecked():
                return "index", self.__chkBoxDictForHistoricalQuotation[chkBox]

        # 如果用户选择为“股票代码”， 进一步判断是否为批量模式
        if self.chkBoxStockCode.isChecked() and not self.chkBoxBulkModeForHistoricalQuotation.isChecked():
            return "singleCode", None
        elif self.chkBoxStockCode.isChecked() and not self.chkBoxBulkModeForHistoricalQuotation.isChecked():
            return "multiCode", None

        # 如果没有复选框被选中
        QtWidgets.QMessageBox.warning(self, u"错误！", u"请选择一个数据源", QtWidgets.QMessageBox.Cancel)
        return None, None

    def getRefDateTimeForHistoricalQuotation(self):
        """获取时间"""

        # 都不填写，表示不需要时间
        if 0 == len(self.lineEditStartTimeForHistoricalQuotation.text()) and 0 == len(self.lineEditEndTimeForHistoricalQuotation.text()):
            return None, None

        # 判断是否选择了时间
        if 0 == len(self.lineEditStartTimeForHistoricalQuotation.text()) or 0 == len(self.lineEditEndTimeForHistoricalQuotation.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写完整日期！", QtWidgets.QMessageBox.Cancel)
            return None, None

        # 起始和终止时间需要合法
        startDate = datetime.datetime.strptime(self.lineEditStartTimeForHistoricalQuotation.text(), '%Y-%m-%d')
        endDate = datetime.datetime.strptime(self.lineEditEndTimeForHistoricalQuotation.text(), '%Y-%m-%d')
        if startDate >= endDate:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"日期非法！", QtWidgets.QMessageBox.Cancel)
            return None, None

        # 获取参数
        start = self.lineEditStartTimeForHistoricalQuotation.text()
        end = self.lineEditEndTimeForHistoricalQuotation.text()

        return start, end

    def getRefSingleStockCodeForHistoricalQuotation(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if len(self.lineEditStockCodeForHistoricalQuotation.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写股票代码", QtWidgets.QMessageBox.Cancel)
            return None
        try:
            int(self.lineEditStockCodeForHistoricalQuotation.text())
        except:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码须为6位数字", QtWidgets.QMessageBox.Cancel)
            return None
        if 6 != len(self.lineEditStockCodeForHistoricalQuotation.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
            return None

        # 创建传参字典
        return self.lineEditStockCodeForHistoricalQuotation.text()

    def getRefMultiStockCodeForHistoricalQuotation(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.__codeListForHistoricalQuotation) or self.__codeListForHistoricalQuotation is None:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请导入股票代码文件", QtWidgets.QMessageBox.Cancel)
            return None
        for stockCode in self.__codeListForHistoricalQuotation:
            if 6 == len(stockCode):
                QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
                return None

        # 返回股票代码列表
        return self.__codeListForHistoricalQuotation

    def isShowTheStockCodeInputForHistoricalQuotation(self):
        """检查是否需要显示股票代码输入接口"""
        if self.chkBoxStockCode.isChecked():
            self.labStockCodeForHistoricalQuotation.show()          # 显示股票代码输入标签
            self.lineEditStockCodeForHistoricalQuotation.show()     # 显示股票代码输入栏
            self.chkBoxBulkModeForHistoricalQuotation.show()        # 显示批量输入复选框
        else:
            self.labStockCodeForHistoricalQuotation.hide()          # 隐藏股票代码输入标签
            self.lineEditStockCodeForHistoricalQuotation.hide()     # 隐藏股票代码输入栏
            self.chkBoxBulkModeForHistoricalQuotation.hide()        # 隐藏批量输入复选框

        self.onChkBoxBulkModeForHistoricalQuotationClicked()

    @QtCore.pyqtSlot()
    def onLineEditStartTimeForHistoricalQuotationClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calenderForHistoricalQuotation.setLineEditObj(self.lineEditStartTimeForHistoricalQuotation)

        # 显示日历窗口
        self.__calenderForHistoricalQuotation.show()

    @QtCore.pyqtSlot()
    def onLineEditEndTimeForHistoricalQuotationClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calenderForHistoricalQuotation.setLineEditObj(self.lineEditEndTimeForHistoricalQuotation)

        # 显示日历窗口
        self.__calenderForHistoricalQuotation.show()

    @QtCore.pyqtSlot()
    def onChkBoxClicked(self):
        # 是否显示批接口控件
        self.isShowTheStockCodeInputForHistoricalQuotation()

    @QtCore.pyqtSlot()
    def onChkBoxBulkModeForHistoricalQuotationClicked(self):
        """检查是否需要调用批接口，显示批接口数据导入按钮"""

        # 检测“批量模式”复选框是否被选中，如果选中，显示“批量导入”按钮
        if self.chkBoxBulkModeForHistoricalQuotation.isChecked():
            self.btnBulkModeForHistoricalQuotation.show()
        else:
            self.btnBulkModeForHistoricalQuotation.hide()

            # 清空lineEdit
            self.lineEditStockCodeForHistoricalQuotation.clear()

        # 清空股票代码列表
        self.__codeListForHistoricalQuotation = []

    @QtCore.pyqtSlot()
    def onBtnBulkModeForHistoricalQuotationClicked(self):
        """批量导入按钮的槽函数"""

        # 清空lineEdit
        self.lineEditStockCodeForHistoricalQuotation.clear()

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
                    self.__codeListForHistoricalQuotation += stockCodeList
                except:
                    QtWidgets.QMessageBox.warning(self, "错误！", "导入的股票代码表存在非法值", QtWidgets.QMessageBox.Cancel)
                    self.__codeListForHistoricalQuotation = []
                    return

        # 将股票列表的代码号填写到linEdit中
        for stockCode in self.__codeListForHistoricalQuotation:
            self.lineEditStockCodeForHistoricalQuotation.insert("\"%s\", " % stockCode)

    @QtCore.pyqtSlot()
    def onBtnSavePathForHistoricalQuotationClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePathForHistoricalQuotation.setText(path)

    def getRefSavePathForHistoricalQuotation(self):
        """获取文件保存路径"""

        # 容错
        if 0 == len(self.lineEditSavePathForHistoricalQuotation.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请设置保存路径", QtWidgets.QMessageBox.Cancel)
            return None

        return str(self.lineEditSavePathForHistoricalQuotation.text())

    def getRefDictForHistoricalQuotation(self):
        """获取历史行情参数字典"""

        # 获取数据源
        mode, code = self.getRefDateSourceForHistoricalQuotation()
        if mode is not None:
            self.__searchRefForHistoricalQuotation["mode"] = mode
            self.__searchRefForHistoricalQuotation["code"] = code
        else:
            return None

        # 如果是查询单只股票
        if self.__searchRefForHistoricalQuotation["mode"] == "singleCode":
            # 获取参数，创建传参字典
            if self.getRefSingleStockCodeForHistoricalQuotation() is not None:
                self.__searchRefForHistoricalQuotation["code"] = self.getRefSingleStockCodeForHistoricalQuotation()
            else:
                return None

        # 如果是查询多只股票
        if self.__searchRefForHistoricalQuotation["mode"] == "multiCode":
            # 获取参数，创建传参字典
            if self.getRefMultiStockCodeForHistoricalQuotation() is not None:
                self.__searchRefForHistoricalQuotation["code"] = self.getRefMultiStockCodeForHistoricalQuotation()
            else:
                return None

        # 获取时间
        start, end = self.getRefDateTimeForHistoricalQuotation()
        if start is not None and end is not None:
            self.__searchRefForHistoricalQuotation["start"] = start
            self.__searchRefForHistoricalQuotation["end"] = end
        else:
            return None

        # 获取数据类型
        self.__searchRefForHistoricalQuotation["ktype"] = ktypeList[self.comboBoxDataType.currentIndex()]

        # 获取文件保存路径
        self.__searchRefForHistoricalQuotation["path"] = self.getRefSavePathForHistoricalQuotation()

        # 回返一个参数字典
        return self.__searchRefForHistoricalQuotation


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = TransactionDataWidgetForHistoricalQuotation()
    window.show()

    sys.exit(app.exec_())
