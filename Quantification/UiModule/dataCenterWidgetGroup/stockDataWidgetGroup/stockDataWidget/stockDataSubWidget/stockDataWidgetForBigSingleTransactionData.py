# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.stockDataWidget.stockDataWidget_ui import Ui_stockDataWidget


class StockDataWidgetForBigSingleTransactionData(QtGui.QWidget, Ui_stockDataWidget):
    def __init__(self, parent=None):
        # QtGui.QWidget.__init__(self, parent)
        # self.setupUi(self)
        pass


# 测试代码
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    window = StockDataWidgetForBigSingleTransactionData()
    window.show()

    sys.exit(app.exec_())
