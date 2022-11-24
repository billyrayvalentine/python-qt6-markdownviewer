# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'markdownviewer.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        self.action_About_Markdown_Viewer = QAction(MainWindow)
        self.action_About_Markdown_Viewer.setObjectName(u"action_About_Markdown_Viewer")
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        self.action_About_Qt = QAction(MainWindow)
        self.action_About_Qt.setObjectName(u"action_About_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About_Qt)
        self.menu_Help.addAction(self.action_About_Markdown_Viewer)

        self.retranslateUi(MainWindow)
        self.action_Quit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.action_About_Markdown_Viewer.setText(QCoreApplication.translate("MainWindow", u"&About Markdown Viewer", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        self.action_About_Qt.setText(QCoreApplication.translate("MainWindow", u"About &Qt", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

