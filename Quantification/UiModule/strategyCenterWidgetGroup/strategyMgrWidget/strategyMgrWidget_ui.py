# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strategyMgrWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_strategyMgrWidget(object):
    def setupUi(self, strategyMgrWidget):
        strategyMgrWidget.setObjectName("strategyMgrWidget")
        strategyMgrWidget.resize(817, 569)
        self.verticalLayout = QtWidgets.QVBoxLayout(strategyMgrWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSearchMgr = QtWidgets.QLabel(strategyMgrWidget)
        self.labelSearchMgr.setObjectName("labelSearchMgr")
        self.horizontalLayout.addWidget(self.labelSearchMgr)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelStrategyName = QtWidgets.QLabel(strategyMgrWidget)
        self.labelStrategyName.setObjectName("labelStrategyName")
        self.gridLayout.addWidget(self.labelStrategyName, 0, 0, 1, 1)
        self.lineEditStrategyName = QtWidgets.QLineEdit(strategyMgrWidget)
        self.lineEditStrategyName.setObjectName("lineEditStrategyName")
        self.gridLayout.addWidget(self.lineEditStrategyName, 0, 1, 1, 1)
        self.labelCreateTime = QtWidgets.QLabel(strategyMgrWidget)
        self.labelCreateTime.setObjectName("labelCreateTime")
        self.gridLayout.addWidget(self.labelCreateTime, 0, 2, 1, 1)
        self.lineEditCreateTime = LineEdit(strategyMgrWidget)
        self.lineEditCreateTime.setObjectName("lineEditCreateTime")
        self.gridLayout.addWidget(self.lineEditCreateTime, 0, 3, 1, 2)
        self.labelStrategyType = QtWidgets.QLabel(strategyMgrWidget)
        self.labelStrategyType.setObjectName("labelStrategyType")
        self.gridLayout.addWidget(self.labelStrategyType, 1, 0, 1, 1)
        self.comboBoxStrategyType = QtWidgets.QComboBox(strategyMgrWidget)
        self.comboBoxStrategyType.setObjectName("comboBoxStrategyType")
        self.gridLayout.addWidget(self.comboBoxStrategyType, 1, 1, 1, 1)
        self.labelModifyTime = QtWidgets.QLabel(strategyMgrWidget)
        self.labelModifyTime.setObjectName("labelModifyTime")
        self.gridLayout.addWidget(self.labelModifyTime, 1, 2, 1, 1)
        self.lineEditModifyTime = LineEdit(strategyMgrWidget)
        self.lineEditModifyTime.setObjectName("lineEditModifyTime")
        self.gridLayout.addWidget(self.lineEditModifyTime, 1, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 4)
        self.btnSearch = QtWidgets.QPushButton(strategyMgrWidget)
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 2, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelStrategyMgr = QtWidgets.QLabel(strategyMgrWidget)
        self.labelStrategyMgr.setObjectName("labelStrategyMgr")
        self.horizontalLayout_2.addWidget(self.labelStrategyMgr)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidgetStrategy = QtWidgets.QTableWidget(strategyMgrWidget)
        self.tableWidgetStrategy.setObjectName("tableWidgetStrategy")
        self.tableWidgetStrategy.setColumnCount(5)
        self.tableWidgetStrategy.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetStrategy.setHorizontalHeaderItem(4, item)
        self.tableWidgetStrategy.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidgetStrategy)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelStrategyOperate = QtWidgets.QLabel(strategyMgrWidget)
        self.labelStrategyOperate.setObjectName("labelStrategyOperate")
        self.horizontalLayout_3.addWidget(self.labelStrategyOperate)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnModifyStrategy = QtWidgets.QPushButton(strategyMgrWidget)
        self.btnModifyStrategy.setObjectName("btnModifyStrategy")
        self.horizontalLayout_4.addWidget(self.btnModifyStrategy)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btnEditStrategy = QtWidgets.QPushButton(strategyMgrWidget)
        self.btnEditStrategy.setObjectName("btnEditStrategy")
        self.horizontalLayout_4.addWidget(self.btnEditStrategy)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.btnDeleteStrategy = QtWidgets.QPushButton(strategyMgrWidget)
        self.btnDeleteStrategy.setObjectName("btnDeleteStrategy")
        self.horizontalLayout_4.addWidget(self.btnDeleteStrategy)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(strategyMgrWidget)
        QtCore.QMetaObject.connectSlotsByName(strategyMgrWidget)

    def retranslateUi(self, strategyMgrWidget):
        _translate = QtCore.QCoreApplication.translate
        strategyMgrWidget.setWindowTitle(_translate("strategyMgrWidget", "策略管理"))
        self.labelSearchMgr.setText(_translate("strategyMgrWidget", "查询管理："))
        self.labelStrategyName.setText(_translate("strategyMgrWidget", "名称："))
        self.labelCreateTime.setText(_translate("strategyMgrWidget", "创建时间："))
        self.labelStrategyType.setText(_translate("strategyMgrWidget", "从属分类："))
        self.labelModifyTime.setText(_translate("strategyMgrWidget", "修改时间："))
        self.btnSearch.setText(_translate("strategyMgrWidget", "查询"))
        self.labelStrategyMgr.setText(_translate("strategyMgrWidget", "策略管理："))
        item = self.tableWidgetStrategy.horizontalHeaderItem(0)
        item.setText(_translate("strategyMgrWidget", "名称"))
        item = self.tableWidgetStrategy.horizontalHeaderItem(1)
        item.setText(_translate("strategyMgrWidget", "创建时间"))
        item = self.tableWidgetStrategy.horizontalHeaderItem(2)
        item.setText(_translate("strategyMgrWidget", "修改时间"))
        item = self.tableWidgetStrategy.horizontalHeaderItem(3)
        item.setText(_translate("strategyMgrWidget", "从属分类"))
        item = self.tableWidgetStrategy.horizontalHeaderItem(4)
        item.setText(_translate("strategyMgrWidget", "描述"))
        self.labelStrategyOperate.setText(_translate("strategyMgrWidget", "操作策略："))
        self.btnModifyStrategy.setText(_translate("strategyMgrWidget", "修改策略"))
        self.btnEditStrategy.setText(_translate("strategyMgrWidget", "编辑策略"))
        self.btnDeleteStrategy.setText(_translate("strategyMgrWidget", "删除策略"))

from UiModule.common.commonTool.lineEdit import LineEdit
