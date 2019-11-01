import pandas as pd
import os
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import datetime as dt
import matplotlib.pyplot as plt




class makeTable:
    def __init__(self, tableName, interval, ost):
        self.tableName = tableName
        self.interval = interval
        self.ost = ost
        self.checker = True
        self.knowner()
        self.makeDateTime()
        self.inde_x = []

    def knowner(self):

        if self.tableName.split()[0] == 'kiruvchi':
            self.column_s = ['Qora', 'Yassi', 'Qurshab', 'Yomgir']
            self.type = 'kir'

        else:
            self.type = 'chiq'
            self.column_s = ['Umumiy', 'Bug`lanish', 'Filtratsiyaga']

        if self.interval == 'kun':
            self.interval = 'kunlik'
        elif self.interval == 'on':
            self.interval = 'onkunlik'
            self.columns_count = 10
        elif self.interval == 'oy':
            self.interval = 'oylik'
            self.columns_count = 30

        else:
            self.checker = False

    def makeDateTime(self):
        self.allDate = self.ost.dateTimeEdit.dateTime().toPyDateTime()
        date = str(self.ost.dateTimeEdit.dateTime(
        ).toPyDateTime()).split()[0]
        time = str(self.ost.dateTimeEdit.dateTime(
        ).toPyDateTime()).split()[1][0:-3]
        date = date.split('-')
        date[0], date[2] = date[2], date[0]
        date = date[0]+'-'+date[1]+'-'+date[2]
        self.date = date
        self.time = time

    def checker_pl(self):
        url = 'db/data_{}'.format(self.date)
        if self.tableName.split()[0] == 'chiquvchi':
            name = self.tableName.replace('chiquvchi', 'kiruvchi')
        else:
            name = self.tableName.replace('kiruvchi', 'chiquvchi')
        if os.path.exists(url):
            if os.path.exists(url+'/'+self.interval):
                if os.path.exists(url+'/'+self.interval+'/'+name+'.xlsx'):
                    return 1
                else:
                    return 'Siz bu kun uchun kiruvchi suv ma`lumotlarini kiritmagansiz!'
            else:
                return 'Siz avval ' + self.interval + ' kiruvchi suv ma`lumotlarini kiritishingiz kerak!'
        else:
            return 'Siz avval kiruvchi suv ma`lumotlarini kiritishingiz kerak!'

    def makeDir(self):

        if self.checker:
            dta = 'db/data_{}'.format(self.date)

            def lister(url=''): return os.listdir(os.getcwd()+'/'+url)

            if lister().count('db') == 0:
                os.mkdir('db')

            if lister('db/').count(dta.replace('db/', '')) == 0:
                os.mkdir(dta)

            if lister(dta).count(self.interval) == 0:
                os.mkdir(dta+"/"+self.interval)
            if lister(dta+"/"+self.interval).count('backub') == 0:
                os.mkdir(dta+"/"+self.interval+"/backub")

    def export_to_excel(self):
        if self.interval == 'kunlik':
            self.inde_x = [self.date]
        elif self.interval == 'onkunlik':
            self.inde_x = [self.allDate.date() - dt.timedelta(days=x)
                           for x in range(0, 10)][::-1]
        elif self.interval == 'oylik':
            self.inde_x = [self.allDate.date() - dt.timedelta(days=x)
                           for x in range(0, 30)][::-1]
        # print(self.interval)
        url = 'db/data_{}'.format(self.date)+"/"+self.interval
        url_part1 = '/'+self.tableName+'.xlsx'
        url_part2 = '/backub'+'/' + \
            '{}-{}'.format(self.tableName, self.time)+'.xlsx'

        data = pd.DataFrame(self.data, columns=self.column_s,
                            index=self.inde_x)

        data.to_excel(url+url_part1, sheet_name=self.tableName)
        data.to_excel(url+url_part2, sheet_name=self.tableName)

    def modificate(self):
        self.rows_count = len(self.column_s)
        if self.interval == 'kunlik' and self.type == 'chiq':
            self.data = [[self.ost.lineEdit_umumiy.text(),
                          self.ost.lineEdit_buglanish.text(),
                          self.ost.lineEdit_filtratsiya.text()]]
        elif self.interval == 'kunlik' and self.type == 'kir':
            self.data = [[self.ost.lineEdit_qora.text(),
                          self.ost.lineEdit_yassi.text(),
                          self.ost.lineEdit_qurshab.text(),
                          self.ost.lineEdit_yomgir.text()]]
        else:
            self.data = []

            for i in range(self.columns_count):
                self.data.append([])

            for i in range(self.columns_count):
                for j in range(self.rows_count):
                    self.data[i].append(
                        eval('self.ost.lineEdit_{}_{}'.format(j, i)).text())

        # if self.interval == 'kunlik':
        #     gacha = 1
        # else:
        #     gacha = self.columns_count
        # for i in range(gacha):
        #     print(self.data[i], gacha)


