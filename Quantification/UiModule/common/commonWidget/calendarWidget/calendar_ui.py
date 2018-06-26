# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_ui.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_calendarWidget(object):
    def setupUi(self, calendarWidget):
        calendarWidget.setObjectName("calendarWidget")
        calendarWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(calendarWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendar = QtWidgets.QCalendarWidget(calendarWidget)
        self.calendar.setObjectName("calendar")
        self.verticalLayout.addWidget(self.calendar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelData = QtWidgets.QLabel(calendarWidget)
        self.labelData.setText("")
        self.labelData.setObjectName("labelData")
        self.horizontalLayout.addWidget(self.labelData)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnOK = QtWidgets.QPushButton(calendarWidget)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(calendarWidget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(calendarWidget)
        QtCore.QMetaObject.connectSlotsByName(calendarWidget)

    def retranslateUi(self, calendarWidget):
        _translate = QtCore.QCoreApplication.translate
        calendarWidget.setWindowTitle(_translate("calendarWidget", "日期"))
        self.btnOK.setText(_translate("calendarWidget", "确定"))
        self.btnCancel.setText(_translate("calendarWidget", "取消"))

