# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mentor.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.outputBox = QTextEdit(self.centralwidget)
        self.outputBox.setObjectName(u"outputBox")
        self.outputBox.setGeometry(QRect(50, 50, 700, 200))
        self.inputBox = QLineEdit(self.centralwidget)
        self.inputBox.setObjectName(u"inputBox")
        self.inputBox.setGeometry(QRect(50, 270, 700, 40))
        self.submitBtn = QPushButton(self.centralwidget)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(350, 330, 100, 40))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        pass
    # retranslateUi

