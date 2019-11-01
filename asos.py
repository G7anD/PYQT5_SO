from PyQt5 import QtCore, QtWidgets
import pandas as pd
import numpy as np
import pyqtgraph as pg
from classes.Balance import *
from classes.wInput import *
from classes.wOut import *
from classes.Main import *
from classes.core import *
from classes.graphClass import  *
from classes.loyqaClass import *
from classes.disGraph import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.startMainpg()

    def startMainpg(self):
        self.ui = main_pg()
        self.ui.setupUi(self)
        self.ui.pushbtn_balans.clicked.connect(self.waterbalans)
        self.ui.pushbtn_loyqa.clicked.connect(self.loyqa)
        self.ui.pushbtn_disgraf.clicked.connect(self.disGraph)
        self.ui.pushbtn_info.clicked.connect(self.info)

# suv muvozanati boshlanishi
    def info(self):
        self.Dia = QtWidgets.QDialog()
        self.ui = Ui_DiaInfo()
        self.ui.setupUi(self.Dia)
        self.Dia.show()

    def waterbalans(self):
        self.ui = waterbalans()
        self.ui.setupUi(self)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_kiruvchi.clicked.connect(self.wkiruvchi)
        self.ui.pushbtn_chiquvchi.clicked.connect(self.outer_main)
        self.ui.pushbtn_suv_balansi.clicked.connect(self.balance_main)

# kiruvchi suvlar boshlanishi

    def wkiruvchi(self):
        self.ui = w_input_main()
        self.ui.setupUi(self)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.comboBox_intanlov3.activated[str].connect(self.tanlovin)

    def kunlikin(self):
        self.ui = Ui_daily()
        self.ui.setupUi(self)

        # progress
        def apply_all(bl, ost=self.ui):
            tab = makeTable('kiruvchi suvlar xisoboti', 'kun', ost)
            tab.modificate()
            tab.makeDir()
            tab.export_to_excel()
            QtWidgets.QMessageBox.about(self, "Saqlandi", "Ma`lumotlarni saqlash muvofaqiyatli amalga oshirildi!")

        # buttons
        self.ui.pushbtn_save.clicked.connect(apply_all)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.wkiruvchi)

    def onkunlikin(self):
        self.ui = Ui_tenDay()
        self.ui.setupUi(self)
        # progress

        def apply_all(bl, ost=self.ui):
            tab = makeTable('kiruvchi suvlar xisoboti', 'on', ost)
            tab.modificate()
            tab.makeDir()
            tab.export_to_excel()
            QtWidgets.QMessageBox.about(self, "Saqlandi", "Ma`lumotlarni saqlash muvofaqiyatli amalga oshirildi!")
        # buttons
        self.ui.pushbtn_save.clicked.connect(apply_all)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.wkiruvchi)

    def oylikin(self):
        self.ui = Ui_monthly()
        self.ui.setupUi(self)
        # progress

        def apply_all(bl, ost=self.ui):
            tab = makeTable('kiruvchi suvlar xisoboti', 'oy', ost)
            tab.modificate()
            tab.makeDir()
            tab.export_to_excel()
            QtWidgets.QMessageBox.about(self, "Saqlandi", "Ma`lumotlarni saqlash muvofaqiyatli amalga oshirildi!")
        # buttons
        self.ui.pushbtn_save.clicked.connect(apply_all)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.wkiruvchi)

# kiruvchi suvlar end
# chiquvchi suvlar start
    def outer_main(self):
        self.ui = Ui_outerWater()
        self.ui.setupUi(self)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.comboBox_outanlov3.activated[str].connect(self.tanlovou)

    def kunlikou(self):
        self.ui = Ui_ouDaily()
        self.ui.setupUi(self)
        # progress
        def apply_all(bl,ost=self.ui):
            tab = makeTable('chiquvchi suvlar xisoboti', 'kun', ost)
            if tab.checker_pl()==1:
                tab.modificate()
                tab.makeDir()
                tab.export_to_excel()
                QtWidgets.QMessageBox.about(self, "Saqlandi", "Ma`lumotlarni saqlash muvofaqiyatli amalga oshirildi!")
            else:
                QtWidgets.QMessageBox.about(self, "Xatolik!!!", tab.checker_pl())

        # buttons
        self.ui.pushbtn_save.clicked.connect(apply_all)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.outer_main)

    def onkunlikou(self):
        self.ui = Ui_onkunlikou()
        self.ui.setupUi(self)
        # progress

        def apply_all(bl,ost=self.ui):
            tab = makeTable('chiquvchi suvlar xisoboti', 'on', ost)
            if tab.checker_pl()==1:
                tab.modificate()
                tab.makeDir()
                tab.export_to_excel()
                QtWidgets.QMessageBox.about(self, "Saqlandi", "Ma`lumotlarni saqlash muvofaqiyatli amalga oshirildi!")
            else:
                QtWidgets.QMessageBox.about(self, "Xatolik!!!", tab.checker_pl())

        # buttons
        self.ui.pushbtn_save.clicked.connect(apply_all)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.outer_main)

    def oylikou(self):
        self.ui = Ui_oylikou()
        self.ui.setupUi(self)
        # progress

        def apply_all(bl,ost=self.ui):
            tab = makeTable('chiquvchi suvlar xisoboti', 'oy', ost)
            if tab.checker_pl()==1:
                tab.modificate()
                tab.makeDir()
                tab.export_to_excel()
                QtWidgets.QMessageBox.about(self, "Saqlandi", "Ma`lumotlarni saqlash muvofaqiyatli amalga oshirildi!")
            else:
                QtWidgets.QMessageBox.about(self, "Xatolik!!!", tab.checker_pl())

        # buttons
        self.ui.pushbtn_save.clicked.connect(apply_all)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.outer_main)

