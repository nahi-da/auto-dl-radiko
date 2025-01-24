# -*- coding: utf-8 -*-

import sys
import os
import re
from const import *
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton,  QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage

__program__ = 'PERSEPHONE'

class CustomWebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def javaScriptConsoleMessage(self, level, message, line_number, source_id):
        print(f"Console: {message} (Line: {line_number})")

    def featurePermissionRequested(self, securityOrigin, feature):
        # 位置情報アクセスのリクエストを許可する
        if feature == QWebEnginePage.Feature.Geolocation:
            self.setFeaturePermission(securityOrigin, feature, QWebEnginePage.PermissionPolicy.PermissionGrantedByUser)



class PersephoneWindow(QWidget):
    def __init__(self, ido=None, keido=None):
        super().__init__()
        self.return_text = str()
        self.initUI()
        self.ido = ido
        self.keido = keido

    def initUI(self):

        initurl = 'https://radiko.jp/#!/timeshift'

        # setting browser
        self.browser = QWebEngineView()
        self.page = CustomWebPage(self)
        self.browser.setPage(self.page)
        # ページロード完了後にJavaScriptを挿入して位置情報を偽装
        self.browser.page().loadFinished.connect(self.inject_geolocation_script)
        self.browser.load(QUrl(initurl))
        self.browser.resize(1000, 600)
        self.browser.move(200, 200)
        self.browser.setWindowTitle(__program__)

        # setting button
        self.back_button = QPushButton('back')
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button = QPushButton('forward')
        self.forward_button.clicked.connect(self.browser.forward)
        self.reload_button = QPushButton('reload')
        self.reload_button.clicked.connect(self.browser.reload)
        self.url_edit = QLineEdit()
        self.move_button = QPushButton('move')
        self.move_button.clicked.connect(self.loadPage)

        # signal catch from moving web pages.
        self.browser.urlChanged.connect(self.updateCurrentUrl)

        # setting layout
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.back_button, 1, 0)
        grid.addWidget(self.forward_button, 1, 1)
        grid.addWidget(self.reload_button, 1, 2)
        grid.addWidget(self.url_edit, 1, 3, 1, 10)
        grid.addWidget(self.move_button, 1, 14)
        grid.addWidget(self.browser, 2, 0, 5, 15)
        self.setLayout(grid)
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle(__program__)
        self.show()

    def center(self):
        ''' centering widget
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadPage(self):
        ''' move web page which is set at url_edit
        '''
        move_url = QUrl(self.url_edit.text())
        self.browser.load(move_url)
        self.updateCurrentUrl

    def updateCurrentUrl(self):
        ''' rewriting url_edit when you move different web page.
        '''
        current_url = self.browser.url().toString()
        self.url_edit.clear()
        self.url_edit.insert(current_url)
        if re.match(r'https:\/\/radiko.jp\/#!\/ts\/(.*)', current_url):
            self.return_text = current_url
            super().close()

    def inject_geolocation_script(self):
        # JavaScriptで位置情報を偽装
        fake_location_js = """
        navigator.geolocation.getCurrentPosition = function(success, error) {
            success({
                coords: {
                    latitude: __IDO__,  // 偽の緯度
                    longitude: __KEIDO__ // 偽の経度
                }
            });
        };
        """.replace("__IDO__", str(self.ido) if self.ido is not None else "35.689488").replace("__KEIDO__", str(self.keido) if self.keido is not None else "139.691706")
        self.browser.page().runJavaScript(fake_location_js)


def main(ido=None, keido=None):
    # mainPyQt5()
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(
        sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    ex = PersephoneWindow(ido, keido)
    app.exec_()

    return ex.return_text


if __name__ == '__main__':
    main()