class makeReport:
    def __init__(self, ost,types):
        self.ost = ost
        self.types = types

    def setDate(self):
        dates = []
        for i in os.listdir("db/"):
            dates.append(i[5:])
        self.ost.comboBox_date.addItems(dates)

    def setInterval(self, date):
        self.date = date
        self.ost.comboBox_interval.clear()
        listdir = os.listdir("db/"+"data_"+date)
        if 'kunlik' in listdir:
            listdir.remove('kunlik')
        self.ost.comboBox_interval.addItems(listdir)

    def setData(self, interval):
        self.interval = interval
        self.url = "db/data_"+self.date+"/"+self.interval
        if self.types == 1:
            self.makeDataFrame()
            self.sendToDisplay()
        elif self.types == 2:
            self.makePicture()
        elif self.types == 3:
            self.makeFilterPic()
    def makePicture(self):
        data_ou = pd.read_excel(self.url+'/chiquvchi suvlar xisoboti.xlsx')
        data_ou.plot(kind='line',x='Bug`lanish',y=data_ou.iloc[:,:1].columns,color='red')
        plt.savefig('img/graph_img/buglanish.png')

        self.ost.label_2.setPixmap(QtGui.QPixmap("img/graph_img/buglanish.png"))
    def makeFilterPic(self):
        data_ou = pd.read_excel(self.url+'/chiquvchi suvlar xisoboti.xlsx')
        data_ou.plot(kind='line',x='Filtratsiyaga',y=data_ou.iloc[:,:1].columns,color='red')
        plt.savefig('img/graph_img/buglanish1.png')

        self.ost.label_2.setPixmap(QtGui.QPixmap("img/graph_img/buglanish1.png"))
    def makeDataFrame(self):
        data_ou = pd.read_excel(self.url+'/chiquvchi suvlar xisoboti.xlsx')
        data_in = pd.read_excel(self.url+'/kiruvchi suvlar xisoboti.xlsx')
        yuqori = data_in.loc[:, ['Qora', 'Yassi', 'Qurshab']].sum().sum()
        yogin = data_in['Yomgir'].sum()

        self.summa = [self.date, str(yuqori+yogin), str(yuqori),
                      str(yogin), str(data_ou.sum().sum()), str(data_ou.sum()[1]),
                      str(data_ou.sum()[2]), str(data_ou.sum()[0]),str(yuqori+yogin-data_ou.sum().sum())]

    def sendToDisplay(self):
        self.ost.tableWidget.setItem(
            0, 0, QtWidgets.QTableWidgetItem(self.summa[0]))
        self.ost.tableWidget.setItem(
            0, 1, QtWidgets.QTableWidgetItem(self.summa[1]))
        self.ost.tableWidget.setItem(
            0, 2, QtWidgets.QTableWidgetItem(self.summa[2]))
        self.ost.tableWidget.setItem(
            0, 4, QtWidgets.QTableWidgetItem(self.summa[3]))
        self.ost.tableWidget.setItem(
            0, 8, QtWidgets.QTableWidgetItem(self.summa[4]))
        self.ost.tableWidget.setItem(
            0, 9, QtWidgets.QTableWidgetItem(self.summa[5]))
        self.ost.tableWidget.setItem(
            0, 10, QtWidgets.QTableWidgetItem(self.summa[6]))
        self.ost.tableWidget.setItem(
            0, 12, QtWidgets.QTableWidgetItem(self.summa[7]))
        self.ost.tableWidget.setItem(
            0, 20, QtWidgets.QTableWidgetItem(self.summa[8]))

    # def setGraph(self):




# if __name__ == "__main__":
#     ob = makeReport('someThing')
#     ob.knownDate()


# class setDisplay:
#     def __init__(self, tableName, data):
#         self.tableName = tableName
#     #     self.data =
#     # def tenDay(self, data):
#     #     se

#     def monthly(self):
#         pass
#     def sendToDisplay(self, data, parr):
#         self.data = data
#         parr.tableWidget.setItem(0, 0, QtableWidgetItem(self.data[0]))
#         parr.tableWidget.setItem(0, 1, QtableWidgetItem(self.data[0]))
#         parr.tableWidget.setItem(0, 2, QtableWidgetItem(self.data[0]))
#         parr.tableWidget.setItem(0, 4, QtableWidgetItem(self.data[0]))
#         parr.tableWidget.setItem(0, 8, QtableWidgetItem(self.data[0]))
#         parr.tableWidget.setItem(0, 9, QtableWidgetItem(self.data[0]))
#         parr.tableWidget.setItem(0, 10, QtableWidgetItem(self.data[0]))
#         parr.tableWidget.setItem(0, 12, QtableWidgetItem(self.data[0]))
