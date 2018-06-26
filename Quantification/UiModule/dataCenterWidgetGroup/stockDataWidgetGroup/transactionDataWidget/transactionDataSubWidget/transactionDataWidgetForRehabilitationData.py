# -*- coding: utf-8 -*-

import sys
import datetime
import xlrd

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataSubWidget.transactionDataWidgetForHistoricalQuotation import TransactionDataWidgetForHistoricalQuotation

# 复权类型列表
autypeList = ["qfq", "hfq", "None"]


class TransactionDataWidgetForRehabilitationData(TransactionDataWidgetForHistoricalQuotation):
    '''复权数据tab'''

    def __init__(self, parent=None):
        # 调用父类方法
        # print "StockDataWidgetForRehabilitationData: init"
        super(TransactionDataWidgetForRehabilitationData, self).__init__()

        # 创建本类管理的tab下的查询的参数
        self.__searchRefForRehabilitationData = {}

        # 存放批量股票代码数据的列表
        self.__codeListForRehabilitationData = []

        # 创建日历窗口，但是不显示
        self.__calenderForRehabilitationData = Calendar()

        # 当点击起始时间，结束时间lineEdit的时候，弹出日历
        self.lineEditStartTimeForRehabilitationData.LineEditClicked.connect(self.onLineEditStartTimeForRehabilitationDataClicked)
        self.lineEditEndTimeForRehabilitationData.LineEditClicked.connect(self.onLineEditEndTimeForRehabilitationDataClicked)

        # 点击复选框，是否显示“批量导入按钮”
        self.onChkBoxBulkModeForRehabilitationDataClicked()
        self.chkBoxBulkModeForRehabilitationData.clicked.connect(self.onChkBoxBulkModeForRehabilitationDataClicked)

        # 批量导入按钮的信号与槽函数
        self.btnBulkModeForRehabilitationData.clicked.connect(self.onBtnBulkModeForRehabilitationDataClicked)

        # 保存路径
        self.btnSavePathForRehabilitationData.clicked.connect(self.onBtnSavePathForRehabilitationDataClicked)

    @QtCore.pyqtSlot()
    def onLineEditStartTimeForRehabilitationDataClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calenderForRehabilitationData.setLineEditObj(self.lineEditStartTimeForRehabilitationData)

        # 显示日历窗口
        self.__calenderForRehabilitationData.show()

    @QtCore.pyqtSlot()
    def onLineEditEndTimeForRehabilitationDataClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calenderForRehabilitationData.setLineEditObj(self.lineEditEndTimeForRehabilitationData)

        # 显示日历窗口
        self.__calenderForRehabilitationData.show()

    @QtCore.pyqtSlot()
    def onChkBoxBulkModeForRehabilitationDataClicked(self):
        """检查是否需要显示批量输入按钮"""
        if self.chkBoxBulkModeForRehabilitationData.isChecked():
            self.btnBulkModeForRehabilitationData.show()     # 显示批量输入按钮
            self.__searchRefForRehabilitationData["mode"] = "multiCode"
        else:
            self.btnBulkModeForRehabilitationData.hide()     # 隐藏批量输入按钮
            self.__searchRefForRehabilitationData["mode"] = "singleCode"

    @QtCore.pyqtSlot()
    def onBtnBulkModeForRehabilitationDataClicked(self):
        """批量导入按钮的槽函数"""

        # 清空lineEdit
        self.lineEditStockCodeForRehabilitationData.clear()

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
                    self.__codeListForRehabilitationData += stockCodeList
                except:
                    QtWidgets.QMessageBox.warning(self, "错误！", "导入的股票代码表存在非法值", QtWidgets.QMessageBox.Cancel)
                    self.__codeListForRehabilitationData = []
                    return

        # 将股票列表的代码号填写到linEdit中
        for stockCode in self.__codeListForRehabilitationData:
            self.lineEditStockCodeForRehabilitationData.insert("\"%s\", " % stockCode)

    @QtCore.pyqtSlot()
    def onBtnSavePathForRehabilitationDataClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePathForRehabilitationData.setText(path)

    def getRefSingleStockCodeForRehabilitationData(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.lineEditStockCodeForRehabilitationData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写股票代码", QtWidgets.QMessageBox.Cancel)
            return None
        try:
            int(self.lineEditStockCodeForRehabilitationData.text())
        except:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码须为6位数字", QtWidgets.QMessageBox.Cancel)
            return None
        if 6 != len(self.lineEditStockCodeForRehabilitationData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
            return None

        # 返回股票代码
        return self.lineEditStockCodeForRehabilitationData.text()

    def getRefMultiStockCodeForRehabilitationData(self):
        """获取单只股票数据参数"""

        # 判断输入的股票代码是否合法
        if 0 == len(self.__codeListForRehabilitationData) or self.__codeListForRehabilitationData is None:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请导入股票代码文件", QtWidgets.QMessageBox.Cancel)
            return None
        for stockCode in self.__codeListForRehabilitationData:
            if 6 == len(stockCode):
                QtWidgets.QMessageBox.warning(self, u"错误！", u"股票代码长度须为6", QtWidgets.QMessageBox.Cancel)
                return None

        # 创建传参字典
        return self.__codeListForRehabilitationData

    def getRefDateTimeForRehabilitationData(self):
        """获取时间"""

        # 都不填写，表示不需要时间
        if 0 == len(self.lineEditStartTimeForRehabilitationData.text()) and 0 == len(self.lineEditEndTimeForRehabilitationData.text()):
            return None, None

        # 判断是否选择了时间
        if 0 == len(self.lineEditStartTimeForRehabilitationData.text()) or 0 == len(self.lineEditEndTimeForRehabilitationData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写完整日期！", QtWidgets.QMessageBox.Cancel)
            return None, None

        # 起始和终止时间需要合法
        startDate = datetime.datetime.strptime(self.lineEditStartTimeForRehabilitationData.text(), '%Y-%m-%d')
        endDate = datetime.datetime.strptime(self.lineEditEndTimeForRehabilitationData.text(), '%Y-%m-%d')
        if startDate >= endDate:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"日期非法！", QtWidgets.QMessageBox.Cancel)
            return None, None

        # 获取参数
        start = self.lineEditStartTimeForRehabilitationData.text()
        end = self.lineEditEndTimeForRehabilitationData.text()

        return start, end

    def getRefIndexForRehabilitationData(self):
        """判断是否是大盘数据"""

        # 如果两个都没有选中，默认选中“是”
        if not self.chkBoxYes.isChecked() and not self.chkBoxNo.isChecked():
            self.chkBoxYes.setChecked(True)

        # 判断用户选中了拿个选项
        if self.chkBoxYes.isChecked() and not self.chkBoxNo.isChecked():
            return True
        else:
            return False

    def getRefSavePathForRehabilitationData(self):
        """获取文件保存路径"""

        # 容错
        if 0 == len(self.lineEditSavePathForRehabilitationData.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请设置保存路径", QtWidgets.QMessageBox.Cancel)
            return None

        return str(self.lineEditSavePathForRehabilitationData.text())

    def getRefDictForRehabilitationData(self):
        """获取复权数据参数字典"""

        # 如果是查询单只股票
        if self.__searchRefForRehabilitationData["mode"] == "singleCode":
            # 获取参数，创建传参字典
            if self.getRefSingleStockCodeForRehabilitationData() is not None:
                self.__searchRefForRehabilitationData["code"] = self.getRefSingleStockCodeForRehabilitationData()
            else:
                return None

        # 如果是查询多只股票
        if self.__searchRefForRehabilitationData["mode"] == "multiCode":
            # 获取参数，创建传参字典
            if self.getRefMultiStockCodeForRehabilitationData() is not None:
                self.__searchRefForRehabilitationData["code"] = self.getRefMultiStockCodeForRehabilitationData()
            else:
                return None

        # 获取时间
        start, end = self.getRefDateTimeForRehabilitationData()
        if start is not None and end is not None:
            self.__searchRefForRehabilitationData["start"] = start
            self.__searchRefForRehabilitationData["end"] = end
        else:
            return None

        # 获取复权类型
        self.__searchRefForRehabilitationData["autype"] = autypeList[self.comboBoxRehabilitationType.currentIndex()]

        # 是否是大盘指数
        self.__searchRefForRehabilitationData["index"] = self.getRefIndexForRehabilitationData()

        # 获取文件保存路径
        self.__searchRefForRehabilitationData["path"] = self.getRefSavePathForRehabilitationData()

        # 回返一个参数字典
        return self.__searchRefForRehabilitationData


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = TransactionDataWidgetForRehabilitationData()
    window.show()

    sys.exit(app.exec_())
