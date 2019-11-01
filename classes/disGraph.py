# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disgraf.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DisGraf(object):
    def setupUi(self, DisGraf):
        DisGraf.setObjectName("DisGraf")
        DisGraf.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DisGraf)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 481, 61))
        self.label.setStyleSheet("font: 75 9pt \"Century Schoolbook L\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 640, 480))
        self.label_2.setMinimumSize(QtCore.QSize(640, 480))
        self.label_2.setMaximumSize(QtCore.QSize(640, 480))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(460, 20, 291, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 480, 61, 51))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(90, 170, 154);\n"
"}\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/bank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        DisGraf.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DisGraf)
        self.statusbar.setObjectName("statusbar")
        DisGraf.setStatusBar(self.statusbar)

        self.retranslateUi(DisGraf)
        QtCore.QMetaObject.connectSlotsByName(DisGraf)

    def retranslateUi(self, DisGraf):
        _translate = QtCore.QCoreApplication.translate
        DisGraf.setWindowTitle(_translate("DisGraf", "Dispatcherlik grafigi"))
        self.label.setText(_translate("DisGraf", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#55aa7f;\">Dispatcherlik grafigi</span></p></body></html>"))


