# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\S11De\Desktop\SqrtPythonProject\formBaseUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 381)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(230000, 230000))
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.answerButton = QtWidgets.QPushButton(self.centralwidget)
        self.answerButton.setGeometry(QtCore.QRect(10, 110, 211, 28))
        self.answerButton.setObjectName("answerButton")
        self.askTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.askTextBrowser.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.askTextBrowser.setReadOnly(False)
        self.askTextBrowser.setObjectName("askTextBrowser")
        self.answerTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.answerTextBrowser.setGeometry(QtCore.QRect(10, 60, 211, 41))
        self.answerTextBrowser.setDocumentTitle("")
        self.answerTextBrowser.setPlaceholderText("")
        self.answerTextBrowser.setObjectName("answerTextBrowser")
        self.rounderSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rounderSpinBox.setGeometry(QtCore.QRect(230, 110, 42, 22))
        self.rounderSpinBox.setMinimum(1)
        self.rounderSpinBox.setMaximum(20)
        self.rounderSpinBox.setObjectName("rounderSpinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sqrt"))
        self.answerButton.setText(_translate("MainWindow", "Push to take sqr"))

