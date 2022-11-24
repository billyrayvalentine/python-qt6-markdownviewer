import sys
import os
import argparse
import signal
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QTextDocument
from PySide6.QtCore import QFile, QUrl
from ui_markdownviewer import Ui_MainWindow


class MarkDownViewer(QMainWindow, Ui_MainWindow):
    def __init__(self, file: QUrl = None, log_level: str = "WARNING"):
        super().__init__()
        self.setupUi(self)

        self.action_About_Markdown_Viewer.triggered.connect(self.showinfo)
        self.action_Open.triggered.connect(self.openfile)
        self.action_About_Qt.triggered.connect(app.aboutQt)

        # Setup logging
        logging.basicConfig(
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y/%m/%d %H:%M:%S",
            level=log_level,
        )

        self.show()

        # Launch with a file if file is not None
        if file:
            logging.info(f"Starting with file: {file}")
            self.showfile(file)

    # Slots
    def showinfo(self):
        """Show the about application dialog"""
        QMessageBox.about(
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
            logging.info(f"Opening {filename[0]}")

        url = QUrl.fromLocalFile(filename[0])

        if url.isValid():
            logging.info(f"Using {url}")
            self.showfile(url)

    def showfile(self, url: QUrl):
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setDocumentTitle(url.fileName())
        self.setWindowTitle(url.fileName())
        self.textBrowser.setSource(url, QTextDocument.MarkdownResource)

        logging.debug(f"Read only = {self.textBrowser.isReadOnly()}")


if __name__ == "__main__":

    # Catch CTL+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    parser = argparse.ArgumentParser(description="MKV - MarkDownViewer")
    parser.add_argument(
        "filename", metavar="file", type=str, nargs="?", help="file to open"
    )
    parser.add_argument(
        "-d",
        "--debug",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        help="debug level",
        default="WARNING",
    )
    args = parser.parse_args()

    if args.filename:
        filename_qurl = QUrl.fromLocalFile(args.filename)
        if not filename_qurl.isValid():
            sys.stderr.write(f"Invalid filename {args.filename}")
            sys.exit(1)
    else:
        filename_qurl = None

    app = QApplication(sys.argv)
    window = MarkDownViewer(filename_qurl, args.debug)
    app.exec()
