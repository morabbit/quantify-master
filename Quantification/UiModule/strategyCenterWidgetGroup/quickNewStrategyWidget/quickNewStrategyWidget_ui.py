# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickNewStrategyWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_quickNewStrategyWidget(object):
    def setupUi(self, quickNewStrategyWidget):
        quickNewStrategyWidget.setObjectName("quickNewStrategyWidget")
        quickNewStrategyWidget.resize(797, 558)
        self.verticalLayout = QtWidgets.QVBoxLayout(quickNewStrategyWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditAddressBar = QtWidgets.QLineEdit(quickNewStrategyWidget)
        self.lineEditAddressBar.setObjectName("lineEditAddressBar")
        self.horizontalLayout.addWidget(self.lineEditAddressBar)
        self.btnGoWeb = QtWidgets.QPushButton(quickNewStrategyWidget)
        self.btnGoWeb.setObjectName("btnGoWeb")
        self.horizontalLayout.addWidget(self.btnGoWeb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebEngineWidgets.QWebEngineView(quickNewStrategyWidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(quickNewStrategyWidget)
        QtCore.QMetaObject.connectSlotsByName(quickNewStrategyWidget)

    def retranslateUi(self, quickNewStrategyWidget):
        _translate = QtCore.QCoreApplication.translate
        quickNewStrategyWidget.setWindowTitle(_translate("quickNewStrategyWidget", "快速新建策略"))
        self.btnGoWeb.setText(_translate("quickNewStrategyWidget", "前往"))

# from PyQt5 import QtWebKitWidgets
from PyQt5 import QtWebEngineWidgets