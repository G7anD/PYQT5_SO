from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class w_input_main(object):
    def setupUi(self, wkiruvchi):
        wkiruvchi.setObjectName("wkiruvchi")
        wkiruvchi.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(wkiruvchi)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.frame.setStyleSheet("QFrame\n"
                                 "{\n"
                                 "background-color:#fff;\n"
                                 "border-radius:0px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox_intanlov3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_intanlov3.setGeometry(QtCore.QRect(220, 280, 391, 131))
        self.comboBox_intanlov3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_intanlov3.setStyleSheet("font: 75 16pt \"Noto Sans\";")
        self.comboBox_intanlov3.setEditable(False)
        self.comboBox_intanlov3.setCurrentText("")
        self.comboBox_intanlov3.setMaxCount(3)
        self.comboBox_intanlov3.setObjectName("comboBox_intanlov3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 90, 521, 91))
        self.label.setStyleSheet("QLabel\n"
                                 "{\n"
                                 "font-family:\"Times New Roman\";\n"
                                 "}")
        self.label.setObjectName("label")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gohome.setGeometry(QtCore.QRect(10, 540, 121, 29))
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
        icon.addPixmap(QtGui.QPixmap("img/yonalish.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_gohome.setIcon(icon)
        self.pushbtn_gohome.setObjectName("pushbtn_gohome")
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gobalance.setGeometry(QtCore.QRect(140, 540, 111, 29))
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 510, 761, 20))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(100, 200, 631, 281))
        self.frame_2.setStyleSheet("QFrame\n"
                                   "{\n"
                                   "background-color: rgb(83, 151, 137);\n"
                                   "border-radius:20px;\n"
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.comboBox_intanlov3.raise_()
        self.label.raise_()
        self.pushbtn_gohome.raise_()
        self.pushbtn_gobalance.raise_()
        self.label_2.raise_()
        wkiruvchi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wkiruvchi)
        self.statusbar.setObjectName("statusbar")
        wkiruvchi.setStatusBar(self.statusbar)

        self.retranslateUi(wkiruvchi)
        QtCore.QMetaObject.connectSlotsByName(wkiruvchi)
        self.comboBox_intanlov3.addItem("Kunlik")
        self.comboBox_intanlov3.addItem("10 Kunlik")
        self.comboBox_intanlov3.addItem("Oylik")

    def retranslateUi(self, wkiruvchi):
        _translate = QtCore.QCoreApplication.translate
        wkiruvchi.setWindowTitle(_translate("wkiruvchi", "Kiruvchi suvlar"))
        self.label.setText(_translate(
            "wkiruvchi", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#539789;\">O\'lchash natijalarini kiritish</span></p></body></html>"))
        self.pushbtn_gohome.setText(_translate("wkiruvchi", "Bosh sahifa"))
        self.pushbtn_gobalance.setText(_translate("wkiruvchi", "Orqaga"))
        self.label_2.setText(_translate(
            "wkiruvchi", "<html><head/><body><p><span style=\" color:#ffaa00;\">_______________________________________________________________________________________________________________________________________________</span><br/></p></body></html>"))
# w_kiruvchi subpg


class Ui_daily(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setMinimumSize(QtCore.QSize(800, 600))
        self.frame.setMaximumSize(QtCore.QSize(800, 600))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 311, 91))
        self.label.setStyleSheet("font: 9pt \"MathJax_WinIE6\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(50, 130, 371, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 431, 41))
        self.label_2.setStyleSheet("font: 9pt \"Noto Naskh Arabic\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 280, 431, 41))
        self.label_3.setStyleSheet("font: 9pt \"Noto Naskh Arabic\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 360, 431, 41))
        self.label_4.setStyleSheet("font: 9pt \"Noto Naskh Arabic\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 430, 431, 41))
        self.label_5.setStyleSheet("font: 9pt \"Noto Naskh Arabic\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 510, 761, 20))
        self.label_6.setObjectName("label_6")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gohome.setGeometry(QtCore.QRect(20, 530, 121, 29))
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
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gobalance.setGeometry(QtCore.QRect(150, 530, 111, 29))
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
        self.pushbtn_goback = QtWidgets.QPushButton(self.frame)
        self.pushbtn_goback.setGeometry(QtCore.QRect(270, 530, 111, 29))
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
        self.pushbtn_goback.setIcon(icon)
        self.pushbtn_goback.setObjectName("pushbtn_goback")
        self.pushbtn_save = QtWidgets.QPushButton(self.frame)
        self.pushbtn_save.setGeometry(QtCore.QRect(600, 530, 171, 41))
        self.pushbtn_save.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(89, 179, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(101, 203, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        self.pushbtn_save.setObjectName("pushbtn_save")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 500, 181, 20))
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 190, 251, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_qora = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_qora.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit_qora.setObjectName("lineEdit_qora")
        self.gridLayout.addWidget(self.lineEdit_qora, 0, 0, 1, 1)
        self.lineEdit_yassi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_yassi.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit_yassi.setObjectName("lineEdit_yassi")
        self.gridLayout.addWidget(self.lineEdit_yassi, 1, 0, 1, 1)
        self.lineEdit_qurshab = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_qurshab.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit_qurshab.setObjectName("lineEdit_qurshab")
        self.gridLayout.addWidget(self.lineEdit_qurshab, 2, 0, 1, 1)
        self.lineEdit_yomgir = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_yomgir.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit_yomgir.setObjectName("lineEdit_yomgir")
        self.gridLayout.addWidget(self.lineEdit_yomgir, 3, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.todaysdate = datetime.date.today()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(
            QtCore.QDate(self.todaysdate.year,
                         self.todaysdate.month, self.todaysdate.day),
            QtCore.QTime(int(datetime.datetime.now().strftime("%H:%M").split(':')[0]),int(datetime.datetime.now().strftime("%H:%M").split(':')[1]))))

        self.dateTimeEdit.setGeometry(QtCore.QRect(490, 60, 271, 71))
        self.dateTimeEdit.setStyleSheet("QDateTimeEdit\n"
"{\n"
"font-size:22px;\n"
"}")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kunlik Ma\'lumotlarni kiritish"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Kerakli sanani kiriting:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#539789;\">Qora daryoda quyilgan suv M:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;color:#539789;\">Yassi daryoda quyilgan suv M:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;color:#539789;\">Qurshab daryoda quyilgan suv M:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;color:#539789;\">SO yuzasiga tushgan yomgirlar M:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffaa00;\">_______________________________________________________________________________________________________________________________________________</span><br/></p></body></html>"))
        self.pushbtn_gohome.setText(_translate("MainWindow", "Bosh sahifa"))
        self.pushbtn_gobalance.setText(_translate("MainWindow", "Suv balansi"))
        self.pushbtn_goback.setText(_translate("MainWindow", "orqaga"))
        self.pushbtn_save.setText(_translate("MainWindow", "Kiritish"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff5500;\">Izoh:</span><span style=\" color:#000000;\"> M - Miqdori !</span></p></body></html>"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "d/M/yy h:mm "))


class Ui_tenDay(object):
    def setupUi(self, onkunlikin):
        onkunlikin.setObjectName("onkunlikin")
        onkunlikin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(onkunlikin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 381, 51))
        self.label_15.setStyleSheet("font: 75 9pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(20, 450, 591, 41))
        self.label_16.setObjectName("label_16")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gohome.setGeometry(QtCore.QRect(20, 510, 121, 29))
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
        self.pushbtn_goback = QtWidgets.QPushButton(self.frame)
        self.pushbtn_goback.setGeometry(QtCore.QRect(270, 510, 111, 29))
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
        self.pushbtn_goback.setIcon(icon)
        self.pushbtn_goback.setObjectName("pushbtn_goback")
        self.pushbtn_save = QtWidgets.QPushButton(self.frame)
        self.pushbtn_save.setGeometry(QtCore.QRect(600, 510, 171, 41))
        self.pushbtn_save.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(89, 179, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(101, 203, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        self.pushbtn_save.setObjectName("pushbtn_save")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(20, 490, 761, 20))
        self.label_17.setObjectName("label_17")
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gobalance.setGeometry(QtCore.QRect(150, 510, 111, 29))
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
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit.setGeometry(QtCore.QRect(500, 50, 281, 61))
        self.todaysdate = datetime.date.today()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(
            QtCore.QDate(self.todaysdate.year,
                         self.todaysdate.month, self.todaysdate.day),
            QtCore.QTime(int(datetime.datetime.now().strftime("%H:%M").split(':')[0]),int(datetime.datetime.now().strftime("%H:%M").split(':')[1]))))
        self.dateTimeEdit.setStyleSheet("QDateTimeEdit\n"
"{\n"
"font-size:20px;\n"
"}")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(410, 60, 71, 31))
        self.label_18.setObjectName("label_18")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 80, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(190, 170, 504, 229))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_57 = QtWidgets.QLabel(self.widget)
        self.label_57.setObjectName("label_57")
        self.gridLayout_2.addWidget(self.label_57, 0, 7, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.widget)
        self.label_53.setObjectName("label_53")
        self.gridLayout_2.addWidget(self.label_53, 0, 2, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.widget)
        self.label_56.setObjectName("label_56")
        self.gridLayout_2.addWidget(self.label_56, 0, 6, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.widget)
        self.label_55.setObjectName("label_55")
        self.gridLayout_2.addWidget(self.label_55, 0, 5, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.widget)
        self.label_52.setObjectName("label_52")
        self.gridLayout_2.addWidget(self.label_52, 0, 1, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.widget)
        self.label_59.setObjectName("label_59")
        self.gridLayout_2.addWidget(self.label_59, 0, 8, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.widget)
        self.label_62.setObjectName("label_62")
        self.gridLayout_2.addWidget(self.label_62, 0, 9, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.widget)
        self.label_51.setObjectName("label_51")
        self.gridLayout_2.addWidget(self.label_51, 0, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.widget)
        self.label_54.setObjectName("label_54")
        self.gridLayout_2.addWidget(self.label_54, 0, 3, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.widget)
        self.label_58.setObjectName("label_58")
        self.gridLayout_2.addWidget(self.label_58, 0, 4, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_0_0 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_0.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_0.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_0.setObjectName("lineEdit_0_0")
        self.gridLayout.addWidget(self.lineEdit_0_0, 0, 0, 1, 1)
        self.lineEdit_0_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_1.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_1.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_1.setObjectName("lineEdit_0_1")
        self.gridLayout.addWidget(self.lineEdit_0_1, 0, 1, 1, 1)
        self.lineEdit_0_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_2.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_2.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_2.setObjectName("lineEdit_0_2")
        self.gridLayout.addWidget(self.lineEdit_0_2, 0, 2, 1, 1)
        self.lineEdit_0_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_3.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_3.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_3.setObjectName("lineEdit_0_3")
        self.gridLayout.addWidget(self.lineEdit_0_3, 0, 3, 1, 1)
        self.lineEdit_0_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_4.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_4.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_4.setObjectName("lineEdit_0_4")
        self.gridLayout.addWidget(self.lineEdit_0_4, 0, 4, 1, 1)
        self.lineEdit_0_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_5.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_5.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_5.setObjectName("lineEdit_0_5")
        self.gridLayout.addWidget(self.lineEdit_0_5, 0, 5, 1, 1)
        self.lineEdit_0_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_6.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_6.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_6.setObjectName("lineEdit_0_6")
        self.gridLayout.addWidget(self.lineEdit_0_6, 0, 6, 1, 1)
        self.lineEdit_0_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_7.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_7.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_7.setObjectName("lineEdit_0_7")
        self.gridLayout.addWidget(self.lineEdit_0_7, 0, 7, 1, 1)
        self.lineEdit_0_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_8.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_8.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_8.setObjectName("lineEdit_0_8")
        self.gridLayout.addWidget(self.lineEdit_0_8, 0, 8, 1, 1)
        self.lineEdit_0_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_0_9.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_9.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_0_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_9.setObjectName("lineEdit_0_9")
        self.gridLayout.addWidget(self.lineEdit_0_9, 0, 9, 1, 1)
        self.lineEdit_1_0 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_0.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_0.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_0.setObjectName("lineEdit_1_0")
        self.gridLayout.addWidget(self.lineEdit_1_0, 1, 0, 1, 1)
        self.lineEdit_1_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_1.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_1.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_1.setObjectName("lineEdit_1_1")
        self.gridLayout.addWidget(self.lineEdit_1_1, 1, 1, 1, 1)
        self.lineEdit_1_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_2.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_2.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_2.setObjectName("lineEdit_1_2")
        self.gridLayout.addWidget(self.lineEdit_1_2, 1, 2, 1, 1)
        self.lineEdit_1_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_3.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_3.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_3.setObjectName("lineEdit_1_3")
        self.gridLayout.addWidget(self.lineEdit_1_3, 1, 3, 1, 1)
        self.lineEdit_1_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_4.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_4.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_4.setObjectName("lineEdit_1_4")
        self.gridLayout.addWidget(self.lineEdit_1_4, 1, 4, 1, 1)
        self.lineEdit_1_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_5.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_5.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_5.setObjectName("lineEdit_1_5")
        self.gridLayout.addWidget(self.lineEdit_1_5, 1, 5, 1, 1)
        self.lineEdit_1_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_6.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_6.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_6.setObjectName("lineEdit_1_6")
        self.gridLayout.addWidget(self.lineEdit_1_6, 1, 6, 1, 1)
        self.lineEdit_1_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_7.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_7.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_7.setObjectName("lineEdit_1_7")
        self.gridLayout.addWidget(self.lineEdit_1_7, 1, 7, 1, 1)
        self.lineEdit_1_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_8.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_8.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_8.setObjectName("lineEdit_1_8")
        self.gridLayout.addWidget(self.lineEdit_1_8, 1, 8, 1, 1)
        self.lineEdit_1_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1_9.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_9.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_1_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_9.setObjectName("lineEdit_1_9")
        self.gridLayout.addWidget(self.lineEdit_1_9, 1, 9, 1, 1)
        self.lineEdit_2_0 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_0.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_0.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_0.setObjectName("lineEdit_2_0")
        self.gridLayout.addWidget(self.lineEdit_2_0, 2, 0, 1, 1)
        self.lineEdit_2_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_1.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_1.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_1.setObjectName("lineEdit_2_1")
        self.gridLayout.addWidget(self.lineEdit_2_1, 2, 1, 1, 1)
        self.lineEdit_2_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_2.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_2.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_2.setObjectName("lineEdit_2_2")
        self.gridLayout.addWidget(self.lineEdit_2_2, 2, 2, 1, 1)
        self.lineEdit_2_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_3.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_3.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_3.setObjectName("lineEdit_2_3")
        self.gridLayout.addWidget(self.lineEdit_2_3, 2, 3, 1, 1)
        self.lineEdit_2_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_4.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_4.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_4.setObjectName("lineEdit_2_4")
        self.gridLayout.addWidget(self.lineEdit_2_4, 2, 4, 1, 1)
        self.lineEdit_2_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_5.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_5.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_5.setObjectName("lineEdit_2_5")
        self.gridLayout.addWidget(self.lineEdit_2_5, 2, 5, 1, 1)
        self.lineEdit_2_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_6.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_6.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_6.setObjectName("lineEdit_2_6")
        self.gridLayout.addWidget(self.lineEdit_2_6, 2, 6, 1, 1)
        self.lineEdit_2_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_7.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_7.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_7.setObjectName("lineEdit_2_7")
        self.gridLayout.addWidget(self.lineEdit_2_7, 2, 7, 1, 1)
        self.lineEdit_2_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_8.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_8.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_8.setObjectName("lineEdit_2_8")
        self.gridLayout.addWidget(self.lineEdit_2_8, 2, 8, 1, 1)
        self.lineEdit_2_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2_9.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_9.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_2_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_9.setObjectName("lineEdit_2_9")
        self.gridLayout.addWidget(self.lineEdit_2_9, 2, 9, 1, 1)
        self.lineEdit_3_0 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_0.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_0.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_0.setObjectName("lineEdit_3_0")
        self.gridLayout.addWidget(self.lineEdit_3_0, 3, 0, 1, 1)
        self.lineEdit_3_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_1.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_1.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_1.setObjectName("lineEdit_3_1")
        self.gridLayout.addWidget(self.lineEdit_3_1, 3, 1, 1, 1)
        self.lineEdit_3_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_2.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_2.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_2.setObjectName("lineEdit_3_2")
        self.gridLayout.addWidget(self.lineEdit_3_2, 3, 2, 1, 1)
        self.lineEdit_3_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_3.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_3.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_3.setObjectName("lineEdit_3_3")
        self.gridLayout.addWidget(self.lineEdit_3_3, 3, 3, 1, 1)
        self.lineEdit_3_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_4.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_4.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_4.setObjectName("lineEdit_3_4")
        self.gridLayout.addWidget(self.lineEdit_3_4, 3, 4, 1, 1)
        self.lineEdit_3_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_5.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_5.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_5.setObjectName("lineEdit_3_5")
        self.gridLayout.addWidget(self.lineEdit_3_5, 3, 5, 1, 1)
        self.lineEdit_3_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_6.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_6.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_6.setObjectName("lineEdit_3_6")
        self.gridLayout.addWidget(self.lineEdit_3_6, 3, 6, 1, 1)
        self.lineEdit_3_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_7.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_7.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_7.setObjectName("lineEdit_3_7")
        self.gridLayout.addWidget(self.lineEdit_3_7, 3, 7, 1, 1)
        self.lineEdit_3_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_8.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_8.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_8.setObjectName("lineEdit_3_8")
        self.gridLayout.addWidget(self.lineEdit_3_8, 3, 8, 1, 1)
        self.lineEdit_3_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3_9.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_9.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEdit_3_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_9.setObjectName("lineEdit_3_9")
        self.gridLayout.addWidget(self.lineEdit_3_9, 3, 9, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(124, 198, 67, 201))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_83 = QtWidgets.QLabel(self.widget1)
        self.label_83.setStyleSheet("font: 57 9pt \"Times New Roman\";")
        self.label_83.setObjectName("label_83")
        self.gridLayout_3.addWidget(self.label_83, 0, 0, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.widget1)
        self.label_82.setStyleSheet("font: 57 9pt \"Times New Roman\";")
        self.label_82.setObjectName("label_82")
        self.gridLayout_3.addWidget(self.label_82, 1, 0, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.widget1)
        self.label_81.setStyleSheet("font: 57 9pt \"Times New Roman\";")
        self.label_81.setObjectName("label_81")
        self.gridLayout_3.addWidget(self.label_81, 2, 0, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.widget1)
        self.label_84.setStyleSheet("font: 57 9pt \"Times New Roman\";")
        self.label_84.setObjectName("label_84")
        self.gridLayout_3.addWidget(self.label_84, 3, 0, 1, 1)
        onkunlikin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(onkunlikin)
        self.statusbar.setObjectName("statusbar")
        onkunlikin.setStatusBar(self.statusbar)

        self.retranslateUi(onkunlikin)
        QtCore.QMetaObject.connectSlotsByName(onkunlikin)

    def retranslateUi(self, onkunlikin):
        _translate = QtCore.QCoreApplication.translate
        onkunlikin.setWindowTitle(_translate("onkunlikin", "10 kunlik ma\'limolarni kiritish"))
        self.label_15.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#5cb333;\">10 kunlik ma\'lumotlarni kiritish</span></p></body></html>"))
        self.label_16.setText(_translate("onkunlikin", "<html><head/><body><p><span style=\" color:#ff0000;\">Qo\'shimcha: </span>1- ustunga birinchi kun ma`lumotlari, 2-ustunga ikkinchi kun ma`lumotlari kiritiladi va hk.</p></body></html>"))
        self.pushbtn_gohome.setText(_translate("onkunlikin", "Bosh sahifa"))
        self.pushbtn_goback.setText(_translate("onkunlikin", "orqaga"))
        self.pushbtn_save.setText(_translate("onkunlikin", "Kiritish"))
        self.label_17.setText(_translate("onkunlikin", "<html><head/><body><p><span style=\" color:#ffaa00;\">_______________________________________________________________________________________________________________________________________________</span><br/></p></body></html>"))
        self.pushbtn_gobalance.setText(_translate("onkunlikin", "Suv balansi"))
        self.dateTimeEdit.setToolTip(_translate("onkunlikin", "<html><head/><body><p>kiritilgan sanadan boshlab 10 kun hisoblaydi</p></body></html>"))
        self.dateTimeEdit.setDisplayFormat(_translate("onkunlikin", "d/M/yy h:mm"))
        self.label_18.setToolTip(_translate("onkunlikin", "<html><head/><body><p>kiritilgan sanadan boshlab 10 kun hisoblaydi</p></body></html>"))
        self.label_18.setText(_translate("onkunlikin", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Sana:</span></p></body></html>"))
        self.label_57.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">8</p></body></html>"))
        self.label_53.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">3</p></body></html>"))
        self.label_56.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">7</p></body></html>"))
        self.label_55.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">6</p></body></html>"))
        self.label_52.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">2</p></body></html>"))
        self.label_59.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">9</p></body></html>"))
        self.label_62.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">10</p></body></html>"))
        self.label_51.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">1</p></body></html>"))
        self.label_54.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">4</p></body></html>"))
        self.label_58.setText(_translate("onkunlikin", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_83.setText(_translate("onkunlikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">Qora</span></p></body></html>"))
        self.label_82.setText(_translate("onkunlikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">Yassi</span></p></body></html>"))
        self.label_81.setText(_translate("onkunlikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">Qurshab</span></p></body></html>"))
        self.label_84.setText(_translate("onkunlikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">Yomg\'ir</span></p></body></html>"))

class Ui_monthly(object):
    def setupUi(self, oylikin):
        oylikin.setObjectName("oylikin")
        oylikin.resize(800, 600)
        oylikin.setMinimumSize(QtCore.QSize(800, 600))
        oylikin.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(oylikin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 381, 51))
        self.label_15.setStyleSheet("font: 75 9pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(20, 500, 591, 41))
        self.label_16.setObjectName("label_16")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gohome.setGeometry(QtCore.QRect(20, 550, 121, 29))
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
        self.pushbtn_goback = QtWidgets.QPushButton(self.frame)
        self.pushbtn_goback.setGeometry(QtCore.QRect(270, 550, 111, 29))
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
        self.pushbtn_goback.setIcon(icon)
        self.pushbtn_goback.setObjectName("pushbtn_goback")
        self.pushbtn_save = QtWidgets.QPushButton(self.frame)
        self.pushbtn_save.setGeometry(QtCore.QRect(600, 540, 171, 41))
        self.pushbtn_save.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(89, 179, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(101, 203, 0);\n"
"color:#fff;\n"
"font-size:15px;\n"
"font-family:\"Manjari\";\n"
"padding-top:4px;\n"
"}\n"
"")
        self.pushbtn_save.setObjectName("pushbtn_save")
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.frame)
        self.pushbtn_gobalance.setGeometry(QtCore.QRect(150, 550, 111, 29))
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
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit.setGeometry(QtCore.QRect(500, 30, 281, 61))
        self.dateTimeEdit.setStyleSheet("QDateTimeEdit\n"
"{\n"
"font-size:20px;\n"
"}")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(410, 40, 71, 31))
        self.label_18.setObjectName("label_18")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 70, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_0_0 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_0.setGeometry(QtCore.QRect(150, 140, 41, 40))
        self.lineEdit_0_0.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_0.setMaximumSize(QtCore.QSize(16777215, 40))
        self.todaysdate = datetime.date.today()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(
            QtCore.QDate(self.todaysdate.year,
                         self.todaysdate.month, self.todaysdate.day),
            QtCore.QTime(int(datetime.datetime.now().strftime("%H:%M").split(':')[0]),int(datetime.datetime.now().strftime("%H:%M").split(':')[1]))))
        self.lineEdit_0_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_0.setObjectName("lineEdit_0_0")
        self.lineEdit_1_0 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_0.setGeometry(QtCore.QRect(150, 180, 41, 40))
        self.lineEdit_1_0.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_0.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_0.setObjectName("lineEdit_1_0")
        self.lineEdit_2_0 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_0.setGeometry(QtCore.QRect(150, 220, 41, 40))
        self.lineEdit_2_0.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_0.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_0.setObjectName("lineEdit_2_0")
        self.lineEdit_3_0 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_0.setGeometry(QtCore.QRect(150, 260, 41, 40))
        self.lineEdit_3_0.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_0.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_0.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_0.setObjectName("lineEdit_3_0")
        self.lineEdit_3_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_1.setGeometry(QtCore.QRect(190, 260, 41, 40))
        self.lineEdit_3_1.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_1.setObjectName("lineEdit_3_1")
        self.lineEdit_1_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_1.setGeometry(QtCore.QRect(190, 180, 41, 40))
        self.lineEdit_1_1.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_1.setObjectName("lineEdit_1_1")
        self.lineEdit_0_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_1.setGeometry(QtCore.QRect(190, 140, 41, 40))
        self.lineEdit_0_1.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_1.setObjectName("lineEdit_0_1")
        self.lineEdit_2_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_1.setGeometry(QtCore.QRect(190, 220, 41, 40))
        self.lineEdit_2_1.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_1.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_1.setObjectName("lineEdit_2_1")
        self.lineEdit_3_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_2.setGeometry(QtCore.QRect(230, 260, 41, 40))
        self.lineEdit_3_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_2.setObjectName("lineEdit_3_2")
        self.lineEdit_0_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_2.setGeometry(QtCore.QRect(230, 140, 41, 40))
        self.lineEdit_0_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_2.setObjectName("lineEdit_0_2")
        self.lineEdit_1_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_3.setGeometry(QtCore.QRect(270, 180, 41, 40))
        self.lineEdit_1_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_3.setObjectName("lineEdit_1_3")
        self.lineEdit_2_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_2.setGeometry(QtCore.QRect(230, 220, 41, 40))
        self.lineEdit_2_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_2.setObjectName("lineEdit_2_2")
        self.lineEdit_3_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_3.setGeometry(QtCore.QRect(270, 260, 41, 40))
        self.lineEdit_3_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_3.setObjectName("lineEdit_3_3")
        self.lineEdit_3_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_4.setGeometry(QtCore.QRect(310, 260, 41, 40))
        self.lineEdit_3_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_4.setObjectName("lineEdit_3_4")
        self.lineEdit_1_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_2.setGeometry(QtCore.QRect(230, 180, 41, 40))
        self.lineEdit_1_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_2.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_2.setObjectName("lineEdit_1_2")
        self.lineEdit_0_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_3.setGeometry(QtCore.QRect(270, 140, 41, 40))
        self.lineEdit_0_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_3.setObjectName("lineEdit_0_3")
        self.lineEdit_1_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_4.setGeometry(QtCore.QRect(310, 180, 41, 40))
        self.lineEdit_1_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_4.setObjectName("lineEdit_1_4")
        self.lineEdit_2_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_3.setGeometry(QtCore.QRect(270, 220, 41, 40))
        self.lineEdit_2_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_3.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_3.setObjectName("lineEdit_2_3")
        self.lineEdit_0_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_4.setGeometry(QtCore.QRect(310, 140, 41, 40))
        self.lineEdit_0_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_4.setObjectName("lineEdit_0_4")
        self.lineEdit_3_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_5.setGeometry(QtCore.QRect(350, 260, 41, 40))
        self.lineEdit_3_5.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_5.setObjectName("lineEdit_3_5")
        self.lineEdit_1_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_5.setGeometry(QtCore.QRect(350, 180, 41, 40))
        self.lineEdit_1_5.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_5.setObjectName("lineEdit_1_5")
        self.lineEdit_0_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_5.setGeometry(QtCore.QRect(350, 140, 41, 40))
        self.lineEdit_0_5.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_5.setObjectName("lineEdit_0_5")
        self.lineEdit_2_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_4.setGeometry(QtCore.QRect(310, 220, 41, 40))
        self.lineEdit_2_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_4.setObjectName("lineEdit_2_4")
        self.lineEdit_2_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_5.setGeometry(QtCore.QRect(350, 220, 41, 40))
        self.lineEdit_2_5.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_5.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_5.setObjectName("lineEdit_2_5")
        self.lineEdit_3_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_6.setGeometry(QtCore.QRect(390, 260, 41, 40))
        self.lineEdit_3_6.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_6.setObjectName("lineEdit_3_6")
        self.lineEdit_2_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_6.setGeometry(QtCore.QRect(390, 220, 41, 40))
        self.lineEdit_2_6.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_6.setObjectName("lineEdit_2_6")
        self.lineEdit_2_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_7.setGeometry(QtCore.QRect(430, 220, 41, 40))
        self.lineEdit_2_7.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_7.setObjectName("lineEdit_2_7")
        self.lineEdit_1_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_6.setGeometry(QtCore.QRect(390, 180, 41, 40))
        self.lineEdit_1_6.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_6.setObjectName("lineEdit_1_6")
        self.lineEdit_1_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_7.setGeometry(QtCore.QRect(430, 180, 41, 40))
        self.lineEdit_1_7.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_7.setObjectName("lineEdit_1_7")
        self.lineEdit_1_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_8.setGeometry(QtCore.QRect(470, 180, 41, 40))
        self.lineEdit_1_8.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_8.setObjectName("lineEdit_1_8")
        self.lineEdit_2_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_8.setGeometry(QtCore.QRect(470, 220, 41, 40))
        self.lineEdit_2_8.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_8.setObjectName("lineEdit_2_8")
        self.lineEdit_3_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_7.setGeometry(QtCore.QRect(430, 260, 41, 40))
        self.lineEdit_3_7.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_7.setObjectName("lineEdit_3_7")
        self.lineEdit_1_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_9.setGeometry(QtCore.QRect(510, 180, 41, 40))
        self.lineEdit_1_9.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_9.setObjectName("lineEdit_1_9")
        self.lineEdit_0_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_6.setGeometry(QtCore.QRect(390, 140, 41, 40))
        self.lineEdit_0_6.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_6.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_6.setObjectName("lineEdit_0_6")
        self.lineEdit_3_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_8.setGeometry(QtCore.QRect(470, 260, 41, 40))
        self.lineEdit_3_8.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_8.setObjectName("lineEdit_3_8")
        self.lineEdit_0_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_7.setGeometry(QtCore.QRect(430, 140, 41, 40))
        self.lineEdit_0_7.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_7.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_7.setObjectName("lineEdit_0_7")
        self.lineEdit_2_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_9.setGeometry(QtCore.QRect(510, 220, 41, 40))
        self.lineEdit_2_9.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_9.setObjectName("lineEdit_2_9")
        self.lineEdit_3_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_9.setGeometry(QtCore.QRect(510, 260, 41, 40))
        self.lineEdit_3_9.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_9.setObjectName("lineEdit_3_9")
        self.lineEdit_0_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_8.setGeometry(QtCore.QRect(470, 140, 41, 40))
        self.lineEdit_0_8.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_8.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_8.setObjectName("lineEdit_0_8")
        self.lineEdit_0_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_9.setGeometry(QtCore.QRect(510, 140, 41, 40))
        self.lineEdit_0_9.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_9.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_9.setObjectName("lineEdit_0_9")
        self.lineEdit_2_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_10.setGeometry(QtCore.QRect(550, 220, 41, 40))
        self.lineEdit_2_10.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_10.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_10.setObjectName("lineEdit_2_10")
        self.lineEdit_3_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_10.setGeometry(QtCore.QRect(550, 260, 41, 40))
        self.lineEdit_3_10.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_10.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_10.setObjectName("lineEdit_3_10")
        self.lineEdit_1_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_10.setGeometry(QtCore.QRect(550, 180, 41, 40))
        self.lineEdit_1_10.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_10.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_10.setObjectName("lineEdit_1_10")
        self.lineEdit_1_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_11.setGeometry(QtCore.QRect(590, 180, 41, 40))
        self.lineEdit_1_11.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_11.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_11.setObjectName("lineEdit_1_11")
        self.lineEdit_0_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_10.setGeometry(QtCore.QRect(550, 140, 41, 40))
        self.lineEdit_0_10.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_10.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_10.setObjectName("lineEdit_0_10")
        self.lineEdit_2_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_11.setGeometry(QtCore.QRect(590, 220, 41, 40))
        self.lineEdit_2_11.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_11.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_11.setObjectName("lineEdit_2_11")
        self.lineEdit_3_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_11.setGeometry(QtCore.QRect(590, 260, 41, 40))
        self.lineEdit_3_11.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_11.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_11.setObjectName("lineEdit_3_11")
        self.lineEdit_0_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_11.setGeometry(QtCore.QRect(590, 140, 41, 40))
        self.lineEdit_0_11.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_11.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_11.setObjectName("lineEdit_0_11")
        self.lineEdit_3_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_12.setGeometry(QtCore.QRect(630, 260, 41, 40))
        self.lineEdit_3_12.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_12.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_12.setObjectName("lineEdit_3_12")
        self.lineEdit_0_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_12.setGeometry(QtCore.QRect(630, 140, 41, 40))
        self.lineEdit_0_12.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_12.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_12.setObjectName("lineEdit_0_12")
        self.lineEdit_0_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_13.setGeometry(QtCore.QRect(670, 140, 41, 40))
        self.lineEdit_0_13.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_13.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_13.setObjectName("lineEdit_0_13")
        self.lineEdit_3_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_13.setGeometry(QtCore.QRect(670, 260, 41, 40))
        self.lineEdit_3_13.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_13.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_13.setObjectName("lineEdit_3_13")
        self.lineEdit_1_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_12.setGeometry(QtCore.QRect(630, 180, 41, 40))
        self.lineEdit_1_12.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_12.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_12.setObjectName("lineEdit_1_12")
        self.lineEdit_1_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_13.setGeometry(QtCore.QRect(670, 180, 41, 40))
        self.lineEdit_1_13.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_13.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_13.setObjectName("lineEdit_1_13")
        self.lineEdit_3_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_14.setGeometry(QtCore.QRect(710, 260, 41, 40))
        self.lineEdit_3_14.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_14.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_14.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_14.setObjectName("lineEdit_3_14")
        self.lineEdit_1_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_14.setGeometry(QtCore.QRect(710, 180, 41, 40))
        self.lineEdit_1_14.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_14.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_14.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_14.setObjectName("lineEdit_1_14")
        self.lineEdit_2_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_12.setGeometry(QtCore.QRect(710, 220, 41, 40))
        self.lineEdit_2_12.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_12.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_12.setObjectName("lineEdit_2_12")
        self.lineEdit_2_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_13.setGeometry(QtCore.QRect(630, 220, 41, 40))
        self.lineEdit_2_13.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_13.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_13.setObjectName("lineEdit_2_13")
        self.lineEdit_2_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_14.setGeometry(QtCore.QRect(670, 220, 41, 40))
        self.lineEdit_2_14.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_14.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_14.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_14.setObjectName("lineEdit_2_14")
        self.lineEdit_0_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_14.setGeometry(QtCore.QRect(710, 140, 41, 40))
        self.lineEdit_0_14.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_14.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_14.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_14.setObjectName("lineEdit_0_14")
        self.lineEdit_3_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_15.setGeometry(QtCore.QRect(150, 460, 41, 40))
        self.lineEdit_3_15.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_15.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_15.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_15.setObjectName("lineEdit_3_15")
        self.lineEdit_2_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_15.setGeometry(QtCore.QRect(150, 420, 41, 40))
        self.lineEdit_2_15.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_15.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_15.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_15.setObjectName("lineEdit_2_15")
        self.lineEdit_1_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_15.setGeometry(QtCore.QRect(150, 380, 41, 40))
        self.lineEdit_1_15.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_15.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_15.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_15.setObjectName("lineEdit_1_15")
        self.lineEdit_0_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_15.setGeometry(QtCore.QRect(150, 340, 41, 40))
        self.lineEdit_0_15.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_15.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_15.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_15.setObjectName("lineEdit_0_15")
        self.lineEdit_3_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_16.setGeometry(QtCore.QRect(190, 460, 41, 40))
        self.lineEdit_3_16.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_16.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_16.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_16.setObjectName("lineEdit_3_16")
        self.lineEdit_0_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_16.setGeometry(QtCore.QRect(190, 340, 41, 40))
        self.lineEdit_0_16.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_16.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_16.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_16.setObjectName("lineEdit_0_16")
        self.lineEdit_2_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_16.setGeometry(QtCore.QRect(190, 420, 41, 40))
        self.lineEdit_2_16.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_16.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_16.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_16.setObjectName("lineEdit_2_16")
        self.lineEdit_1_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_16.setGeometry(QtCore.QRect(190, 380, 41, 40))
        self.lineEdit_1_16.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_16.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_16.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_16.setObjectName("lineEdit_1_16")
        self.lineEdit_0_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_17.setGeometry(QtCore.QRect(230, 340, 41, 40))
        self.lineEdit_0_17.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_17.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_17.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_17.setObjectName("lineEdit_0_17")
        self.lineEdit_2_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_17.setGeometry(QtCore.QRect(230, 420, 41, 40))
        self.lineEdit_2_17.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_17.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_17.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_17.setObjectName("lineEdit_2_17")
        self.lineEdit_3_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_17.setGeometry(QtCore.QRect(230, 460, 41, 40))
        self.lineEdit_3_17.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_17.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_17.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_17.setObjectName("lineEdit_3_17")
        self.lineEdit_1_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_17.setGeometry(QtCore.QRect(230, 380, 41, 40))
        self.lineEdit_1_17.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_17.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_17.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_17.setObjectName("lineEdit_1_17")
        self.lineEdit_3_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_18.setGeometry(QtCore.QRect(270, 460, 41, 40))
        self.lineEdit_3_18.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_18.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_18.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_18.setObjectName("lineEdit_3_18")
        self.lineEdit_0_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_18.setGeometry(QtCore.QRect(270, 340, 41, 40))
        self.lineEdit_0_18.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_18.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_18.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_18.setObjectName("lineEdit_0_18")
        self.lineEdit_1_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_18.setGeometry(QtCore.QRect(270, 380, 41, 40))
        self.lineEdit_1_18.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_18.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_18.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_18.setObjectName("lineEdit_1_18")
        self.lineEdit_2_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_18.setGeometry(QtCore.QRect(270, 420, 41, 40))
        self.lineEdit_2_18.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_18.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_18.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_18.setObjectName("lineEdit_2_18")
        self.lineEdit_0_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_19.setGeometry(QtCore.QRect(310, 340, 41, 40))
        self.lineEdit_0_19.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_19.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_19.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_19.setObjectName("lineEdit_0_19")
        self.lineEdit_2_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_19.setGeometry(QtCore.QRect(310, 420, 41, 40))
        self.lineEdit_2_19.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_19.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_19.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_19.setObjectName("lineEdit_2_19")
        self.lineEdit_1_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_19.setGeometry(QtCore.QRect(310, 380, 41, 40))
        self.lineEdit_1_19.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_19.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_19.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_19.setObjectName("lineEdit_1_19")
        self.lineEdit_3_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_19.setGeometry(QtCore.QRect(310, 460, 41, 40))
        self.lineEdit_3_19.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_19.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_19.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_19.setObjectName("lineEdit_3_19")
        self.lineEdit_2_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_20.setGeometry(QtCore.QRect(350, 420, 41, 40))
        self.lineEdit_2_20.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_20.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_20.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_20.setObjectName("lineEdit_2_20")
        self.lineEdit_1_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_20.setGeometry(QtCore.QRect(350, 380, 41, 40))
        self.lineEdit_1_20.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_20.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_20.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_20.setObjectName("lineEdit_1_20")
        self.lineEdit_0_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_20.setGeometry(QtCore.QRect(350, 340, 41, 40))
        self.lineEdit_0_20.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_20.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_20.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_20.setObjectName("lineEdit_0_20")
        self.lineEdit_3_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_20.setGeometry(QtCore.QRect(350, 460, 41, 40))
        self.lineEdit_3_20.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_20.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_20.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_20.setObjectName("lineEdit_3_20")
        self.lineEdit_1_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_21.setGeometry(QtCore.QRect(390, 380, 41, 40))
        self.lineEdit_1_21.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_21.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_21.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_21.setObjectName("lineEdit_1_21")
        self.lineEdit_0_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_21.setGeometry(QtCore.QRect(390, 340, 41, 40))
        self.lineEdit_0_21.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_21.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_21.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_21.setObjectName("lineEdit_0_21")
        self.lineEdit_2_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_21.setGeometry(QtCore.QRect(390, 420, 41, 40))
        self.lineEdit_2_21.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_21.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_21.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_21.setObjectName("lineEdit_2_21")
        self.lineEdit_3_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_21.setGeometry(QtCore.QRect(390, 460, 41, 40))
        self.lineEdit_3_21.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_21.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_21.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_21.setObjectName("lineEdit_3_21")
        self.lineEdit_2_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_22.setGeometry(QtCore.QRect(430, 420, 41, 40))
        self.lineEdit_2_22.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_22.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_22.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_22.setObjectName("lineEdit_2_22")
        self.lineEdit_3_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_22.setGeometry(QtCore.QRect(430, 460, 41, 40))
        self.lineEdit_3_22.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_22.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_22.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_22.setObjectName("lineEdit_3_22")
        self.lineEdit_0_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_22.setGeometry(QtCore.QRect(430, 340, 41, 40))
        self.lineEdit_0_22.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_22.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_22.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_22.setObjectName("lineEdit_0_22")
        self.lineEdit_1_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_22.setGeometry(QtCore.QRect(430, 380, 41, 40))
        self.lineEdit_1_22.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_22.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_22.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_22.setObjectName("lineEdit_1_22")
        self.lineEdit_0_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_23.setGeometry(QtCore.QRect(470, 340, 41, 40))
        self.lineEdit_0_23.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_23.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_23.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_23.setObjectName("lineEdit_0_23")
        self.lineEdit_3_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_23.setGeometry(QtCore.QRect(470, 460, 41, 40))
        self.lineEdit_3_23.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_23.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_23.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_23.setObjectName("lineEdit_3_23")
        self.lineEdit_2_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_23.setGeometry(QtCore.QRect(470, 420, 41, 40))
        self.lineEdit_2_23.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_23.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_23.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_23.setObjectName("lineEdit_2_23")
        self.lineEdit_1_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_23.setGeometry(QtCore.QRect(470, 380, 41, 40))
        self.lineEdit_1_23.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_23.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_23.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_23.setObjectName("lineEdit_1_23")
        self.lineEdit_0_24 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_24.setGeometry(QtCore.QRect(510, 340, 41, 40))
        self.lineEdit_0_24.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_24.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_24.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_24.setObjectName("lineEdit_0_24")
        self.lineEdit_3_24 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_24.setGeometry(QtCore.QRect(510, 460, 41, 40))
        self.lineEdit_3_24.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_24.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_24.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_24.setObjectName("lineEdit_3_24")
        self.lineEdit_1_24 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_24.setGeometry(QtCore.QRect(510, 380, 41, 40))
        self.lineEdit_1_24.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_24.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_24.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_24.setObjectName("lineEdit_1_24")
        self.lineEdit_2_24 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_24.setGeometry(QtCore.QRect(510, 420, 41, 40))
        self.lineEdit_2_24.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_24.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_24.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_24.setObjectName("lineEdit_2_24")
        self.lineEdit_3_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_25.setGeometry(QtCore.QRect(550, 460, 41, 40))
        self.lineEdit_3_25.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_25.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_25.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_25.setObjectName("lineEdit_3_25")
        self.lineEdit_2_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_25.setGeometry(QtCore.QRect(550, 420, 41, 40))
        self.lineEdit_2_25.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_25.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_25.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_25.setObjectName("lineEdit_2_25")
        self.lineEdit_0_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_25.setGeometry(QtCore.QRect(550, 340, 41, 40))
        self.lineEdit_0_25.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_25.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_25.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_25.setObjectName("lineEdit_0_25")
        self.lineEdit_1_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_25.setGeometry(QtCore.QRect(550, 380, 41, 40))
        self.lineEdit_1_25.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_25.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_25.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_25.setObjectName("lineEdit_1_25")
        self.lineEdit_3_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_26.setGeometry(QtCore.QRect(590, 460, 41, 40))
        self.lineEdit_3_26.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_26.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_26.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_26.setObjectName("lineEdit_3_26")
        self.lineEdit_1_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_26.setGeometry(QtCore.QRect(590, 380, 41, 40))
        self.lineEdit_1_26.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_26.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_26.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_26.setObjectName("lineEdit_1_26")
        self.lineEdit_0_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_26.setGeometry(QtCore.QRect(590, 340, 41, 40))
        self.lineEdit_0_26.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_26.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_26.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_26.setObjectName("lineEdit_0_26")
        self.lineEdit_2_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_26.setGeometry(QtCore.QRect(590, 420, 41, 40))
        self.lineEdit_2_26.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_26.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_26.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_26.setObjectName("lineEdit_2_26")
        self.lineEdit_3_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_27.setGeometry(QtCore.QRect(630, 460, 41, 40))
        self.lineEdit_3_27.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_27.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_27.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_27.setObjectName("lineEdit_3_27")
        self.lineEdit_0_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_27.setGeometry(QtCore.QRect(630, 340, 41, 40))
        self.lineEdit_0_27.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_27.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_27.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_27.setObjectName("lineEdit_0_27")
        self.lineEdit_2_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_27.setGeometry(QtCore.QRect(630, 420, 41, 40))
        self.lineEdit_2_27.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_27.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_27.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_27.setObjectName("lineEdit_2_27")
        self.lineEdit_1_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_27.setGeometry(QtCore.QRect(630, 380, 41, 40))
        self.lineEdit_1_27.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_27.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_27.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_27.setObjectName("lineEdit_1_27")
        self.lineEdit_0_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_28.setGeometry(QtCore.QRect(670, 340, 41, 40))
        self.lineEdit_0_28.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_28.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_28.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_28.setObjectName("lineEdit_0_28")
        self.lineEdit_1_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_28.setGeometry(QtCore.QRect(670, 380, 41, 40))
        self.lineEdit_1_28.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_28.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_28.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_28.setObjectName("lineEdit_1_28")
        self.lineEdit_2_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_28.setGeometry(QtCore.QRect(670, 420, 41, 40))
        self.lineEdit_2_28.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_28.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_28.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_28.setObjectName("lineEdit_2_28")
        self.lineEdit_3_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_28.setGeometry(QtCore.QRect(670, 460, 41, 40))
        self.lineEdit_3_28.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_28.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_28.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_28.setObjectName("lineEdit_3_28")
        self.lineEdit_2_29 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_29.setGeometry(QtCore.QRect(710, 420, 41, 40))
        self.lineEdit_2_29.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2_29.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2_29.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_2_29.setObjectName("lineEdit_2_29")
        self.lineEdit_0_29 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_0_29.setGeometry(QtCore.QRect(710, 340, 41, 40))
        self.lineEdit_0_29.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_0_29.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_0_29.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_0_29.setObjectName("lineEdit_0_29")
        self.lineEdit_1_29 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1_29.setGeometry(QtCore.QRect(710, 380, 41, 40))
        self.lineEdit_1_29.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_1_29.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_1_29.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_1_29.setObjectName("lineEdit_1_29")
        self.lineEdit_3_29 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_29.setGeometry(QtCore.QRect(710, 460, 41, 40))
        self.lineEdit_3_29.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3_29.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3_29.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:0px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_3_29.setObjectName("lineEdit_3_29")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(71, 425, 65, 27))
        self.label_5.setStyleSheet("font: 57 9pt \"Likhan\";")
        self.label_5.setObjectName("label_5")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(70, 410, 80, 21))
        self.line_5.setMinimumSize(QtCore.QSize(80, 0))
        self.line_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 340, 39, 27))
        self.label_6.setStyleSheet("font: 57 9pt \"Likhan\";")
        self.label_6.setObjectName("label_6")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(70, 370, 80, 21))
        self.line_6.setMinimumSize(QtCore.QSize(80, 0))
        self.line_6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(70, 460, 67, 40))
        self.label_7.setMinimumSize(QtCore.QSize(0, 40))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_7.setStyleSheet("font: 57 9pt \"Likhan\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(70, 383, 43, 27))
        self.label_8.setStyleSheet("font: 57 9pt \"Likhan\";")
        self.label_8.setObjectName("label_8")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(70, 450, 80, 21))
        self.line_7.setMinimumSize(QtCore.QSize(80, 0))
        self.line_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(190, 110, 3, 30))
        self.line_8.setMaximumSize(QtCore.QSize(40, 30))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(230, 110, 3, 30))
        self.line_9.setMaximumSize(QtCore.QSize(40, 30))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(270, 110, 3, 30))
        self.line_10.setMaximumSize(QtCore.QSize(40, 30))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.frame)
        self.line_11.setGeometry(QtCore.QRect(310, 110, 3, 30))
        self.line_11.setMaximumSize(QtCore.QSize(40, 30))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(390, 110, 3, 30))
        self.line_12.setMaximumSize(QtCore.QSize(40, 30))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame)
        self.line_13.setGeometry(QtCore.QRect(350, 110, 3, 30))
        self.line_13.setMaximumSize(QtCore.QSize(40, 30))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.frame)
        self.line_14.setGeometry(QtCore.QRect(430, 110, 3, 30))
        self.line_14.setMaximumSize(QtCore.QSize(40, 30))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.frame)
        self.line_15.setGeometry(QtCore.QRect(550, 110, 3, 30))
        self.line_15.setMaximumSize(QtCore.QSize(40, 30))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.frame)
        self.line_16.setGeometry(QtCore.QRect(510, 110, 3, 30))
        self.line_16.setMaximumSize(QtCore.QSize(40, 30))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.frame)
        self.line_17.setGeometry(QtCore.QRect(470, 110, 3, 30))
        self.line_17.setMaximumSize(QtCore.QSize(40, 30))
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.frame)
        self.line_18.setGeometry(QtCore.QRect(630, 110, 3, 30))
        self.line_18.setMaximumSize(QtCore.QSize(40, 30))
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.frame)
        self.line_19.setGeometry(QtCore.QRect(590, 110, 3, 30))
        self.line_19.setMaximumSize(QtCore.QSize(40, 30))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.frame)
        self.line_20.setGeometry(QtCore.QRect(670, 110, 3, 30))
        self.line_20.setMaximumSize(QtCore.QSize(40, 30))
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.frame)
        self.line_21.setGeometry(QtCore.QRect(710, 110, 3, 30))
        self.line_21.setMaximumSize(QtCore.QSize(40, 30))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.frame)
        self.line_22.setGeometry(QtCore.QRect(750, 110, 3, 30))
        self.line_22.setMaximumSize(QtCore.QSize(40, 30))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.frame)
        self.line_23.setGeometry(QtCore.QRect(750, 310, 3, 30))
        self.line_23.setMaximumSize(QtCore.QSize(40, 30))
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.frame)
        self.line_24.setGeometry(QtCore.QRect(430, 310, 3, 30))
        self.line_24.setMaximumSize(QtCore.QSize(40, 30))
        self.line_24.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_25 = QtWidgets.QFrame(self.frame)
        self.line_25.setGeometry(QtCore.QRect(310, 310, 3, 30))
        self.line_25.setMaximumSize(QtCore.QSize(40, 30))
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.frame)
        self.line_26.setGeometry(QtCore.QRect(470, 310, 3, 30))
        self.line_26.setMaximumSize(QtCore.QSize(40, 30))
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.frame)
        self.line_27.setGeometry(QtCore.QRect(670, 310, 3, 30))
        self.line_27.setMaximumSize(QtCore.QSize(40, 30))
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.frame)
        self.line_28.setGeometry(QtCore.QRect(630, 310, 3, 30))
        self.line_28.setMaximumSize(QtCore.QSize(40, 30))
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.frame)
        self.line_29.setGeometry(QtCore.QRect(510, 310, 3, 30))
        self.line_29.setMaximumSize(QtCore.QSize(40, 30))
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(self.frame)
        self.line_30.setGeometry(QtCore.QRect(190, 310, 3, 30))
        self.line_30.setMaximumSize(QtCore.QSize(40, 30))
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(self.frame)
        self.line_31.setGeometry(QtCore.QRect(270, 310, 3, 30))
        self.line_31.setMaximumSize(QtCore.QSize(40, 30))
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.line_32 = QtWidgets.QFrame(self.frame)
        self.line_32.setGeometry(QtCore.QRect(230, 310, 3, 30))
        self.line_32.setMaximumSize(QtCore.QSize(40, 30))
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.line_33 = QtWidgets.QFrame(self.frame)
        self.line_33.setGeometry(QtCore.QRect(550, 310, 3, 30))
        self.line_33.setMaximumSize(QtCore.QSize(40, 30))
        self.line_33.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.line_34 = QtWidgets.QFrame(self.frame)
        self.line_34.setGeometry(QtCore.QRect(390, 310, 3, 30))
        self.line_34.setMaximumSize(QtCore.QSize(40, 30))
        self.line_34.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setObjectName("line_34")
        self.line_35 = QtWidgets.QFrame(self.frame)
        self.line_35.setGeometry(QtCore.QRect(710, 310, 3, 30))
        self.line_35.setMaximumSize(QtCore.QSize(40, 30))
        self.line_35.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.line_36 = QtWidgets.QFrame(self.frame)
        self.line_36.setGeometry(QtCore.QRect(350, 310, 3, 30))
        self.line_36.setMaximumSize(QtCore.QSize(40, 30))
        self.line_36.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setObjectName("line_36")
        self.line_37 = QtWidgets.QFrame(self.frame)
        self.line_37.setGeometry(QtCore.QRect(590, 310, 3, 30))
        self.line_37.setMaximumSize(QtCore.QSize(40, 30))
        self.line_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.line_38 = QtWidgets.QFrame(self.frame)
        self.line_38.setGeometry(QtCore.QRect(70, 290, 80, 21))
        self.line_38.setMinimumSize(QtCore.QSize(80, 0))
        self.line_38.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(self.frame)
        self.line_39.setGeometry(QtCore.QRect(70, 490, 80, 21))
        self.line_39.setMinimumSize(QtCore.QSize(80, 0))
        self.line_39.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(self.frame)
        self.line_40.setGeometry(QtCore.QRect(70, 330, 80, 16))
        self.line_40.setMinimumSize(QtCore.QSize(80, 0))
        self.line_40.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.line_41 = QtWidgets.QFrame(self.frame)
        self.line_41.setGeometry(QtCore.QRect(70, 130, 80, 21))
        self.line_41.setMinimumSize(QtCore.QSize(80, 0))
        self.line_41.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.line_42 = QtWidgets.QFrame(self.frame)
        self.line_42.setGeometry(QtCore.QRect(150, 310, 3, 30))
        self.line_42.setMaximumSize(QtCore.QSize(40, 30))
        self.line_42.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.line_43 = QtWidgets.QFrame(self.frame)
        self.line_43.setGeometry(QtCore.QRect(150, 110, 3, 30))
        self.line_43.setMaximumSize(QtCore.QSize(40, 30))
        self.line_43.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_43.setObjectName("line_43")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(160, 110, 21, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(200, 110, 21, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(240, 110, 21, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(280, 110, 21, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(360, 110, 21, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(400, 110, 21, 21))
        self.label_14.setObjectName("label_14")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(440, 110, 21, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(320, 110, 21, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(480, 110, 21, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(680, 110, 21, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(720, 110, 21, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(520, 110, 21, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(560, 110, 21, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(640, 110, 21, 21))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(600, 110, 21, 21))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(680, 310, 21, 21))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(720, 310, 21, 21))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(200, 310, 21, 21))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(520, 310, 21, 21))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(560, 310, 21, 21))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(400, 310, 21, 21))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(480, 310, 21, 21))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(440, 310, 21, 21))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(640, 310, 21, 21))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(240, 310, 21, 21))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(280, 310, 21, 21))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(160, 310, 21, 21))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame)
        self.label_40.setGeometry(QtCore.QRect(600, 310, 21, 21))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame)
        self.label_41.setGeometry(QtCore.QRect(360, 310, 21, 21))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame)
        self.label_42.setGeometry(QtCore.QRect(320, 310, 21, 21))
        self.label_42.setObjectName("label_42")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(70, 250, 80, 21))
        self.line_3.setMinimumSize(QtCore.QSize(80, 0))
        self.line_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(71, 225, 65, 27))
        self.label_3.setStyleSheet("font: 57 9pt \"Likhan\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 183, 43, 27))
        self.label_2.setStyleSheet("font: 57 9pt \"Likhan\";")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 140, 39, 27))
        self.label.setStyleSheet("font: 57 9pt \"Likhan\";")
        self.label.setObjectName("label")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(70, 170, 80, 21))
        self.line_4.setMinimumSize(QtCore.QSize(80, 0))
        self.line_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(70, 210, 80, 21))
        self.line_2.setMinimumSize(QtCore.QSize(80, 0))
        self.line_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 260, 67, 31))
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"padding:0px;\n"
"margin:0px;\n"
"font: 57 9pt \"Likhan\";\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.line_44 = QtWidgets.QFrame(self.frame)
        self.line_44.setWindowModality(QtCore.Qt.NonModal)
        self.line_44.setGeometry(QtCore.QRect(20, 530, 771, 2))
        self.line_44.setMinimumSize(QtCore.QSize(80, 0))
        self.line_44.setMaximumSize(QtCore.QSize(800, 2))
        self.line_44.setStyleSheet("color:yellow")
        self.line_44.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setObjectName("line_44")
        oylikin.setCentralWidget(self.centralwidget)

        self.retranslateUi(oylikin)
        QtCore.QMetaObject.connectSlotsByName(oylikin)

    def retranslateUi(self, oylikin):
        _translate = QtCore.QCoreApplication.translate
        oylikin.setWindowTitle(_translate("oylikin", "Oylik ma\'limolarni kiritish"))
        self.label_15.setText(_translate("oylikin", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#5cb333;\">30 kunlik ma\'lumotlarni kiritish</span></p></body></html>"))
        self.label_16.setText(_translate("oylikin", "<html><head/><body><p><span style=\" color:#ff0000;\">Qo\'shimcha: </span>1- ustunga birinchi kun ma`lumotlari, 2-ustunga ikkinchi kun ma`lumotlari kiritiladi va hk.</p></body></html>"))
        self.pushbtn_gohome.setText(_translate("oylikin", "Bosh sahifa"))
        self.pushbtn_goback.setText(_translate("oylikin", "orqaga"))
        self.pushbtn_save.setText(_translate("oylikin", "Kiritish"))
        self.pushbtn_gobalance.setText(_translate("oylikin", "Suv balansi"))
        self.dateTimeEdit.setToolTip(_translate("oylikin", "<html><head/><body><p>kiritilgan sanadan boshlab 30 kun hisoblaydi</p></body></html>"))
        self.dateTimeEdit.setDisplayFormat(_translate("oylikin", "d/M/yy h:mm"))
        self.label_18.setToolTip(_translate("oylikin", "<html><head/><body><p>kiritilgan sanadan boshlab 10 kun hisoblaydi</p></body></html>"))
        self.label_18.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Sana:</span></p></body></html>"))
        self.label_5.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Qurshab</span></p></body></html>"))
        self.label_6.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Qora</span></p></body></html>"))
        self.label_7.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Yomg`ir</span></p></body></html>"))
        self.label_8.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Yassi</span></p></body></html>"))
        self.label_9.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">1</p></body></html>"))
        self.label_10.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">2</p></body></html>"))
        self.label_11.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">3</p></body></html>"))
        self.label_12.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">4</p></body></html>"))
        self.label_13.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">6</p></body></html>"))
        self.label_14.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">7</p></body></html>"))
        self.label_19.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">8</p></body></html>"))
        self.label_20.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_21.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">9</p></body></html>"))
        self.label_22.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">14</p></body></html>"))
        self.label_23.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">15</p></body></html>"))
        self.label_24.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">10</p></body></html>"))
        self.label_25.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">11</p></body></html>"))
        self.label_26.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">13</p></body></html>"))
        self.label_27.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">12</p></body></html>"))
        self.label_28.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">29</p></body></html>"))
        self.label_29.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">30</p></body></html>"))
        self.label_30.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">17</p></body></html>"))
        self.label_31.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">25</p></body></html>"))
        self.label_32.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">26</p></body></html>"))
        self.label_33.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">22</p></body></html>"))
        self.label_34.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">24</p></body></html>"))
        self.label_35.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">23</p></body></html>"))
        self.label_36.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">28</p></body></html>"))
        self.label_37.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">18</p></body></html>"))
        self.label_38.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">19</p></body></html>"))
        self.label_39.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">16</p></body></html>"))
        self.label_40.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">27</p></body></html>"))
        self.label_41.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">21</p></body></html>"))
        self.label_42.setText(_translate("oylikin", "<html><head/><body><p align=\"center\">20</p></body></html>"))
        self.label_3.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Qurshab</span></p></body></html>"))
        self.label_2.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Yassi</span></p></body></html>"))
        self.label.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Qora</span></p></body></html>"))
        self.label_4.setText(_translate("oylikin", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Yomg`ir</span></p></body></html>"))
