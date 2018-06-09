# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strategyMgrWidget_ui.ui'
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

class Ui_strategyMgrWidget(object):
    def setupUi(self, strategyMgrWidget):
        strategyMgrWidget.setObjectName(_fromUtf8("strategyMgrWidget"))
        strategyMgrWidget.resize(817, 569)
        self.verticalLayout = QtGui.QVBoxLayout(strategyMgrWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelSearchMgr = QtGui.QLabel(strategyMgrWidget)
        self.labelSearchMgr.setObjectName(_fromUtf8("labelSearchMgr"))
        self.horizontalLayout.addWidget(self.labelSearchMgr)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelStrategyName = QtGui.QLabel(strategyMgrWidget)
        self.labelStrategyName.setObjectName(_fromUtf8("labelStrategyName"))
        self.gridLayout.addWidget(self.labelStrategyName, 0, 0, 1, 1)
        self.lineEditStrategyName = QtGui.QLineEdit(strategyMgrWidget)
        self.lineEditStrategyName.setObjectName(_fromUtf8("lineEditStrategyName"))
        self.gridLayout.addWidget(self.lineEditStrategyName, 0, 1, 1, 1)
        self.labelCreateTime = QtGui.QLabel(strategyMgrWidget)
        self.labelCreateTime.setObjectName(_fromUtf8("labelCreateTime"))
        self.gridLayout.addWidget(self.labelCreateTime, 0, 2, 1, 1)
        self.lineEditCreateTime = LineEdit(strategyMgrWidget)
        self.lineEditCreateTime.setObjectName(_fromUtf8("lineEditCreateTime"))
        self.gridLayout.addWidget(self.lineEditCreateTime, 0, 3, 1, 2)
        self.labelStrategyType = QtGui.QLabel(strategyMgrWidget)
        self.labelStrategyType.setObjectName(_fromUtf8("labelStrategyType"))
        self.gridLayout.addWidget(self.labelStrategyType, 1, 0, 1, 1)
        self.comboBoxStrategyType = QtGui.QComboBox(strategyMgrWidget)
        self.comboBoxStrategyType.setObjectName(_fromUtf8("comboBoxStrategyType"))
        self.gridLayout.addWidget(self.comboBoxStrategyType, 1, 1, 1, 1)
        self.labelModifyTime = QtGui.QLabel(strategyMgrWidget)
        self.labelModifyTime.setObjectName(_fromUtf8("labelModifyTime"))
        self.gridLayout.addWidget(self.labelModifyTime, 1, 2, 1, 1)
        self.lineEditModifyTime = LineEdit(strategyMgrWidget)
        self.lineEditModifyTime.setObjectName(_fromUtf8("lineEditModifyTime"))
        self.gridLayout.addWidget(self.lineEditModifyTime, 1, 3, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(298, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 4)
        self.btnSearch = QtGui.QPushButton(strategyMgrWidget)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.gridLayout.addWidget(self.btnSearch, 2, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelStrategyMgr = QtGui.QLabel(strategyMgrWidget)
        self.labelStrategyMgr.setObjectName(_fromUtf8("labelStrategyMgr"))
        self.horizontalLayout_2.addWidget(self.labelStrategyMgr)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidgetStrategy = QtGui.QTableWidget(strategyMgrWidget)
        self.tableWidgetStrategy.setObjectName(_fromUtf8("tableWidgetStrategy"))
        self.tableWidgetStrategy.setColumnCount(5)
        self.tableWidgetStrategy.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(4, item)
        self.tableWidgetStrategy.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidgetStrategy)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelStrategyOperate = QtGui.QLabel(strategyMgrWidget)
        self.labelStrategyOperate.setObjectName(_fromUtf8("labelStrategyOperate"))
        self.horizontalLayout_3.addWidget(self.labelStrategyOperate)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnModifyStrategy = QtGui.QPushButton(strategyMgrWidget)
        self.btnModifyStrategy.setObjectName(_fromUtf8("btnModifyStrategy"))
        self.horizontalLayout_4.addWidget(self.btnModifyStrategy)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btnEditStrategy = QtGui.QPushButton(strategyMgrWidget)
        self.btnEditStrategy.setObjectName(_fromUtf8("btnEditStrategy"))
        self.horizontalLayout_4.addWidget(self.btnEditStrategy)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.btnDeleteStrategy = QtGui.QPushButton(strategyMgrWidget)
        self.btnDeleteStrategy.setObjectName(_fromUtf8("btnDeleteStrategy"))
        self.horizontalLayout_4.addWidget(self.btnDeleteStrategy)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(strategyMgrWidget)
        QtCore.QMetaObject.connectSlotsByName(strategyMgrWidget)

    def retranslateUi(self, strategyMgrWidget):
        strategyMgrWidget.setWindowTitle(_translate("strategyMgrWidget", "策略管理", None))
        self.labelSearchMgr.setText(_translate("strategyMgrWidget", "查询管理：", None))
        self.labelStrategyName.setText(_translate("strategyMgrWidget", "名称：", None))
        self.labelCreateTime.setText(_translate("strategyMgrWidget", "创建时间：", None))
        self.labelStrategyType.setText(_translate("strategyMgrWidget", "从属分类：", None))
        self.labelModifyTime.setText(_translate("strategyMgrWidget", "修改时间：", None))
        self.btnSearch.setText(_translate("strategyMgrWidget", "查询", None))
        self.labelStrategyMgr.setText(_translate("strategyMgrWidget", "策略管理：", None))
        item = self.tableWidgetStrategy.horizontalHeaderItem(0)
        item.setText(_translate("strategyMgrWidget", "名称", None))
        item = self.tableWidgetStrategy.horizontalHeaderItem(1)
        item.setText(_translate("strategyMgrWidget", "创建时间", None))
        item = self.tableWidgetStrategy.horizontalHeaderItem(2)
        item.setText(_translate("strategyMgrWidget", "修改时间", None))
        item = self.tableWidgetStrategy.horizontalHeaderItem(3)
        item.setText(_translate("strategyMgrWidget", "从属分类", None))
        item = self.tableWidgetStrategy.horizontalHeaderItem(4)
        item.setText(_translate("strategyMgrWidget", "描述", None))
        self.labelStrategyOperate.setText(_translate("strategyMgrWidget", "操作策略：", None))
        self.btnModifyStrategy.setText(_translate("strategyMgrWidget", "修改策略", None))
        self.btnEditStrategy.setText(_translate("strategyMgrWidget", "编辑策略", None))
        self.btnDeleteStrategy.setText(_translate("strategyMgrWidget", "删除策略", None))

from UiModule.common.commonTool.lineEdit import LineEdit
