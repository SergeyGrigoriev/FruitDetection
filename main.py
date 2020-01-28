# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(QtGui.QFont('SansSerif', 15))  # Изменение шрифта и размера
        self.label.setGeometry(QtCore.QRect(100, 110, 300, 300))  # изменить геометрию ярлыка
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(QtGui.QFont('SansSerif', 15))  # Изменение шрифта и размера
        self.label_2.setGeometry(QtCore.QRect(90, 200, 500, 300))  # изменить геометрию ярлыка
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)

        self.label_3.setFont(QtGui.QFont('SansSerif', 25))  # Изменение шрифта и размера
        self.label_3.setGeometry(QtCore.QRect(150, 55, 300, 200))  # изменить геометрию ярлыка
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 257, 191, 26))  # изменить геометрию ярлыка
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 340, 191, 26))  # изменить геометрию ярлыка
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFont(QtGui.QFont('SansSerif', 13))  # Изменение шрифта и размера КНОПКИ
        self.pushButton.setGeometry(QtCore.QRect(240, 425, 150, 38))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setFont(QtGui.QFont('SansSerif', 12))  # Изменение шрифта и размера КНОПКИ
        self.pushButton_2.setGeometry(QtCore.QRect(200, 480, 240, 40))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 261, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\Таня\\Documents\\Snimok.PNG"))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_3.setText(_translate("MainWindow", "Авторизация"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.pushButton_2.setText(_translate("MainWindow", "Зарегистрироваться"))
