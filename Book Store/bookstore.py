# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookstore.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from bookadd import Ui_MainWindow
import sqlite3


class Ui_Form(object):

    def __init__(self):
        self.price=0.0
        self.total_cost=0.0

    def openAdder(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def find_price(self):
        ttl=self.lineEdit.text()
        
        Mybooks=sqlite3.connect('booksdb.db')
        curbooks=Mybooks.cursor()
        sql="SELECT * FROM bookstb WHERE TITLE='"+str(ttl)+"';"
        curbooks.execute(sql)
        record=curbooks.fetchone()
        if record==None:
            self.label_7.setText("No such book found!!!")
        else:
            self.lineEdit_3.clear()
            self.label_6.setText("Rs.0")
            self.label_7.setText("Book found!!!")
            print (record)
            pri=record[2]
            self.label_5.setText("Rs. {}".format(pri))
            self.price=pri

    def find_total(self):
        a=self.price
        b=float(self.lineEdit_3.text())
        self.total_cost=a*b
        self.label_6.setText("Rs. {}".format(self.total_cost))

    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 350)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 50, 301, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.find_price)
        
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setIndent(-1)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_3.setValidator(QtGui.QIntValidator())
        
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.find_total)
        
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 220, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.openAdder)

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 260, 301, 20))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Book Store"))
        self.label.setText(_translate("Form", "Book Title"))
        self.pushButton.setText(_translate("Form", "Find Price"))
        self.label_2.setText(_translate("Form", "Price"))
        self.label_5.setText(_translate("Form", "Rs. 0"))
        self.label_3.setText(_translate("Form", "Quantity"))
        self.pushButton_2.setText(_translate("Form", "Find Total"))
        self.label_4.setText(_translate("Form", "Total"))
        self.label_6.setText(_translate("Form", "Rs.0"))
        self.pushButton_3.setText(_translate("Form", "Add New Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

