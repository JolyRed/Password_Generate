# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_generate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 0, 441, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 160, 113, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 25px;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 300, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(7, 7, 7);\n"
"border-radius: 25px;")
        self.pushButton.setObjectName("pushButton")
        self.main_edit = QtWidgets.QLineEdit(Form)
        self.main_edit.setGeometry(QtCore.QRect(20, 420, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.main_edit.setFont(font)
        self.main_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 25px;")
        self.main_edit.setText("")
        self.main_edit.setObjectName("main_edit")
        self.btn_check_strong = QtWidgets.QPushButton(Form)
        self.btn_check_strong.setGeometry(QtCore.QRect(610, 160, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_check_strong.setFont(font)
        self.btn_check_strong.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 25px;")
        self.btn_check_strong.setObjectName("btn_check_strong")
        self.label_strong = QtWidgets.QLabel(Form)
        self.label_strong.setGeometry(QtCore.QRect(580, 260, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_strong.setFont(font)
        self.label_strong.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;")
        self.label_strong.setText("")
        self.label_strong.setObjectName("label_strong")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 510, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 510, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.btn_reload = QtWidgets.QPushButton(Form)
        self.btn_reload.setGeometry(QtCore.QRect(610, 360, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_reload.setFont(font)
        self.btn_reload.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(7, 7, 7);\n"
"border-radius: 25px;")
        self.btn_reload.setObjectName("btn_reload")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Генератор паролей"))
        self.label.setText(_translate("Form", "Сгенерируйте пароль"))
        self.label_2.setText(_translate("Form", "Количество символов:"))
        self.pushButton.setText(_translate("Form", "Сгенерировать"))
        self.btn_check_strong.setText(_translate("Form", "Проверить пароль"))
        self.pushButton_2.setText(_translate("Form", "Скопировать"))
        self.pushButton_3.setText(_translate("Form", "Сохранить пароль"))
        self.btn_reload.setText(_translate("Form", "Сбросить"))

