# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from UiModule.mainWindow_ui import Ui_mainWindow
from UiModule.strategyCenterWidgetGroup.quickNewStrategyWidget.quickNewStrategyWidget import QuickNewStrategyWidget
from UiModule.strategyCenterWidgetGroup.newStrategyWidget.newStrategyWidget import NewStrategyWidget
from UiModule.strategyCenterWidgetGroup.strategyMgrWidget.strategyMgrWidget import StrategyMgrWidget
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataWidget import StockDataWidget
from UiModule.dataCenterWidgetGroup.futuresDataWidget.futuresDataWidget import FutureDataWidget


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.__subWidgetList = []   # 统一管理所有的子窗口

        # 实例化所有的子窗口，统一使用列表管理
        self.__strategyMgrWidget = StrategyMgrWidget(self.widget)
        self.__subWidgetList.append(self.__strategyMgrWidget)

        self.__newStrategyWidget = NewStrategyWidget(self.widget)
        self.__subWidgetList.append(self.__newStrategyWidget)

        self.__quickNewStrategyWidget = QuickNewStrategyWidget(self.widget)
        self.__subWidgetList.append(self.__quickNewStrategyWidget)

        self.__stockDataWidget = StockDataWidget(self.widget)
        self.__subWidgetList.append(self.__stockDataWidget)

        self.__futureDataWidget = FutureDataWidget(self.widget)
        self.__subWidgetList.append(self.__futureDataWidget)

        # self.__stockDataWidget = StockDataWidget(self.widget)
        # self.__subWidgetList.append(self.__stockDataWidget)

        # 将所有的子窗口放入主界面中，但是不显示
        self.adaptAllSubWidgetToWindow()
        self.allSubWidgetHide()

        # 连接所有的信号和槽
        self.actionStrategyMgr.triggered.connect(self.onActionStrategyMgrTriggered)  # 策略中心 --> 策略管理
        self.actionEditStrategy.triggered.connect(self.onActionEdittrategyTriggered)  # 策略中心 --> 新建策略 --> 编写策略
        self.actionPieceStrategy.triggered.connect(self.onActionPieceStrategyTriggered)  # 策略中心 --> 新建策略 --> 快速新建
        self.actionTransactionData.triggered.connect(self.onActionTransactionDataTriggered)  # 数据中心 --> 股票数据 --> 交易数据
        self.actionfuturesDate.triggered.connect(self.onActionFuturesDataTriggered)  # 数据中心 --> 期货数据

    def adaptAllSubWidgetToWindow(self):
        """将在所有的子窗口放入主界面中"""

        # 为所有的子窗口创建一个布局
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # 将所有子窗口都放入主窗口中
        for widget in self.__subWidgetList:
            sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
            widget.setSizePolicy(sizePolicy)
            widget.setObjectName("load_window")
            self.gridLayout_for_widget.addWidget(widget, 0, 0, 0, 0)

    def allSubWidgetHide(self):
        """ 隐藏所有的子窗口"""
        for widget in self.__subWidgetList:
            widget.hide()

    @QtCore.pyqtSlot()
    def onActionStrategyMgrTriggered(self):
        self.allSubWidgetHide()
        self.__strategyMgrWidget.show()

    @QtCore.pyqtSlot()
    def onActionEdittrategyTriggered(self):
        self.allSubWidgetHide()
        self.__newStrategyWidget.show()

    @QtCore.pyqtSlot()
    def onActionPieceStrategyTriggered(self):
        self.allSubWidgetHide()
        self.__quickNewStrategyWidget.show()

    @QtCore.pyqtSlot()
    def onActionTransactionDataTriggered(self):
        self.allSubWidgetHide()
        self.__stockDataWidget.show()

    @QtCore.pyqtSlot()
    def onActionFuturesDataTriggered(self):
        self.allSubWidgetHide()
        self.__futureDataWidget.show()


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
