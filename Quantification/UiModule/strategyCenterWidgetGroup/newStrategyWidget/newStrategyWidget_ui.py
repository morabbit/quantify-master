# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newStrategyWidget_ui.ui'
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

class Ui_newStrategyWidget(object):
    def setupUi(self, newStrategyWidget):
        newStrategyWidget.setObjectName(_fromUtf8("newStrategyWidget"))
        newStrategyWidget.resize(711, 480)
        self.verticalLayout = QtGui.QVBoxLayout(newStrategyWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = TextEdit(newStrategyWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnImportTemplate = QtGui.QPushButton(newStrategyWidget)
        self.btnImportTemplate.setObjectName(_fromUtf8("btnImportTemplate"))
        self.horizontalLayout.addWidget(self.btnImportTemplate)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSaveStrategy = QtGui.QPushButton(newStrategyWidget)
        self.btnSaveStrategy.setObjectName(_fromUtf8("btnSaveStrategy"))
        self.horizontalLayout.addWidget(self.btnSaveStrategy)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnRewriteStrategy = QtGui.QPushButton(newStrategyWidget)
        self.btnRewriteStrategy.setObjectName(_fromUtf8("btnRewriteStrategy"))
        self.horizontalLayout.addWidget(self.btnRewriteStrategy)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(newStrategyWidget)
        QtCore.QMetaObject.connectSlotsByName(newStrategyWidget)

    def retranslateUi(self, newStrategyWidget):
        newStrategyWidget.setWindowTitle(_translate("newStrategyWidget", "新建策略", None))
        self.btnImportTemplate.setText(_translate("newStrategyWidget", "导入模板", None))
        self.btnSaveStrategy.setText(_translate("newStrategyWidget", "保存", None))
        self.btnRewriteStrategy.setText(_translate("newStrategyWidget", "重写", None))

from UiModule.common.commonTool.notepad import TextEdit
