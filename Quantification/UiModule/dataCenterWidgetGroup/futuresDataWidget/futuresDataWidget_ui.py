# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'futuresDataWidget_ui.ui'
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

class Ui_futureDataWidget(object):
    def setupUi(self, futureDataWidget):
        futureDataWidget.setObjectName(_fromUtf8("futureDataWidget"))
        futureDataWidget.resize(779, 500)
        self.verticalLayout = QtGui.QVBoxLayout(futureDataWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labDataSource = QtGui.QLabel(futureDataWidget)
        self.labDataSource.setObjectName(_fromUtf8("labDataSource"))
        self.gridLayout.addWidget(self.labDataSource, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chkBoxSH = QtGui.QCheckBox(futureDataWidget)
        self.chkBoxSH.setObjectName(_fromUtf8("chkBoxSH"))
        self.horizontalLayout_2.addWidget(self.chkBoxSH)
        self.chkBoxSZ = QtGui.QCheckBox(futureDataWidget)
        self.chkBoxSZ.setObjectName(_fromUtf8("chkBoxSZ"))
        self.horizontalLayout_2.addWidget(self.chkBoxSZ)
        self.chkBoxHS300 = QtGui.QCheckBox(futureDataWidget)
        self.chkBoxHS300.setObjectName(_fromUtf8("chkBoxHS300"))
        self.horizontalLayout_2.addWidget(self.chkBoxHS300)
        self.chkBoxSZ50 = QtGui.QCheckBox(futureDataWidget)
        self.chkBoxSZ50.setObjectName(_fromUtf8("chkBoxSZ50"))
        self.horizontalLayout_2.addWidget(self.chkBoxSZ50)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.labStartTime = QtGui.QLabel(futureDataWidget)
        self.labStartTime.setObjectName(_fromUtf8("labStartTime"))
        self.gridLayout.addWidget(self.labStartTime, 1, 0, 1, 1)
        self.lineEditStartTime = LineEdit(futureDataWidget)
        self.lineEditStartTime.setObjectName(_fromUtf8("lineEditStartTime"))
        self.gridLayout.addWidget(self.lineEditStartTime, 1, 1, 1, 1)
        self.labEndTime = QtGui.QLabel(futureDataWidget)
        self.labEndTime.setObjectName(_fromUtf8("labEndTime"))
        self.gridLayout.addWidget(self.labEndTime, 2, 0, 1, 1)
        self.lineEditEndTime = LineEdit(futureDataWidget)
        self.lineEditEndTime.setObjectName(_fromUtf8("lineEditEndTime"))
        self.gridLayout.addWidget(self.lineEditEndTime, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 370, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnSaveToCSV = QtGui.QPushButton(futureDataWidget)
        self.btnSaveToCSV.setObjectName(_fromUtf8("btnSaveToCSV"))
        self.horizontalLayout.addWidget(self.btnSaveToCSV)
        self.btnSaveToExcel = QtGui.QPushButton(futureDataWidget)
        self.btnSaveToExcel.setObjectName(_fromUtf8("btnSaveToExcel"))
        self.horizontalLayout.addWidget(self.btnSaveToExcel)
        self.btnSaveToHDF5 = QtGui.QPushButton(futureDataWidget)
        self.btnSaveToHDF5.setObjectName(_fromUtf8("btnSaveToHDF5"))
        self.horizontalLayout.addWidget(self.btnSaveToHDF5)
        self.btnSaveToJSON = QtGui.QPushButton(futureDataWidget)
        self.btnSaveToJSON.setObjectName(_fromUtf8("btnSaveToJSON"))
        self.horizontalLayout.addWidget(self.btnSaveToJSON)
        self.btnSaveToMySQL = QtGui.QPushButton(futureDataWidget)
        self.btnSaveToMySQL.setObjectName(_fromUtf8("btnSaveToMySQL"))
        self.horizontalLayout.addWidget(self.btnSaveToMySQL)
        self.btnSaveToMongoDB = QtGui.QPushButton(futureDataWidget)
        self.btnSaveToMongoDB.setObjectName(_fromUtf8("btnSaveToMongoDB"))
        self.horizontalLayout.addWidget(self.btnSaveToMongoDB)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(futureDataWidget)
        QtCore.QMetaObject.connectSlotsByName(futureDataWidget)

    def retranslateUi(self, futureDataWidget):
        futureDataWidget.setWindowTitle(_translate("futureDataWidget", "期货数据", None))
        self.labDataSource.setText(_translate("futureDataWidget", "数据源：", None))
        self.chkBoxSH.setText(_translate("futureDataWidget", "中金所", None))
        self.chkBoxSZ.setText(_translate("futureDataWidget", "郑商所", None))
        self.chkBoxHS300.setText(_translate("futureDataWidget", "上期所", None))
        self.chkBoxSZ50.setText(_translate("futureDataWidget", "大商所", None))
        self.labStartTime.setText(_translate("futureDataWidget", "开始时间：", None))
        self.labEndTime.setText(_translate("futureDataWidget", "结束时间：", None))
        self.btnSaveToCSV.setText(_translate("futureDataWidget", "保存为CSV", None))
        self.btnSaveToExcel.setText(_translate("futureDataWidget", "保存为Excel", None))
        self.btnSaveToHDF5.setText(_translate("futureDataWidget", "保存为HDF5", None))
        self.btnSaveToJSON.setText(_translate("futureDataWidget", "保存为JSON", None))
        self.btnSaveToMySQL.setText(_translate("futureDataWidget", "保存至MySQL", None))
        self.btnSaveToMongoDB.setText(_translate("futureDataWidget", "保存至MongoDB", None))

from UiModule.common.commonTool.lineEdit import LineEdit
