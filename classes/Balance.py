from PyQt5 import QtCore, QtGui, QtWidgets

#Water balance
class waterbalans(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"border-radius:0px;\n"
"background-color:#fff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 80, 421, 41))
        self.label.setStyleSheet("font: 57 9pt \"aakar\";")
        self.label.setObjectName("label")
        self.pushbtn_kiruvchi = QtWidgets.QPushButton(self.frame)
        self.pushbtn_kiruvchi.setGeometry(QtCore.QRect(30, 190, 361, 111))
        self.pushbtn_kiruvchi.setStyleSheet("QPushButton \n"
"{\n"
"font-size:16px;\n"
"border-radius:50px;\n"
"background-color: rgb(60, 120, 180);\n"
"font-family: \"Georgia\";\n"
"font-weight:bold;\n"
"color:#fff;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font-size:14px;\n"
"border-radius:50px;\n"
"background-color: rgb(66, 132, 198);\n"
"font-family: \"Georgia\";\n"
"font-weight:bold;\n"
"color:#fff;\n"
"}")
        self.pushbtn_kiruvchi.setObjectName("pushbtn_kiruvchi")
        self.pushbtn_chiquvchi = QtWidgets.QPushButton(self.frame)
        self.pushbtn_chiquvchi.setGeometry(QtCore.QRect(410, 190, 351, 111))
        self.pushbtn_chiquvchi.setStyleSheet("QPushButton \n"
"{\n"
"font-size:16px;\n"
"border-radius:50px;\n"
"background-color: rgb(60, 120, 180);\n"
"font-family: \"Georgia\";\n"
"font-weight:bold;\n"
"color:#fff;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font-size:14px;\n"
"border-radius:50px;\n"
"background-color: rgb(66, 132, 198);\n"
"font-family: \"Georgia\";\n"
"font-weight:bold;\n"
"color:#fff;\n"
"}")
        self.pushbtn_chiquvchi.setObjectName("pushbtn_chiquvchi")
        self.pushbtn_suv_balansi = QtWidgets.QPushButton(self.frame)
        self.pushbtn_suv_balansi.setGeometry(QtCore.QRect(30, 330, 731, 141))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setBold(True)
        font.setWeight(75)
        self.pushbtn_suv_balansi.setFont(font)
        self.pushbtn_suv_balansi.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushbtn_suv_balansi.setStyleSheet("QPushButton \n"
"{\n"
"font-size:26px;\n"
"border-radius:70px;\n"
"background-color: rgb(255, 170, 0);\n"
"font-family: \"Georgia\";\n"
"font-weight:bold;\n"
"color:#fff;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font-size:24px;\n"
"border-radius:70px;\n"
"background-color: rgb(255, 192, 3);\n"
"font-family: \"Georgia\";\n"
"font-weight:bold;\n"
"color:#fff;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/svbalansi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_suv_balansi.setIcon(icon)
        self.pushbtn_suv_balansi.setIconSize(QtCore.QSize(96, 96))
        self.pushbtn_suv_balansi.setObjectName("pushbtn_suv_balansi")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gohome.setGeometry(QtCore.QRect(10, 520, 141, 31))
        self.pushbtn_gohome.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 170, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 184, 2);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/yonalish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_gohome.setIcon(icon1)
        self.pushbtn_gohome.setIconSize(QtCore.QSize(24, 24))
        self.pushbtn_gohome.setObjectName("pushbtn_gohome")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 500, 761, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 120, 581, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Suv muvozanati"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffaa00;\">SOning suv muvozanati</span></p></body></html>"))
        self.pushbtn_kiruvchi.setText(_translate("MainWindow", "Kiruvchi suvlar"))
        self.pushbtn_chiquvchi.setText(_translate("MainWindow", "Chiquvchi suvlar"))
        self.pushbtn_suv_balansi.setText(_translate("MainWindow", "Suv balansi"))
        self.pushbtn_gohome.setText(_translate("MainWindow", "Bosh sahifaga"))
        self.pushbtn_gohome.setShortcut(_translate("MainWindow", "Space"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffaa00;\">_______________________________________________________________________________________________________________________________________________</span><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#22bc00;\">_____________________________________________________________________________________________________________</span></p></body></html>"))

