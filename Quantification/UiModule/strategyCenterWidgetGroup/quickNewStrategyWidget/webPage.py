# coding=utf8
from PyQt4.QtWebKit import *
import webbrowser


class WebPage(QWebPage):
    """
    网页类，对Qt网页类QWebPage的继承
    """
    def __init__(self):
        super(WebPage, self).__init__()

    def acceptNavigationRequest(self, frame, request, type):
        """
        进行网页获取，对Qt网页类QWebPage的acceptNavigationRequest的重载
        :param frame: 网页框架
        :param request: 网页请求
        :param type: 网页类型
        :return: bool
        """

        # 如果连接请求类型正确
        if type == QWebPage.NavigationTypeLinkClicked:
            # 如果框架解析正确
            if frame == self.mainFrame():
                self.view().load(request.url())
            else:
                webbrowser.open(request.url().toString())
                return False
        return QWebPage.acceptNavigationRequest(self, frame, request, type)