# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newStrategyWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newStrategyWidget(object):
    def setupUi(self, newStrategyWidget):
        newStrategyWidget.setObjectName("newStrategyWidget")
        newStrategyWidget.resize(711, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(newStrategyWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = TextEdit(newStrategyWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnImportTemplate = QtWidgets.QPushButton(newStrategyWidget)
        self.btnImportTemplate.setObjectName("btnImportTemplate")
        self.horizontalLayout.addWidget(self.btnImportTemplate)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSaveStrategy = QtWidgets.QPushButton(newStrategyWidget)
        self.btnSaveStrategy.setObjectName("btnSaveStrategy")
        self.horizontalLayout.addWidget(self.btnSaveStrategy)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnRewriteStrategy = QtWidgets.QPushButton(newStrategyWidget)
        self.btnRewriteStrategy.setObjectName("btnRewriteStrategy")
        self.horizontalLayout.addWidget(self.btnRewriteStrategy)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(newStrategyWidget)
        QtCore.QMetaObject.connectSlotsByName(newStrategyWidget)

    def retranslateUi(self, newStrategyWidget):
        _translate = QtCore.QCoreApplication.translate
        newStrategyWidget.setWindowTitle(_translate("newStrategyWidget", "新建策略"))
        self.btnImportTemplate.setText(_translate("newStrategyWidget", "导入模板"))
        self.btnSaveStrategy.setText(_translate("newStrategyWidget", "保存"))
        self.btnRewriteStrategy.setText(_translate("newStrategyWidget", "重写"))

from UiModule.common.commonTool.notepad import TextEdit