class Ui_balance_main(object):
    def setupUi(self, balance_main):
        balance_main.setObjectName("balance_main")
        balance_main.resize(800, 600)
        balance_main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(balance_main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 110, 501, 61))
        self.label.setStyleSheet("font: 9pt \"Sans Serif\";\n"
"")
        self.label.setObjectName("label")
        self.pushbtn_blnc = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_blnc.setGeometry(QtCore.QRect(90, 230, 641, 101))
        self.pushbtn_blnc.setStyleSheet("QPushButton\n"
"{\n"
"font: 57 20pt \"Manjari\";\n"
"background-color: rgb(170, 170, 255);\n"
"border-radius:20px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font: 57 18pt \"Manjari\";\n"
"background-color: rgb(188, 188, 255);\n"
"border-radius:20px;\n"
"color:#fff;\n"
"}")
        self.pushbtn_blnc.setObjectName("pushbtn_blnc")
        self.pushbtn_fitr = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_fitr.setGeometry(QtCore.QRect(90, 340, 310, 91))
        self.pushbtn_fitr.setMinimumSize(QtCore.QSize(310, 0))
        self.pushbtn_fitr.setMaximumSize(QtCore.QSize(310, 16777215))
        self.pushbtn_fitr.setStyleSheet("QPushButton\n"
"{\n"
"font: 57 16pt \"Manjari\";\n"
"background-color: rgb(170, 170, 255);\n"
"border-radius:20px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font: 57 14pt \"Manjari\";\n"
"background-color: rgb(188, 188, 255);\n"
"border-radius:20px;\n"
"color:#fff;\n"
"}")
        self.pushbtn_fitr.setObjectName("pushbtn_fitr")
        self.pushbtn_bug = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_bug.setGeometry(QtCore.QRect(420, 340, 310, 91))
        self.pushbtn_bug.setMinimumSize(QtCore.QSize(310, 0))
        self.pushbtn_bug.setMaximumSize(QtCore.QSize(310, 16777215))
        self.pushbtn_bug.setStyleSheet("QPushButton\n"
"{\n"
"font: 57 16pt \"Manjari\";\n"
"background-color: rgb(170, 170, 255);\n"
"border-radius:20px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font: 57 14pt \"Manjari\";\n"
"background-color: rgb(188, 188, 255);\n"
"border-radius:20px;\n"
"color:#fff;\n"
"}")
        self.pushbtn_bug.setObjectName("pushbtn_bug")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_gohome.setGeometry(QtCore.QRect(20, 540, 121, 29))
        self.pushbtn_gohome.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 170, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 184, 2);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/yonalish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_gohome.setIcon(icon)
        self.pushbtn_gohome.setObjectName("pushbtn_gohome")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 520, 761, 20))
        self.label_6.setObjectName("label_6")
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_gobalance.setGeometry(QtCore.QRect(150, 540, 111, 29))
        self.pushbtn_gobalance.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 170, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 184, 2);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        self.pushbtn_gobalance.setIcon(icon)
        self.pushbtn_gobalance.setObjectName("pushbtn_gobalance")
        balance_main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(balance_main)
        self.statusbar.setObjectName("statusbar")
        balance_main.setStatusBar(self.statusbar)

        self.retranslateUi(balance_main)
        QtCore.QMetaObject.connectSlotsByName(balance_main)

    def retranslateUi(self, balance_main):
        _translate = QtCore.QCoreApplication.translate
        balance_main.setWindowTitle(_translate("balance_main", "Suv balansi xisooti"))
        self.label.setText(_translate("balance_main", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#4e8e80;\">Suv balansi to\'g\'risidagi xisobotlar</span></p></body></html>"))
        self.pushbtn_blnc.setText(_translate("balance_main", "Suv muvozanati"))
        self.pushbtn_fitr.setText(_translate("balance_main", "Filtiratsiyaga sarf bo`lgan suv"))
        self.pushbtn_bug.setText(_translate("balance_main", "Bug\'lanishga sarf bo`lgan suv"))
        self.pushbtn_gohome.setText(_translate("balance_main", "Bosh sahifa"))
        self.label_6.setText(_translate("balance_main", "<html><head/><body><p><span style=\" color:#ffaa00;\">_______________________________________________________________________________________________________________________________________________</span><br/></p></body></html>"))
        self.pushbtn_gobalance.setText(_translate("balance_main", "orqaga"))


class Ui_getReport(object):
    def setupUi(self, getReport):
        getReport.setObjectName("getReport")
        getReport.resize(800, 600)
        getReport.setMinimumSize(QtCore.QSize(800, 600))
        getReport.setMaximumSize(QtCore.QSize(800, 600))
        getReport.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(getReport)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 941, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 40, 291, 41))
        self.label.setStyleSheet("font: 9pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.comboBox_date = QtWidgets.QComboBox(self.frame)
        self.comboBox_date.setGeometry(QtCore.QRect(400, 40, 181, 41))
        self.comboBox_date.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"Foreground:    color: rgb(255, 255, 255);\n"
"FontSize:18px;\n"
"}")
        self.comboBox_date.setObjectName("comboBox_date")
        self.comboBox_interval = QtWidgets.QComboBox(self.frame)
        self.comboBox_interval.setGeometry(QtCore.QRect(610, 40, 171, 41))
        self.comboBox_interval.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"Foreground:    color: rgb(255, 255, 255);\n"
