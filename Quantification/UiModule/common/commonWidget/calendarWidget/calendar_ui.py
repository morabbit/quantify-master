# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_ui.ui'
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

class Ui_calendarWidget(object):
    def setupUi(self, calendarWidget):
        calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        calendarWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(calendarWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.calendar = QtGui.QCalendarWidget(calendarWidget)
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.verticalLayout.addWidget(self.calendar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelData = QtGui.QLabel(calendarWidget)
        self.labelData.setText(_fromUtf8(""))
        self.labelData.setObjectName(_fromUtf8("labelData"))
        self.horizontalLayout.addWidget(self.labelData)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnOK = QtGui.QPushButton(calendarWidget)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.horizontalLayout.addWidget(self.btnOK)
        self.btnCancel = QtGui.QPushButton(calendarWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(calendarWidget)
        QtCore.QMetaObject.connectSlotsByName(calendarWidget)

    def retranslateUi(self, calendarWidget):
        calendarWidget.setWindowTitle(_translate("calendarWidget", "日期", None))
        self.btnOK.setText(_translate("calendarWidget", "确定", None))
        self.btnCancel.setText(_translate("calendarWidget", "取消", None))

