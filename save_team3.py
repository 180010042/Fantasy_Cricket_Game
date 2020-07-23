# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_team.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from message2 import Ui_msg2
from open_team import Ui_msg5

class Ui_Dialog3(object):
    def save_team(self):
        self.msg = QtWidgets.QDialog()
        self.ui = Ui_msg2()
        self.ui.setupUi(self.msg)
        self.msg.show()
        
    def delete_team(self):
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM teams;"
        cur.execute(sql)
        record = cur.fetchall()
        rows = record[-1][0]
        sql2 = " DELETE FROM teams WHERE ID = {};".format(rows)
        cur.execute(sql2)
        Myteam.commit()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_msg5()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def message(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_msg5()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(255, 100)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 25, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Users/Admin/Documents/question.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 60, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.message)
        self.pushButton.clicked.connect(self.save_team)
        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton_2.clicked.connect(self.delete_team)
        self.pushButton_2.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Save Team?"))
        self.label.setText(_translate("Dialog", "Do you want to save the team?"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Don\'t Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
