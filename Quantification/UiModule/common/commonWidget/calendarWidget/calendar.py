# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from UiModule.common.commonWidget.calendarWidget.calendar_ui import Ui_calendarWidget


class Calendar(QtWidgets.QWidget, Ui_calendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        # 固定大小
        self.setGeometry(300, 300, 350, 300)

        # 设置为模态
        self.setWindowModality(QtCore.Qt.WindowModal)

        # 获取创建类的日期数据指针
        self.__lineEdit = None

        # 每当日历上日期被点击的时候，微博版框里的数据要变化
        self.calendar.selectionChanged.connect(self.showDate)

        # 确定按钮
        self.btnOK.clicked.connect(self.onBtnOKClicked)

        # 取消按钮
        self.btnCancel.clicked.connect(self.onBtnCancelClicked)

        # 对象被创建的时候，先获取一次时间
        self.showDate()

        # self.show()
        # self.exec_()

    def setLineEditObj(self, lineEdit):
        """设置时间需要返回给那个lineEdit"""
        self.__lineEdit = lineEdit

    @QtCore.pyqtSlot()
    def showDate(self):
        """"为界面文本框设置时间"""
        date = self.calendar.selectedDate()
        self.labelData.setText(str(date.toPyDate()))

    @QtCore.pyqtSlot()
    def onBtnOKClicked(self):
        """点击“确定”，获取选中的时间信息"""
        if self.__lineEdit is not None:
            self.__lineEdit.setText(str(self.labelData.text()))
        self.__lineEdit = None
        self.close()

    @QtCore.pyqtSlot()
    def onBtnCancelClicked(self):
        """点击“取消”，时间信息清零，关闭窗口"""
        if self.__lineEdit is not None:
            self.__lineEdit.setText('')
        self.__lineEdit = None
        self.close()


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Calendar()
    window.show()

    sys.exit(app.exec_())
