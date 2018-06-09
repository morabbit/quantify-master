# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from newStrategyWidget_ui import Ui_newStrategyWidget


class NewStrategyWidget(QtGui.QWidget, Ui_newStrategyWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        # 设置字体
        font = QtGui.QFont("Courier", 11)
        font.setFixedPitch(True)
        self.textEdit.setFont(font)

        # 文本编辑器的信号和槽函数，发生编辑的时候，刷新界面
        self.textEdit.selectionChanged.connect(self.updateUi)
        self.textEdit.document().modificationChanged.connect(self.updateUi)

        # 当剪切板的数据改变的时候，刷新界面
        QtGui.QApplication.clipboard().dataChanged.connect(self.updateUi)

        # 按钮的信号与槽函数
        self.btnImportTemplate.clicked.connect(self.onBtnImportTemplateClicked)
        self.btnSaveStrategy.clicked.connect(self.onBtnSaveStrategyClicked)
        self.btnRewriteStrategy.clicked.connect(self.onBtnRewriteStrategyClicked)

        # 刷新界面
        self.updateUi()

    @QtCore.pyqtSlot()
    def updateUi(self, arg=None):
        """
        刷新界面
        :param arg:
        :return:
        """
        # 判断文件是否为空，如果非空，菜单栏选项为可用
        enable = not self.textEdit.document().isEmpty()
        self.btnSaveStrategy.setEnabled(enable)
        self.btnRewriteStrategy.setEnabled(enable)

        # 设置当前文件是否需要保存
        self.btnSaveStrategy.setEnabled(self.textEdit.document().isModified())

    @QtCore.pyqtSlot()
    def onBtnImportTemplateClicked(self):
        """插入模板"""

        #  创建一个文件打开对话框，获取用户需要的文件的路径与文件名
        filePathName = QtGui.QFileDialog.getOpenFileName(self, u'导入模板', './')

        # 如果获取的文件名为空，或者用户点击了取消，直接退出本方法
        if filePathName.isEmpty():
            return

        # 依据获取的文件名，打开文件
        file = open(filePathName)
        code = file.read()

        # 将文件流写入界面
        self.textEdit.setText(code)

    @QtCore.pyqtSlot()
    def onBtnSaveStrategyClicked(self):
        """保存"""

        # 打开一个文件保存对话框，获取用户希望保存的文件的路径与文件名
        filename = QtGui.QFileDialog.getSaveFileName(self, u"保存策略", '', "Python files (*.py *.pyw)")

        # 防御式编程
        try:
            # 依据用户指定的路径和文件名，创建一个Qt文件对象
            fh = QtCore.QFile(filename)

            # 尝试只读的方式打开文件，如果失败，抛出异常
            if not fh.open(QtCore.QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))

            # 将文件打开，放入输入流中
            stream = QtCore.QTextStream(fh)

            # 设置文件流的编码
            stream.setCodec("UTF-8")

            # 将界面上的文本放入文本流中（即保存）
            stream << self.textEdit.toPlainText()

            # 将文件属性设置为无修改
            self.textEdit.document().setModified(False)
        except EnvironmentError as e:

            # 异常警告
            QtGui.QMessageBox.warning(self, "Python Editor -- Save Error", "Failed to save {0}: {1}".format(filename, e))
            return False

    @QtCore.pyqtSlot()
    def onBtnRewriteStrategyClicked(self):
        """重写"""
        self.textEdit.clear()
        self.updateUi()


# 测试代码
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    window = NewStrategyWidget()
    window.show()

    sys.exit(app.exec_())