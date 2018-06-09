# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickNewStrategyWidget_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_quickNewStrategyWidget(object):
    def setupUi(self, quickNewStrategyWidget):
        quickNewStrategyWidget.setObjectName(_fromUtf8("quickNewStrategyWidget"))
        quickNewStrategyWidget.resize(797, 558)
        self.verticalLayout = QtGui.QVBoxLayout(quickNewStrategyWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditAddressBar = QtGui.QLineEdit(quickNewStrategyWidget)
        self.lineEditAddressBar.setObjectName(_fromUtf8("lineEditAddressBar"))
        self.horizontalLayout.addWidget(self.lineEditAddressBar)
        self.btnGoWeb = QtGui.QPushButton(quickNewStrategyWidget)
        self.btnGoWeb.setObjectName(_fromUtf8("btnGoWeb"))
        self.horizontalLayout.addWidget(self.btnGoWeb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(quickNewStrategyWidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(quickNewStrategyWidget)
        QtCore.QMetaObject.connectSlotsByName(quickNewStrategyWidget)

    def retranslateUi(self, quickNewStrategyWidget):
        quickNewStrategyWidget.setWindowTitle(_translate("quickNewStrategyWidget", "快速新建策略", None))
        self.btnGoWeb.setText(_translate("quickNewStrategyWidget", "前往", None))

from PyQt4 import QtWebKit
