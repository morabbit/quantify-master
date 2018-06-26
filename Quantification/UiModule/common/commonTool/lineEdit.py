# coding=utf8

from PyQt5 import QtCore, QtGui, QtWidgets


class LineEdit(QtWidgets.QLineEdit):
    LineEditClicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)

    def mouseReleaseEvent(self, event):
        """当鼠标点击文本编辑框的时候，发出信号"""
        self.LineEditClicked.emit()
