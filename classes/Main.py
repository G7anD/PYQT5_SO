from PyQt5 import QtCore, QtGui, QtWidgets

#main page
class main_pg(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(70, 130, 671, 16))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_sarlavha = QtWidgets.QLabel(self.frame)
        self.label_sarlavha.setGeometry(QtCore.QRect(180, 80, 441, 51))
        self.label_sarlavha.setStyleSheet("font: 75 18pt \"Norasi\";")
        self.label_sarlavha.setObjectName("label_sarlavha")
        self.pushbtn_info = QtWidgets.QPushButton(self.frame)
        self.pushbtn_info.setGeometry(QtCore.QRect(690, 90, 41, 41))
        self.pushbtn_info.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:20px;\n"
"background-color: rgb(212, 245, 254);\n"
"}")
        self.pushbtn_info.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_info.setIcon(icon1)
        self.pushbtn_info.setIconSize(QtCore.QSize(32, 32))
        self.pushbtn_info.setObjectName("pushbtn_info")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 190, 601, 254))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushbtn_balans = QtWidgets.QPushButton(self.layoutWidget)
        self.pushbtn_balans.setMinimumSize(QtCore.QSize(0, 80))
        self.pushbtn_balans.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(97, 184, 167);\n"
"color:#fff;\n"
"font-size:20px;\n"
"font-family: \"Manjari\";\n"
"text-align:left;\n"
"padding-left:30px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(111, 211, 191);\n"
"color:#fff;\n"
"font-size:18px;\n"
"font-family: \"Manjari\";\n"
"text-align:left;\n"
"padding-left:35px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/blns.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_balans.setIcon(icon2)
        self.pushbtn_balans.setIconSize(QtCore.QSize(48, 48))
        self.pushbtn_balans.setObjectName("pushbtn_balans")
        self.verticalLayout.addWidget(self.pushbtn_balans)
        self.pushbtn_loyqa = QtWidgets.QPushButton(self.layoutWidget)
        self.pushbtn_loyqa.setMinimumSize(QtCore.QSize(0, 80))
        self.pushbtn_loyqa.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(97, 184, 167);\n"
"color:#fff;\n"
"font-size:20px;\n"
"font-family: \"Manjari\";\n"
"text-align:left;\n"
"padding-left:30px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(111, 211, 191);\n"
"color:#fff;\n"
"font-size:18px;\n"
"font-family: \"Manjari\";\n"
"text-align:left;\n"
"padding-left:35px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/lyqh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_loyqa.setIcon(icon3)
        self.pushbtn_loyqa.setIconSize(QtCore.QSize(48, 48))
        self.pushbtn_loyqa.setObjectName("pushbtn_loyqa")
        self.verticalLayout.addWidget(self.pushbtn_loyqa)
        self.pushbtn_disgraf = QtWidgets.QPushButton(self.layoutWidget)
        self.pushbtn_disgraf.setMinimumSize(QtCore.QSize(0, 80))
        self.pushbtn_disgraf.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(97, 184, 167);\n"
"color:#fff;\n"
"font-size:20px;\n"
"font-family: \"Manjari\";\n"
"text-align:left;\n"
"padding-left:30px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-radius:10px;\n"
"background-color: rgb(111, 211, 191);\n"
"color:#fff;\n"
"font-size:18px;\n"
"font-family: \"Manjari\";\n"
"text-align:left;\n"
"padding-left:35px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/dsgr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbtn_disgraf.setIcon(icon4)
        self.pushbtn_disgraf.setIconSize(QtCore.QSize(48, 48))
        self.pushbtn_disgraf.setObjectName("pushbtn_disgraf")
        self.verticalLayout.addWidget(self.pushbtn_disgraf)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_sarlavha.setBuddy(self.pushbtn_info)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bosh sahifa - Suv muvozanati"))
        self.label_sarlavha.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Suv omborining ish rejasi </span></p></body></html>"))
        self.pushbtn_balans.setText(_translate("MainWindow", "                            Suv muvozanati(balansi)"))
        self.pushbtn_loyqa.setText(_translate("MainWindow", "                            SOning loyqalangan hajmi"))
        self.pushbtn_disgraf.setText(_translate("MainWindow", "                             Dispatcherlik grafigi"))
class Ui_DiaInfo(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(441, 358)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, -10, 451, 371))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 421, 41))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(30, 80, 381, 211))
        self.textBrowser.setStyleSheet("QTextBrowser\n"
"{\n"
"border:2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius:20px;\n"
"padding:10px;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 310, 131, 31))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(0, 143, 0);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(0, 175, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dastur haqida"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#2f915d;\">Dastur haqida qisqacha!</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">&nbsp;Bu dastur suv omborining ish rejimini boshqarishga hamda nazariy jihatdan hisob kitoblarni amalga oshirish uchun amaliy yordam beradi.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">&nbsp;Dasturda suv muvozanatini hisobga olish, Suv omboridagi suvning loyqalangan hajmini aniqlash hamda dispatcherlik grafigini tuzish kabi ishlarni bajaradi.</span><span style=\" font-style:italic;\">(barchasi avtomatik tarzda amalga oshiriladi)</span><span style=\" font-size:11pt; font-style:italic;\">. </span></p>\n"
"</body></html>"))
        self.pushButton.setText(_translate("Dialog", "Yopish"))
