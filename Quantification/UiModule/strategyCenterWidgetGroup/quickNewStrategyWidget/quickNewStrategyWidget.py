# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebEngineWidgets import *
from UiModule.strategyCenterWidgetGroup.quickNewStrategyWidget.quickNewStrategyWidget_ui import Ui_quickNewStrategyWidget


class QuickNewStrategyWidget(QtWidgets.QWidget, Ui_quickNewStrategyWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.webView = QWebEngineView()

        # 初始化的url地址
        url = QtCore.QUrl("http://www.morabbit.com")
        self.webView.load(url)

        # 地址消息栏，里面输入回车按钮
        self.lineEditAddressBar.returnPressed.connect(self.search)
        self.lineEditAddressBar.returnPressed.connect(self.lineEditAddressBar.selectAll)

        # search按钮被点击按下的响应方法
        self.btnGoWeb.clicked.connect(self.search)
        self.btnGoWeb.clicked.connect(self.lineEditAddressBar.selectAll)

    # search按钮的响应方法
    @QtCore.pyqtSlot()
    def search(self):
        address = str(self.addressBar.text())

        # 获取的地址不如
        if address:
            if address.find('://') == -1:
                address = 'http://' + address
            url = QtCore.QUrl(address)
            self.webView.load(url)


# 测试代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = QuickNewStrategyWidget()
    window.show()

    sys.exit(app.exec_())
