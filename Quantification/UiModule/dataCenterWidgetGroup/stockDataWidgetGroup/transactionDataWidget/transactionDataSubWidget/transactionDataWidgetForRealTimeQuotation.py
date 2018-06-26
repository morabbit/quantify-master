# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataSubWidget.transactionDataWidgetForRehabilitationData import \
    TransactionDataWidgetForRehabilitationData


class TransactionDataWidgetForRealTimeQuotation(TransactionDataWidgetForRehabilitationData):
    """实时行情tab"""

    def __init__(self, parent=None):
        # print "StockDataWidgetForHistoricalTick: init"
        super(TransactionDataWidgetForRealTimeQuotation, self).__init__()

        # 创建本类管理的tab下的查询的参数
        self.__searchRefForRealTimeQuotation = {}

        # 保存路径
        self.btnSavePathForRealTimeQuotation.clicked.connect(self.onBtnSavePathForRealTimeQuotationClicked)

    @QtCore.pyqtSlot()
    def onBtnSavePathForRealTimeQuotationClicked(self):
        """获取用户想要保存的数据路径"""

        # 打开对话框，获取需要保存的路径
        path = QtWidgets.QFileDialog.getExistingDirectory(self, u"数据保存路径", QtCore.QDir.currentPath())

        # 如果获取失败，退出函数
        if path is None:
            return

        # 将路径显示到界面上
        self.lineEditSavePathForRealTimeQuotation.setText(path)

    def getRefSavePathForRealTimeQuotation(self):
        """获取文件保存路径"""

        # 容错
        if 0 == len(self.lineEditSavePathForRealTimeQuotation.text()):
            QtWidgets.QMessageBox.warning(self, u"错误！", u"请设置保存路径", QtWidgets.QMessageBox.Cancel)
            return None

        return str(self.lineEditSavePathForRealTimeQuotation.text())

    def getRefDictForRealTimeQuotation(self):
        """获取历史行情参数字典"""

        # 获取文件保存路径
        self.__searchRefForRealTimeQuotation["path"] = self.getRefSavePathForRealTimeQuotation()

        # 回返一个参数字典
        return self.__searchRefForRealTimeQuotation
