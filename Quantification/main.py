# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from UiModule.mainWindow import MainWindow


def main():
    # 设置软件全局编码格式为UTF-8，不然将会无法显示中文
    # codec = QTextCodec.codecForName("utf-8")
    # QTextCodec.setCodecForTr(codec)
    # QTextCodec.setCodecForLocale(QTextCodec.codecForLocale())
    # QTextCodec.setCodecForCStrings(QTextCodec.codecForLocale())

    # 创建界面应用
    app = QtWidgets.QApplication(sys.argv)

    # 显示UI
    window = MainWindow()
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
