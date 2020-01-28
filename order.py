# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prikaz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Order(object):
    def setupUi(self, Order):
        Order.setObjectName("Order")
        Order.resize(450, 600)
        Order.setMinimumSize(QtCore.QSize(700, 700))
        Order.setMaximumSize(QtCore.QSize(700, 700))

        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)

        self.label = QtWidgets.QLabel(Order)
        self.label.setGeometry(QtCore.QRect(180, 83, 361, 51))
        self.label.setFont(font)
        self.label.setObjectName("label")

        font.setPointSize(9)

        self.label_6 = QtWidgets.QLabel(Order)
        self.label_6.setGeometry(QtCore.QRect(50, 140, 101, 25))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_2 = QtWidgets.QLabel(Order)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 151, 20))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Order)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 81, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Order)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 61, 20))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Order)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 261, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\Таня\\Documents\\Snimok.PNG"))
        self.label_5.setObjectName("label_5")

        self.lineEdit = QtWidgets.QLineEdit(Order)
        self.lineEdit.setGeometry(QtCore.QRect(180, 140, 181, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.comboBox = QtWidgets.QComboBox(Order)
        self.comboBox.setGeometry(QtCore.QRect(180, 180, 181, 20))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(Order)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 220, 181, 20))
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_3 = QtWidgets.QComboBox(Order)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 260, 181, 22))
        self.comboBox_3.setObjectName("comboBox_3")

        self.pushButton = QtWidgets.QPushButton(Order)
        self.pushButton.setGeometry(QtCore.QRect(110, 300, 75, 27))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Order)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 620, 241, 28))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Order)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 660, 241, 28))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.tableWidget = QtWidgets.QTableWidget(Order)
        self.tableWidget.setGeometry(QtCore.QRect(10, 340, 680, 272))
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(Order)
        QtCore.QMetaObject.connectSlotsByName(Order)

    def retranslateUi(self, Order):
        _translate = QtCore.QCoreApplication.translate
        Order.setWindowTitle(_translate("Order", "Приказ"))
        self.label.setText(_translate("Order", "Формирование приказа"))
        self.label_2.setText(_translate("Order", "Направление"))
        self.label_3.setText(_translate("Order", "Профиль"))
        self.label_4.setText(_translate("Order", "Группа"))
        self.label_6.setText(_translate("Order", "Фамилия"))
        self.pushButton.setText(_translate("Order", "Поиск"))
        self.pushButton_2.setText(_translate("Order", "Сформировать приказ"))
        self.pushButton_3.setText(_translate("Order", "Назад"))
