# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prikaz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_changes(object):
    def setupUi(self, Order):
        Order.setObjectName("changes")
        Order.resize(450, 600)
        Order.setMinimumSize(QtCore.QSize(700, 600))
        Order.setMaximumSize(QtCore.QSize(700, 600))

        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)

        self.label = QtWidgets.QLabel(Order)
        #self.label.setFont(QtGui.QFont('Tahoma', 21))
        self.label.setGeometry(QtCore.QRect(135, 83, 261, 41))
        self.label.setFont(font)
        self.label.setObjectName("label")

        #font.setPointSize(9)

        self.label_2 = QtWidgets.QLabel(Order)
        self.label.setFont(QtGui.QFont('SansSerif', 15))
        self.label_2.setGeometry(QtCore.QRect(48, 120, 191, 40))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Order)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 101, 25))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_6")

        self.label_4 = QtWidgets.QLabel(Order)
        self.label_4.setGeometry(QtCore.QRect(433, 10, 261, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\Таня\\Documents\\Snimok.PNG"))
        self.label_4.setObjectName("label_5")

        self.lineEdit = QtWidgets.QLineEdit(Order)
        self.lineEdit.setGeometry(QtCore.QRect(165, 69, 181, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.comboBox = QtWidgets.QComboBox(Order)
        self.comboBox.setGeometry(QtCore.QRect(235, 135, 181, 20))
        self.comboBox.setObjectName("comboBox")

        self.pushButton = QtWidgets.QPushButton(Order)
        self.pushButton.setGeometry(QtCore.QRect(180, 190, 80, 33))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Order)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 500, 251, 37))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Order)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 550, 251, 37))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.tableWidget = QtWidgets.QTableWidget(Order)
        self.tableWidget.setGeometry(QtCore.QRect(10, 240, 680, 240))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Order)
        QtCore.QMetaObject.connectSlotsByName(Order)

    def retranslateUi(self, Order):
        _translate = QtCore.QCoreApplication.translate
        Order.setWindowTitle(_translate("Order", "Редактор"))
        self.label.setText(_translate("Order", ""))
        self.label_2.setText(_translate("Order", "Направление"))
        self.label_3.setText(_translate("Order", "Фамилия"))
        self.pushButton.setText(_translate("Order", "Поиск"))
        self.pushButton_2.setText(_translate("Order", "Сохранить"))
        self.pushButton_3.setText(_translate("Order", "Назад"))