# -*- coding: utf-8 -*-

import datetime
import sys

from PyQt5 import QtCore, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.dataCenterWidgetGroup.futuresDataWidget.futuresDataWidget_ui import Ui_futureDataWidget


class FutureDataWidget(QtWidgets.QWidget, Ui_futureDataWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        # 用户需要查询那些数据（记录那些checkbox被选中）
        self.__marketDataSourceList = []

        # 查询数据的传参字典
        self.__refDict = {}

        # 创建日历窗口，但是不显示
        self.__calender = Calendar()

        # 当点击起始时间，结束时间lineEdit的时候，弹出日历
        self.lineEditStartTime.LineEditClicked.connect(self.onLineEditStartTimeClicked)
        self.lineEditEndTime.LineEditClicked.connect(self.onLineEditEndTimeClicked)

        # 所有的chkbox的点击事件
        self.chkBoxSH.clicked.connect(self.onChkBoxChicked)         # 中金所
        self.chkBoxSZ.clicked.connect(self.onChkBoxChicked)         # 郑商所
        self.chkBoxHS300.clicked.connect(self.onChkBoxChicked)      # 上期所
        self.chkBoxSZ50.clicked.connect(self.onChkBoxChicked)       # 大商所

        # 所有的按钮事件
        self.btnSelectSavePath.clicked.connect(self.onBtnSelectSavePathClicked)
        self.btnSaveToCSV.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToExcel.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToHDF5.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToJSON.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToMySQL.clicked.connect(self.onBtnSaveClicked)
        self.btnSaveToMongoDB.clicked.connect(self.onBtnSaveClicked)

    def getRefDict(self):
        """获取用户选择的数据，如果数据有误，返回False"""

        # 判断参数是否正确
        if 0 == len(self.__marketDataSourceList):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请选择数据来源！", QtWidgets.QMessageBox.Cancel)
            return False

        # 需要有起始和终止时间
        if 0 == len(self.lineEditStartTime.text()) or 0 == len(self.lineEditEndTime.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请填写完整日期！", QtWidgets.QMessageBox.Cancel)
            return False

        # 起始和终止时间需要合法
        startDate = datetime.datetime.strptime(self.lineEditStartTime.text(), '%Y-%m-%d')
        endDate = datetime.datetime.strptime(self.lineEditEndTime.text(), '%Y-%m-%d')
        if startDate >= endDate:
            QtWidgets.QMessageBox.warning(self, u"错误！", u"日期非法！", QtWidgets.QMessageBox.Cancel)
            return False

        # 创建传参字典
        self.__refDict["market"] = self.__marketDataSourceList
        self.__refDict["startTime"] = str(self.lineEditStartTime.text())
        self.__refDict["endTime"] = str(self.lineEditEndTime.text())
        return True

    def appendDataSourceToList(self, chkBox, ref):
        """判断数据源列表中需要添加还是删除数据"""

        # 容错
        if chkBox is None:
            return

        # 判断参数的添加与删除
        if chkBox.isChecked():
            self.__marketDataSourceList.append(ref)
        else:
            self.__marketDataSourceList.remove(ref)

    @QtCore.pyqtSlot()
    def onBtnSelectSavePathClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePath.setText(path)

    @QtCore.pyqtSlot()
    def onBtnSaveClicked(self):
        """各个保存按钮按下的时候的槽函数"""

        # 先获取一下需要传递的参数，如果数据有误，退出函数
        if not self.getRefDict():
            return

        # 获取用户想要保存的数据路径
        if 0 == len(self.lineEditSavePath.text()) or 0 == len(self.lineEditSavePath.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请输入保存路径！", QtWidgets.QMessageBox.Cancel)
            return
        self.__refDict["path"] = str(self.lineEditSavePath.text())

        print(self.__refDict)

        # 调取数据模块的接口
        if self.btnSaveToCSV == self.sender():
            print (self.__refDict)
            for market in self.__refDict["market"]:
                DataBasic.get_futures(self.__refDict["startTime"], self.__refDict["endTime"], market)

        elif self.btnSaveToExcel == self.sender():
            pass # todo
        elif self.btnSaveToHDF5 == self.sender():
            pass # todo
        elif self.btnSaveToJSON == self.sender():
            pass # todo
        elif self.btnSaveToMySQL == self.sender():
            pass # todo
        elif self.btnSaveToMongoDB == self.sender():
            pass # todo
        else:
            return

    @QtCore.pyqtSlot()
    def onChkBoxChicked(self):
        """当复选框被选中的时候"""

        # 中金所
        if self.chkBoxSH == self.sender():
            self.appendDataSourceToList(self.sender(), 'CFFEX')
        # 郑商所
        elif self.chkBoxSZ == self.sender():
            self.appendDataSourceToList(self.sender(), "CZCE")
        # 上期所
        elif self.chkBoxHS300 == self.sender():
            self.appendDataSourceToList(self.sender(), "SHFE")
        # 大商所
        elif self.chkBoxSZ50 == self.sender():
            self.appendDataSourceToList(self.sender(), "DCE")

    @QtCore.pyqtSlot()
    def onLineEditStartTimeClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calender.setLineEditObj(self.lineEditStartTime)

        # 显示日历窗口
        self.__calender.show()

    @QtCore.pyqtSlot()
    def onLineEditEndTimeClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calender.setLineEditObj(self.lineEditEndTime)

        # 显示日历窗口
        self.__calender.show()


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = FutureDataWidget()
    window.show()

    sys.exit(app.exec_())
