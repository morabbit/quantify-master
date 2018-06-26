# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from UiModule.common.commonWidget.calendarWidget.calendar import Calendar
from UiModule.strategyCenterWidgetGroup.strategyMgrWidget.strategyMgrWidget_ui import Ui_strategyMgrWidget


class StrategyMgrWidget(QtWidgets.QWidget, Ui_strategyMgrWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        # 创建日历窗口，但是不显示
        self.__calender = Calendar()

        # 当点击创建时间，修改时间lineEdit的时候，弹出日历
        self.lineEditCreateTime.LineEditClicked.connect(self.onLineEditCreateTimeClicked)
        self.lineEditModifyTime.LineEditClicked.connect(self.onLineEditModifyTimeClicked)

    @QtCore.pyqtSlot()
    def onLineEditCreateTimeClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calender.setLineEditObj(self.lineEditCreateTime)

        # 显示日历窗口
        self.__calender.show()

    @QtCore.pyqtSlot()
    def onLineEditModifyTimeClicked(self):
        # 设置要修改的文本编辑窗口
        self.__calender.setLineEditObj(self.lineEditModifyTime)

        # 显示日历窗口
        self.__calender.show()


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = StrategyMgrWidget()
    window.show()

    sys.exit(app.exec_())
