# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loyqa_hajmi.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loyqa_hajmi(object):
    def setupUi(self, loyqa_hajmi):
        loyqa_hajmi.setObjectName("loyqa_hajmi")
        loyqa_hajmi.resize(800, 600)
        loyqa_hajmi.setMinimumSize(QtCore.QSize(800, 600))
        loyqa_hajmi.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(loyqa_hajmi)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 20, 361, 61))
        self.label.setStyleSheet("font: 57 9pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 90, 671, 131))
        self.lcdNumber.setDigitCount(15)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 450, 341, 101))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(255, 115, 87);\n"
"color:#fff;\n"
"font-size:30px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(190, 86, 65);\n"
"color:#fff;\n"
"font-size:27px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(560, 280, 81, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 340, 81, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 280, 421, 51))
        self.label_2.setStyleSheet("font: 57 9pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 340, 421, 51))
        self.label_3.setStyleSheet("font: 57 9pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(60, 220, 671, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 500, 41, 41))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(90, 170, 154);\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/bank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(550, 30, 181, 41))
        self.comboBox.setObjectName("comboBox")
        loyqa_hajmi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loyqa_hajmi)
        self.statusbar.setObjectName("statusbar")
        loyqa_hajmi.setStatusBar(self.statusbar)

        self.retranslateUi(loyqa_hajmi)
        QtCore.QMetaObject.connectSlotsByName(loyqa_hajmi)

    def retranslateUi(self, loyqa_hajmi):
        _translate = QtCore.QCoreApplication.translate
        loyqa_hajmi.setWindowTitle(_translate("loyqa_hajmi", "SOning loyqalangan hajmi "))
        self.label.setText(_translate("loyqa_hajmi", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">SOning loyqalangan hajmi!</span></p></body></html>"))
        self.pushButton.setText(_translate("loyqa_hajmi", "Xisoblash"))
        self.label_2.setText(_translate("loyqa_hajmi", "<html><head/><body><p><span style=\" font-size:18pt;\">SOning loyihaviy chiziq bo`yicha hajmi</span></p></body></html>"))
        self.label_3.setText(_translate("loyqa_hajmi", "<html><head/><body><p><span style=\" font-size:18pt;\">SOga quyilgan oqimning hajmi</span></p></body></html>"))


