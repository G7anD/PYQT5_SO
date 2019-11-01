import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_getGraph(object):
    def setupUi(self, getGraph):
        getGraph.setObjectName("getGraph")
        getGraph.resize(800, 600)
        getGraph.setMinimumSize(QtCore.QSize(800, 600))
        getGraph.setMaximumSize(QtCore.QSize(800, 600))
        getGraph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(getGraph)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 941, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 361, 41))
        self.label.setStyleSheet("font: 9pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.comboBox_date = QtWidgets.QComboBox(self.frame)
        self.comboBox_date.setGeometry(QtCore.QRect(430, 30, 181, 41))
        self.comboBox_date.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"Foreground:    color: rgb(255, 255, 255);\n"
"FontSize:18px;\n"
"}")
        self.comboBox_date.setObjectName("comboBox_date")
        self.comboBox_interval = QtWidgets.QComboBox(self.frame)
        self.comboBox_interval.setGeometry(QtCore.QRect(620, 30, 171, 41))
        self.comboBox_interval.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"Foreground:    color: rgb(255, 255, 255);\n"
"FontSize:18px;\n"
"}")
        self.comboBox_interval.setObjectName("comboBox_interval")
        self.pushbtn_goback = QtWidgets.QPushButton(self.frame)
        self.pushbtn_goback.setGeometry(QtCore.QRect(270, 540, 111, 29))
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
        self.label_6.setGeometry(QtCore.QRect(20, 520, 901, 20))
        self.label_6.setObjectName("label_6")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
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
        self.pushbtn_gohome.setIcon(icon)
        self.pushbtn_gohome.setObjectName("pushbtn_gohome")
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.frame)
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 640, 480))
        self.label_2.setMinimumSize(QtCore.QSize(640, 480))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/graph_img/buglanish.png"))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(520, 540, 251, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2.raise_()
        self.label.raise_()
        self.comboBox_date.raise_()
        self.comboBox_interval.raise_()
        self.pushbtn_goback.raise_()
        self.label_6.raise_()
        self.pushbtn_gohome.raise_()
        self.pushbtn_gobalance.raise_()
        self.progressBar.raise_()
        getGraph.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(getGraph)
        self.statusBar.setObjectName("statusBar")
        getGraph.setStatusBar(self.statusBar)

        self.retranslateUi(getGraph)
        QtCore.QMetaObject.connectSlotsByName(getGraph)
        self.progressBar.hide()
    def retranslateUi(self, getGraph):
        _translate = QtCore.QCoreApplication.translate
        getGraph.setWindowTitle(_translate("getGraph", "Xisobotni olish"))
        self.label.setText(_translate("getGraph", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#00aa00;\">Bug\'lanishga sarf bo\'lgan suv!</span></p></body></html>"))
        self.pushbtn_goback.setText(_translate("getGraph", "orqaga"))
        self.label_6.setText(_translate("getGraph", "<html><head/><body><p><span style=\" color:#009400;\">_______________________________________________________________________________________________________________________________________________<br/></span></p></body></html>"))
        self.pushbtn_gohome.setText(_translate("getGraph", "Bosh sahifa"))
        self.pushbtn_gobalance.setText(_translate("getGraph", "Suv balansi"))
class Ui_filtr(object):
    def setupUi(self, getFiltr):
        getFiltr.setObjectName("getFiltr")
        getFiltr.resize(800, 600)
        getFiltr.setMinimumSize(QtCore.QSize(800, 600))
        getFiltr.setMaximumSize(QtCore.QSize(800, 600))
        getFiltr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(getFiltr)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 941, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 361, 41))
        self.label.setStyleSheet("font: 9pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.comboBox_date = QtWidgets.QComboBox(self.frame)
        self.comboBox_date.setGeometry(QtCore.QRect(430, 30, 181, 41))
        self.comboBox_date.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"Foreground:    color: rgb(255, 255, 255);\n"
"FontSize:18px;\n"
"}")
        self.comboBox_date.setObjectName("comboBox_date")
        self.comboBox_interval = QtWidgets.QComboBox(self.frame)
        self.comboBox_interval.setGeometry(QtCore.QRect(620, 30, 171, 41))
        self.comboBox_interval.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(85, 85, 255);\n"
"Foreground:    color: rgb(255, 255, 255);\n"
"FontSize:18px;\n"
"}")
        self.comboBox_interval.setObjectName("comboBox_interval")
        self.pushbtn_goback = QtWidgets.QPushButton(self.frame)
        self.pushbtn_goback.setGeometry(QtCore.QRect(270, 540, 111, 29))
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
        self.label_6.setGeometry(QtCore.QRect(20, 520, 901, 20))
        self.label_6.setObjectName("label_6")
        self.pushbtn_gohome = QtWidgets.QPushButton(self.frame)
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
        self.pushbtn_gohome.setIcon(icon)
        self.pushbtn_gohome.setObjectName("pushbtn_gohome")
        self.pushbtn_gobalance = QtWidgets.QPushButton(self.frame)
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 640, 480))
        self.label_2.setMinimumSize(QtCore.QSize(640, 480))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/graph_img/buglanish.png"))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(520, 540, 251, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2.raise_()
        self.label.raise_()
        self.comboBox_date.raise_()
        self.comboBox_interval.raise_()
        self.pushbtn_goback.raise_()
        self.label_6.raise_()
        self.pushbtn_gohome.raise_()
        self.pushbtn_gobalance.raise_()
        self.progressBar.raise_()
        getFiltr.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(getFiltr)
        self.statusBar.setObjectName("statusBar")
        getFiltr.setStatusBar(self.statusBar)

        self.retranslateUi(getFiltr)
        QtCore.QMetaObject.connectSlotsByName(getFiltr)
        self.progressBar.hide()
    def retranslateUi(self, getFiltr):
        _translate = QtCore.QCoreApplication.translate
        getFiltr.setWindowTitle(_translate("getFiltr", "Xisobotni olish"))
        self.label.setText(_translate("getFiltr", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#00aa00;\">Filtratsiyaga sarf bo\'lgan suv!</span></p></body></html>"))
        self.pushbtn_goback.setText(_translate("getFiltr", "orqaga"))
        self.label_6.setText(_translate("getFiltr", "<html><head/><body><p><span style=\" color:#009400;\">_______________________________________________________________________________________________________________________________________________<br/></span></p></body></html>"))
        self.pushbtn_gohome.setText(_translate("getFiltr", "Bosh sahifa"))
        self.pushbtn_gobalance.setText(_translate("getFiltr", "Suv balansi"))
