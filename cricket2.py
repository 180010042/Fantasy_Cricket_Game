# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from save_team import Ui_Dialog
from save_team2 import Ui_Dialog2
from save_team3 import Ui_Dialog3
from message import Ui_msg
from message2 import Ui_msg2

class Ui_MainWindow(object):
        
    def batsmen(self):
        self.l1.clear()
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM stats WHERE ctg = 'BAT';"
        cur.execute(sql)
        rec = cur.fetchall()
        total = 0
        for i in rec:
            self.l1.addItem('        {}'.format(i[1]))
            total=total+i[6]
        self.t2.setText("{}".format(total))

    def bowlers(self):
        self.l1.clear()
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM stats WHERE ctg = 'BOW';"
        cur.execute(sql)
        rec = cur.fetchall()
        total = 0
        for i in rec:
            self.l1.addItem('        {}'.format(i[1]))
            total=total+i[6]
        self.t2.setText("{}".format(total))
        
    def allrounders(self):
        self.l1.clear()
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM stats WHERE ctg = 'AR';"
        cur.execute(sql)
        rec = cur.fetchall()
        total = 0
        for i in rec:
            self.l1.addItem('        {}'.format(i[1]))            
            total=total+i[6]
        self.t2.setText("{}".format(total))
        
    def wicket_keepers(self):
        self.l1.clear()
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM stats WHERE ctg = 'WK';"
        cur.execute(sql)
        rec = cur.fetchall()
        total = 0
        for i in rec:
            self.l1.addItem('        {}'.format(i[1]))
            total=total+i[6]
        self.t2.setText("{}".format(total))

    def removelist1(self,item):
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM stats WHERE player_name = '{}';".format(item.text()[8:])
        cur.execute(sql)
        rec = cur.fetchone()
        if rec[7] == 'BAT':
            self.t4.setText("{}".format(int(self.t4.text()) + 1))
        elif rec[7] == 'BOW':
            self.t5.setText("{}".format(int(self.t5.text()) + 1))
        elif rec[7] == 'AR':
            self.t6.setText("{}".format(int(self.t6.text()) + 1))
        else:
            self.t7.setText("{}".format(int(self.t7.text()) + 1))
        if int(self.t7.text()) > 1:
            self.WK_popup()
            self.t7.setText("1")
        else:
            self.t2.setText("{}".format(int(self.t2.text())-rec[6]))
            self.t3.setText("{}".format(rec[6]+int(self.t3.text())))
            self.l1.takeItem(self.l1.row(item))
            self.l2.addItem(item.text())
            
    def removelist2(self,item):
        self.l2.takeItem(self.l2.row(item))
        self.l1.addItem(item.text())
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM stats WHERE player_name = '{}';".format(item.text()[8:])
        cur.execute(sql)
        rec = cur.fetchone()
        self.t3.setText("{}".format(int(self.t3.text())-rec[6]))
        self.t2.setText("{}".format(rec[6]+int(self.t2.text())))
        if rec[7] == 'BAT':
            self.t4.setText("{}".format(int(self.t4.text()) - 1))
        elif rec[7] == 'BOW':
            self.t5.setText("{}".format(int(self.t5.text()) - 1))
        elif rec[7] == 'AR':
            self.t6.setText("{}".format(int(self.t6.text()) - 1))
        else:
            self.t7.setText("{}".format(int(self.t7.text()) - 1))

    def WK_popup(self):
        self.msg = QtWidgets.QDialog()
        self.ui = Ui_msg()
        self.ui.setupUi(self.msg)
        self.msg.show()

    def save_team(self):
        from Lib import sqlite3
        Myteam = sqlite3.connect('cricket.db')
        cur = Myteam.cursor()
        items = []
        ids = ","
        for x in range(3,self.l2.count()-1):
            items.append(self.l2.item(x).text())
        for i in items:
            sql = "SELECT * FROM stats WHERE player_name = '{}';".format(i[8:])
            cur.execute(sql)
            rec = cur.fetchone()
            ids = ids+","+"{}".format(rec[0])
        sql2 = "UPDATE teams set players = '{}' WHERE team_name  = '{}';".format(ids, self.t1.text())
        cur.execute(sql2)
        Myteam.commit()
        self.msg = QtWidgets.QDialog()
        self.ui = Ui_msg2()
        self.ui.setupUi(self.msg)
        self.msg.show()
        

    def new_team(self):
        from Lib import sqlite3
        Myteam = sqlite3.connect('cricket.db')
        cur = Myteam.cursor()
        items = []
        ids = ","
        for x in range(3,self.l2.count()-1):
            items.append(self.l2.item(x).text())
        for i in items:
            sql = "SELECT * FROM stats WHERE player_name = '{}';".format(i[8:])
            cur.execute(sql)
            rec = cur.fetchone()
            ids = ids+","+"{}".format(rec[0])
        sql2 = "UPDATE teams set players = '{}' WHERE team_name  = '{}';".format(ids, self.t1.text())
        cur.execute(sql2)
        Myteam.commit()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        

    def evaluate_team(self):
        from Lib import sqlite3
        Myteam = sqlite3.connect('cricket.db')
        cur = Myteam.cursor()
        items = []
        ids = ","
        for x in range(3,self.l2.count()-1):
            items.append(self.l2.item(x).text())
        for i in items:
            sql = "SELECT * FROM stats WHERE player_name = '{}';".format(i[8:])
            cur.execute(sql)
            rec = cur.fetchone()
            ids = ids+","+"{}".format(rec[0])
        sql2 = "UPDATE teams set players = '{}' WHERE team_name  = '{}';".format(ids, self.t1.text())
        cur.execute(sql2)
        Myteam.commit()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def open_team(self):
        from Lib import sqlite3
        Myteam = sqlite3.connect('cricket.db')
        cur = Myteam.cursor()
        items = []
        ids = ","
        for x in range(3,self.l2.count()-1):
            items.append(self.l2.item(x).text())
        for i in items:
            sql = "SELECT * FROM stats WHERE player_name = '{}';".format(i[8:])
            cur.execute(sql)
            rec = cur.fetchone()
            ids = ids+","+"{}".format(rec[0])
        sql2 = "UPDATE teams set players = '{}' WHERE team_name  = '{}';".format(ids, self.t1.text())
        cur.execute(sql2)
        Myteam.commit()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QListWidget(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(70, 160, 291, 391))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l1.setFont(font)
        self.l1.setStyleSheet("color: rgb(0, 85, 255);")
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QListWidget(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(440, 160, 291, 391))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l2.setFont(font)
        self.l2.setStyleSheet("color: rgb(0, 85, 255);")
        self.l2.setObjectName("l2")
        item = QtWidgets.QListWidgetItem()
        self.l2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l2.addItem(item)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(440, 160, 291, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.t1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t1.setFont(font)
        self.t1.setStyleSheet("color: rgb(53, 186, 193);")
        self.t1.setObjectName("t1")
        self.horizontalLayout_2.addWidget(self.t1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 30, 701, 81))
        self.listView.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(98, 98, 98);")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 110, 701, 2))
        self.line.setStyleSheet("color: rgb(198, 198, 198);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 30, 701, 2))
        self.line_2.setStyleSheet("color: rgb(198, 198, 198);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 130, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.t2 = QtWidgets.QLabel(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(190, 130, 25, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t2.setFont(font)
        self.t2.setStyleSheet("color: rgb(53, 186, 193);")
        self.t2.setObjectName("t2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(440, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.t3 = QtWidgets.QLabel(self.centralwidget)
        self.t3.setGeometry(QtCore.QRect(530, 130, 25, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t3.setFont(font)
        self.t3.setStyleSheet("color: rgb(53, 186, 193);")
        self.t3.setObjectName("t3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 160, 291, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCheckable(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setCheckable(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 30, 2, 81))
        self.line_3.setStyleSheet("color: rgb(198, 198, 198);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(750, 30, 2, 81))
        self.line_4.setStyleSheet("color: rgba(198, 198, 198, 198);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(70, 160, 2, 391))
        self.line_5.setStyleSheet("color:rgb(106, 106, 106)")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(360, 160, 2, 391))
        self.line_6.setStyleSheet("color: rgb(106, 106, 106);")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(440, 160, 2, 391))
        self.line_7.setStyleSheet("color: rgb(106, 106, 106);")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(730, 160, 2, 391))
        self.line_8.setStyleSheet("color:rgb(106, 106, 106)")
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(70, 550, 291, 2))
        self.line_9.setStyleSheet("color: rgb(106, 106, 106);")
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(440, 550, 291, 2))
        self.line_10.setStyleSheet("color:rgb(106, 106, 106)")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(440, 160, 291, 2))
        self.line_11.setStyleSheet("color: rgb(106, 106, 106);")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(70, 160, 291, 2))
        self.line_12.setStyleSheet("color: rgb(106, 106, 106);")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 70, 97, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.label_11.setObjectName("label_11")
        self.t4 = QtWidgets.QLabel(self.centralwidget)
        self.t4.setGeometry(QtCore.QRect(180, 70, 18, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t4.setFont(font)
        self.t4.setStyleSheet("color: rgb(53, 186, 193);\n"
"background-color: rgb(243, 243, 243);")
        self.t4.setObjectName("t4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 70, 97, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.label_9.setObjectName("label_9")
        self.t5 = QtWidgets.QLabel(self.centralwidget)
        self.t5.setGeometry(QtCore.QRect(340, 70, 18, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t5.setFont(font)
        self.t5.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(53, 186, 193);")
        self.t5.setObjectName("t5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 70, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.label_7.setObjectName("label_7")
        self.t6 = QtWidgets.QLabel(self.centralwidget)
        self.t6.setGeometry(QtCore.QRect(500, 70, 18, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t6.setFont(font)
        self.t6.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(53, 186, 193);")
        self.t6.setObjectName("t6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 70, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.label_5.setObjectName("label_5")
        self.t7 = QtWidgets.QLabel(self.centralwidget)
        self.t7.setGeometry(QtCore.QRect(700, 70, 18, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t7.setFont(font)
        self.t7.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(53, 186, 193);")
        self.t7.setObjectName("t7")
        self.l1.raise_()
        self.l2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.listView.raise_()
        self.label.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_12.raise_()
        self.t2.raise_()
        self.label_14.raise_()
        self.t3.raise_()
        self.horizontalLayoutWidget.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.label_11.raise_()
        self.label_11.raise_()
        self.t4.raise_()
        self.label_9.raise_()
        self.t5.raise_()
        self.label_7.raise_()
        self.t6.raise_()
        self.label_5.raise_()
        self.t7.raise_()
        self.label_11.raise_()
        self.t4.raise_()
        self.label_9.raise_()
        self.t5.raise_()
        self.label_7.raise_()
        self.t6.raise_()
        self.label_5.raise_()
        self.t7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"")
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionNEW_Team.setFont(font)
        self.actionNEW_Team.setObjectName("actionNEW_Team")

        self.actionNEW_Team.triggered.connect(self.new_team)
        self.actionNEW_Team.triggered.connect(MainWindow.close)
        
        self.action_OPEN_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.action_OPEN_Team.setFont(font)
        self.action_OPEN_Team.setObjectName("action_OPEN_Team")

        self.action_OPEN_Team.triggered.connect(self.open_team)
        self.action_OPEN_Team.triggered.connect(MainWindow.close)
        
        self.action_SAVE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.action_SAVE_Team.setFont(font)
        self.action_SAVE_Team.setObjectName("action_SAVE_Team")

        self.action_SAVE_Team.triggered.connect(self.save_team)
        self.action_SAVE_Team.triggered.connect(MainWindow.close)
        
        self.action_EVALUATE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.action_EVALUATE_Team.setFont(font)
        self.action_EVALUATE_Team.setObjectName("action_EVALUATE_Team")

        self.action_EVALUATE_Team.triggered.connect(self.evaluate_team)
        self.action_EVALUATE_Team.triggered.connect(MainWindow.close)
        
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.action_OPEN_Team)
        self.menuManage_Teams.addAction(self.action_SAVE_Team)
        self.menuManage_Teams.addAction(self.action_EVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.radioButton.clicked.connect(self.bowlers)
        self.radioButton_2.clicked.connect(self.wicket_keepers)
        self.radioButton_3.clicked.connect(self.allrounders)
        self.radioButton_4.clicked.connect(self.batsmen)
    
       
        self.l1.itemDoubleClicked.connect(self.removelist1)
        self.l2.itemDoubleClicked.connect(self.removelist2)

        
    def retranslateUi(self, MainWindow):
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        try:
            cur = Myteam.cursor()
            sql = "SELECT * FROM teams WHERE players is NULL ;"
            cur.execute(sql)
        
            record=cur.fetchone()
        
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
            __sortingEnabled = self.l1.isSortingEnabled()
            self.l1.setSortingEnabled(False)
            self.l1.setSortingEnabled(__sortingEnabled)
            __sortingEnabled = self.l2.isSortingEnabled()
            self.l2.setSortingEnabled(False)
            self.l2.setSortingEnabled(__sortingEnabled)
            self.label_3.setText(_translate("MainWindow", "Team Name  "))

            self.t1.setText(_translate("MainWindow", "{}".format(record[1])))

            self.label.setText(_translate("MainWindow", "Your Selections"))
            self.label_12.setText(_translate("MainWindow", "Points Avialable"))
            self.t2.setText(_translate("MainWindow", "0"))
            self.label_14.setText(_translate("MainWindow", "Points Used"))
            self.t3.setText(_translate("MainWindow", "0"))
            self.radioButton_4.setText(_translate("MainWindow", "BAT"))
            self.radioButton.setText(_translate("MainWindow", "BOW"))
            self.radioButton_3.setText(_translate("MainWindow", "AR"))
            self.radioButton_2.setText(_translate("MainWindow", "WK"))
            self.label_11.setText(_translate("MainWindow", "Batsmen (BAT)"))
            self.t4.setText(_translate("MainWindow", "0"))
            self.label_9.setText(_translate("MainWindow", "Bowlers (BOW)"))
            self.t5.setText(_translate("MainWindow", "0"))
            self.label_7.setText(_translate("MainWindow", "Allrounders (AR)"))
            self.t6.setText(_translate("MainWindow", "0"))
            self.label_5.setText(_translate("MainWindow", "Wicket-keepers (WK)"))
            self.t7.setText(_translate("MainWindow", "0"))
            self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
            self.actionNEW_Team.setText(_translate("MainWindow", "      NEW Team"))
            self.actionNEW_Team.setToolTip(_translate("MainWindow", "0"))
            self.action_OPEN_Team.setText(_translate("MainWindow", "      OPEN Team"))
            self.action_SAVE_Team.setText(_translate("MainWindow", "      SAVE Team"))
            self.action_EVALUATE_Team.setText(_translate("MainWindow", "      EVALUATE Team"))
        except TypeError:
            print("Error in operation. You may have entered a team name which already exists.")
            

         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
