# -*- coding: utf-8 -*-

from PyQt5 import  QtWidgets
from UiModule.dataCenterWidgetGroup.stockDataWidgetGroup.transactionDataWidget.transactionDataWidget_ui import Ui_transactionDataWidget

# 历史行情数据的查询数据类型列表
ktypeList = ["D", "W", "M", "5", "15", "30", "60"]


class TransactionDataWidgetBase(QtWidgets.QWidget, Ui_transactionDataWidget):
    '''股票数据界面的逻辑接口基类'''

    def __init__(self, parent=None):
        # 先实例化界面，穿件基类对象
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