# suv balansi start

    def balance_main(self):
        self.ui = Ui_balance_main()
        self.ui.setupUi(self)
        self.ui.pushbtn_bug.clicked.connect(self.plot_data)
        self.ui.pushbtn_fitr.clicked.connect(self.filtr)
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_blnc.clicked.connect(self.report)

    def report(self):
        self.ui = Ui_getReport()
        self.ui.setupUi(self)
        #progress
        mk = makeReport(self.ui,1)
        mk.setDate()


        def setDate(bl,ost = self.ui,osst = mk):
            mk.setInterval(ost.comboBox_date.currentText())

        def setInterval(bl,ost=self.ui,osst = mk):
            mk.setData(ost.comboBox_interval.currentText())
        def print_data(bl):
            url = '/chiquvchi_suvlar_xisoboti.xlsx'
            printer = os.system("lpr -P "+url)
            QtWidgets.QMessageBox.about(self, "Xatolik!!!", "Printer bilan bog`liq muammo yuz berdi!!!")

        #comboBox changed
        self.ui.pushbtn_print.clicked.connect(print_data)
        self.ui.comboBox_date.activated.connect(setDate)
        self.ui.comboBox_interval.activated.connect(setInterval)

        #button
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.balance_main)

    def plot_data(self):
        self.ui = Ui_getGraph()
        self.ui.setupUi(self)
        mk = makeReport(self.ui,2)
        mk.setDate()
        self.ui.label_2.setPixmap(QtGui.QPixmap(""))

        def prg_bar(ost=self.ui):
            ost.progressBar.show()
            completed = 0
            while completed < 100:
                completed += 0.001
                ost.progressBar.setValue(completed)

        def setDate(bl,ost = self.ui,osst = mk):
            mk.setInterval(ost.comboBox_date.currentText())

        def setInterval(bl,ost=self.ui,osst = mk):
            prg_bar()
            mk.setData(ost.comboBox_interval.currentText())

        #comboBox changed
        self.ui.comboBox_date.activated.connect(setDate)
        self.ui.comboBox_interval.activated.connect(setInterval)
        #button
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.balance_main)

    def filtr(self):
        self.ui = Ui_filtr()
        self.ui.setupUi(self)
        mk = makeReport(self.ui,3)
        mk.setDate()
        self.ui.label_2.setPixmap(QtGui.QPixmap(""))

        def prg_bar(ost=self.ui):
            ost.progressBar.show()
            completed = 0
            while completed < 100:
                completed += 0.001
                ost.progressBar.setValue(completed)

        def setDate(bl,ost = self.ui,osst = mk):
            mk.setInterval(ost.comboBox_date.currentText())

        def setInterval(bl,ost=self.ui,osst = mk):
            prg_bar()
            mk.setData(ost.comboBox_interval.currentText())

        #comboBox changed
        self.ui.comboBox_date.activated.connect(setDate)
        self.ui.comboBox_interval.activated.connect(setInterval)
        #button
        self.ui.pushbtn_gohome.clicked.connect(self.startMainpg)
        self.ui.pushbtn_gobalance.clicked.connect(self.waterbalans)
        self.ui.pushbtn_goback.clicked.connect(self.balance_main)
    def loyqa(self):
        tek = os.listdir().count("db")
        if tek!=0:
            self.ui = Ui_loyqa_hajmi()
            self.ui.setupUi(self)
            self.ui.progressBar.hide()
            def setDate(ost=self.ui):
                dates = []
                for i in os.listdir("db/"):
                    if os.listdir('db/'+i+"/").count('oylik') !=0:
                        dates.append(i[5:])
                ost.comboBox.addItems(dates)
                if len(dates)!=0:
                    self.ui.url = "db/data_"+dates[-1]+"/oylik/"
                    self.ui.data_in = pd.read_excel(self.ui.url+"kiruvchi suvlar xisoboti.xlsx")
                    self.ui.data_ou = pd.read_excel(self.ui.url+"chiquvchi suvlar xisoboti.xlsx")
                else:
                 QtWidgets.QMessageBox.about(self, "Xatolik!!!", "Oylik ma`lumotlar kiritilmagan")
            setDate()

            def pointer(ost=self.ui):
                date = self.ui.comboBox.currentText()
                self.ui.url = "db/data_"+date+"/oylik/"
            def apply_all(bl,ost=self.ui):
                data_in = self.ui.data_in
                data_ou = self.ui.data_ou

                sum_in = data_in.sum().sum()
                sum_ou = data_ou.sum().sum()
                if ost.lineEdit == '' or ost.lineEdit_2 == '':
                    QtWidgets.QMessageBox.about(self, "Xatolik!!!", "Avval barcha maydonlarni to`ldiring!")
                else:
                    lh = int(ost.lineEdit.text()) # loyihaviy hajmi
                    oh = int(ost.lineEdit_2.text()) # oqim hajmi
                    uh = lh-(sum_in-sum_ou) # olik hajmi
                    te = 0.012*pow(oh,0.785) # tekislovchi(emperik formula)
                    toliq = uh + te
                    toliq = round(toliq,2)
                    ost.lcdNumber.display(toliq)

            self.ui.comboBox.activated.connect(pointer)

            self.ui.pushButton.clicked.connect(apply_all)
            self.ui.pushButton_2.clicked.connect(self.startMainpg)
        else:
            QtWidgets.QMessageBox.about(self, "Xatolik!!!", "Oylik ma`lumotlar kiritilmagan")



    def disGraph(self):
        self.ui = Ui_DisGraf()
        self.ui.setupUi(self)
        def setDate(ost=self.ui):
            dates = []
            for i in os.listdir("db/"):
                if os.listdir('db/'+i).count('oylik') !=0:
                    dates.append(i[5:])
            ost.comboBox.addItems(dates)
            if len(dates)!=0:
                self.ui.url = "db/data_"+dates[-1]+"/oylik/"
                self.ui.data_in = pd.read_excel(self.ui.url+"kiruvchi suvlar xisoboti.xlsx")
                self.ui.data_ou = pd.read_excel(self.ui.url+"chiquvchi suvlar xisoboti.xlsx")
            else:
             QtWidgets.QMessageBox.about(self, "Xatolik!!!", "Oylik ma`lumotlar kiritilmagan")
        setDate()


        def pointer(bl,ost=self.ui):
            date = self.ui.comboBox.currentText()
            ost.url = "db/data_"+date+"/oylik/"
            ost.suv_sathi1 = [871,874,871,878,881,879,868,854,857,847,846,856]
            ost.suv_sathi2 = [641,834,873,848,851,849,888,874,865,857,886,846]
            ost.suv_osti1 = [442,615,550,654,645,614,580,536,682,560,721,624]
            ost.suv_osti2 = [615,543,550,742,369,754,455,234,243,559,290,779]
            ost.suv_sathi1, self.ui.suv_sathi2 = self.ui.suv_sathi2, self.ui.suv_sathi1
            datalst_lst = []

            for i in range(12):
                datalst_lst.append([ost.suv_sathi1[i],ost.suv_osti1[i]])
            data_lst = pd.DataFrame(datalst_lst,columns=['Suv sathi belgisi','Suv sathi belgisi past'],index = range(1,13))
            data_lst.plot.line()

            plt.savefig('img/disgraf/stat.png')

            ost.label_2.setPixmap(QtGui.QPixmap("img/disgraf/stat.png"))

        self.ui.comboBox.activated.connect(pointer)

        self.ui.pushButton.clicked.connect(self.startMainpg)
# funksiyalar
    def tanlovin(self, text):
        if text == "Kunlik":
            self.kunlikin()
        elif text == "10 Kunlik":
            self.onkunlikin()
        else:
            self.oylikin()

    def tanlovou(self, text):
        if text == "Kunlik":
            self.kunlikou()
        elif text == "10 Kunlik":
            self.onkunlikou()
        else:
            self.oylikou()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