"FontSize:18px;\n"
"}")
        self.comboBox_interval.setObjectName("comboBox_interval")
        self.pushbtn_goback = QtWidgets.QPushButton(self.frame)
        self.pushbtn_goback.setGeometry(QtCore.QRect(270, 520, 111, 29))
        self.pushbtn_goback.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 170, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 184, 2);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/yonalish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_goback.setIcon(icon)
        self.pushbtn_goback.setObjectName("pushbtn_goback")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 500, 901, 20))
        self.label_6.setObjectName("label_6")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gohome.setGeometry(QtCore.QRect(20, 520, 121, 29))
        self.pushbtn_gohome.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 170, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 184, 2);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        self.pushbtn_gohome.setIcon(icon)
        self.pushbtn_gohome.setObjectName("pushbtn_gohome")
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gobalance.setGeometry(QtCore.QRect(150, 520, 111, 29))
        self.pushbtn_gobalance.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 170, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:0px;\n"
"background-color: rgb(255, 184, 2);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        self.pushbtn_gobalance.setIcon(icon)
        self.pushbtn_gobalance.setObjectName("pushbtn_gobalance")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 461, 20))
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 410, 771, 71))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(22)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(43)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.pushbtn_print = QtWidgets.QPushButton(self.frame)
        self.pushbtn_print.setGeometry(QtCore.QRect(620, 520, 161, 41))
        self.pushbtn_print.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:10px;\n"
"font-size:18px;\n"
"background-color: rgb(0, 170, 0);\n"
"color:#fff;\n"
"font-family:\"Manjari\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:10px;\n"
"font-size:16px;\n"
"background-color: rgb(0, 203, 0);\n"
"color:#fff;\n"
"font-family:\"Manjari\";\n"
"}")
        self.pushbtn_print.setObjectName("pushbtn_print")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 771, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/table.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.comboBox_date.raise_()
        self.comboBox_interval.raise_()
        self.pushbtn_goback.raise_()
        self.label_6.raise_()
        self.pushbtn_gohome.raise_()
        self.pushbtn_gobalance.raise_()
        self.label_7.raise_()
        self.tableWidget.raise_()
        self.pushbtn_print.raise_()
        getReport.setCentralWidget(self.centralwidget)

        self.retranslateUi(getReport)
        QtCore.QMetaObject.connectSlotsByName(getReport)

    def retranslateUi(self, getReport):
        _translate = QtCore.QCoreApplication.translate
        getReport.setWindowTitle(_translate("getReport", "Xisobotni olish"))
        self.label.setText(_translate("getReport", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#00aa00;\">Xisobotlarni olish</span></p></body></html>"))
        self.pushbtn_goback.setText(_translate("getReport", "orqaga"))
        self.label_6.setText(_translate("getReport", "<html><head/><body><p><span style=\" color:#009400;\">_______________________________________________________________________________________________________________________________________________<br/></span></p></body></html>"))
        self.pushbtn_gohome.setText(_translate("getReport", "Bosh sahifa"))
        self.pushbtn_gobalance.setText(_translate("getReport", "Suv balansi"))
        self.label_7.setText(_translate("getReport", "<html><head/><body><p><span style=\" color:#ffaa00;\">_______________________________________________________________________________________________________________________________________________</span><br/></p></body></html>"))
        self.tableWidget.setSortingEnabled(True)
        self.pushbtn_print.setText(_translate("getReport", "Chop etish"))
