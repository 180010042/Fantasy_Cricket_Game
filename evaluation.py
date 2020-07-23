# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluation.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def players(self):
        self.l1.clear()
        from manofmatch import points
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM teams WHERE team_name = '{}';".format(self.comboBox.currentText())
        cur.execute(sql)
        rec = cur.fetchone()
        if rec != None:
            for i in rec[2]:
                if i!= ',':
                    sql2 = "SELECT * FROM stats WHERE ID = {};".format(int(i))
                    cur.execute(sql2)
                    rec2 = cur.fetchone()
                    self.l1.addItem("{}".format(rec2[1]))
                    if self.comboBox_2.currentText() != 'Select Match':
                        sql3 = "SELECT * FROM {} WHERE playerID = {};".format(self.comboBox_2.currentText(), int(i))
                        cur.execute(sql3)
                        rec3 = cur.fetchone()
                        score = points(rec3[1],rec3[2],rec3[3],rec3[4],rec3[8],int(rec3[5]/6),rec3[7],rec3[6]+rec3[9]+rec3[10]+rec3[11])
                        self.l2.addItem("{}".format(score))
                    
    def score(self):
        self.l2.clear()
        from manofmatch import points
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM teams WHERE team_name = '{}';".format(self.comboBox.currentText())
        cur.execute(sql)
        rec = cur.fetchone()
        if rec != None:
            for i in rec[2]:
                if i!= ',':
                    sql2 = "SELECT * FROM {} WHERE playerID = {};".format(self.comboBox_2.currentText(), int(i))
                    cur.execute(sql2)
                    rec2 = cur.fetchone()
                    score = points(rec2[1],rec2[2],rec2[3],rec2[4],rec2[8],int(rec2[5]/6),rec2[7],rec2[6]+rec2[9]+rec2[10]+rec2[11])
                    self.l2.addItem("{}".format(score))

    def total_score(self):
        from manofmatch import points
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM teams WHERE team_name = '{}';".format(self.comboBox.currentText())
        cur.execute(sql)
        rec = cur.fetchone()
        total = 0
        if rec != None:
            for i in rec[2]:
                if i!= ',':
                    sql2 = "SELECT * FROM {} WHERE playerID = {};".format(self.comboBox_2.currentText(), int(i))
                    cur.execute(sql2)
                    rec2 = cur.fetchone()
                    score = points(rec2[1],rec2[2],rec2[3],rec2[4],rec2[8],int(rec2[5]/6),rec2[7],rec2[6]+rec2[9]+rec2[10]+rec2[11])
                    total = total + score
                self.label_3.setText("{}".format(total))
                sql3 = "UPDATE teams SET value = {} WHERE team_name = '{}';".format(total, self.comboBox.currentText())
                cur.execute(sql3)
                Myteam.commit()
                
    def setupUi(self, Dialog):
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM teams;"
        cur.execute(sql)
        rec = cur.fetchall()  
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 444)
        Dialog.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.l1 = QtWidgets.QListWidget(Dialog)
        self.l1.setGeometry(QtCore.QRect(50, 150, 161, 231))
        self.l1.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(190, 150, 21, 231))
        self.verticalScrollBar.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.l2 = QtWidgets.QListWidget(Dialog)
        self.l2.setGeometry(QtCore.QRect(240, 150, 161, 231))
        self.l2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(53, 186, 193);")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(380, 150, 21, 231))
        self.verticalScrollBar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 130, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 130, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 130, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(53, 186, 193);")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 100, 390, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(60, 60, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        for i in rec:
           self.comboBox.addItem("")
           
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 60, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(50, 380, 161, 3))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(50, 150, 161, 3))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(240, 150, 161, 3))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(240, 380, 161, 3))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(50, 150, 2, 231))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(190, 150, 2, 231))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(210, 150, 2, 231))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(240, 150, 2, 231))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(380, 150, 2, 231))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(400, 150, 2, 231))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")        

        self.comboBox.currentTextChanged.connect(self.players)
        self.comboBox_2.currentTextChanged.connect(self.score)
        self.pushButton.clicked.connect(self.total_score)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        
        from Lib import sqlite3
        Myteam=sqlite3.connect('cricket.db')
        cur=Myteam.cursor()
        sql = "SELECT * FROM teams;"
        cur.execute(sql)
        rec = cur.fetchall()   
        Dialog.setWindowTitle(_translate("Dialog", "Evaluate Score"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))
        self.label.setText(_translate("Dialog", "Players"))
        self.label_2.setText(_translate("Dialog", "Points"))
        self.label_3.setText(_translate("Dialog", "0"))
        self.comboBox.setItemText(0, _translate("Dialog", "Select Team"))

        k = 1
        for i in rec:
           self.comboBox.setItemText(k, _translate("Dialog", "{}".format(i[1])))
           k += 1
           
        self.comboBox_2.setItemText(0, _translate("Dialog", "Select Match"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "match"))
        self.label_4.setText(_translate("Dialog", "Evaluate the Perfomance of your Fantasy Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
