import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QTextDocument
from PySide6.QtCore import QFile, QUrl
from ui_markdownviewer import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_About_Markdown_Viewer.triggered.connect(self.showinfo)
        self.ui.action_Open.triggered.connect(self.openfile)

    # Slots
    def showinfo(self):
        """Show the about application dialog"""
        QMessageBox.information(
            self,
            "About MKV (MarkDown Viewer)",
            "MKV (MarkDown Viewer) \n\
            Copyright © 2022 Ben Sampson (http://github.com/billyrayvalentine)\n\
            This work is free. You can redistribute it and/or modify it under the\n\
            terms of the Do What The Fuck You Want To Public License, Version 2,\n\
            as published by Sam Hocevar.\n\
            See http://www.wtfpl.net/ for more details.",
        )

    def openfile(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", os.getcwd())

        if filename[0]:
            print(f"Opening {filename[0]}")

        url = QUrl.fromLocalFile(filename[0])

        if url.isValid():
            print(f"Using {url}")
            self.showfile(url)

    def showfile(self, url: QUrl):
        self.ui.textBrowser.setOpenExternalLinks(True)
        self.ui.textBrowser.setDocumentTitle(url.fileName())
        self.setWindowTitle(url.fileName())
        self.ui.textBrowser.setSource(url, QTextDocument.MarkdownResource)

        # print(f"Read only = {self.ui.textBrowser.isReadOnly()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
