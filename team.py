# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from cricket2 import Ui_MainWindow
from message3 import Ui_msg6

class Ui_Form(object):
    def team_name(self):
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        team_name = self.lineEdit.text()
        sql = "SELECT * FROM teams WHERE team_name = '{}'".format(team_name)
        cur.execute(sql)
        rec = cur.fetchone()
        if rec == None:
            sql2 = "INSERT INTO teams (team_name, players, value) VALUES ('"+team_name+"', NULL, NULL);"
            cur.execute(sql2)
            Myteam.commit()
        else:
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_msg6()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()

    def mainwindow(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(244, 138)
        Form.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 181, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.team_name)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton.clicked.connect(self.mainwindow)
       
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 100, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Team Name"))
        self.label.setText(_translate("Form", "Name of Team :"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
