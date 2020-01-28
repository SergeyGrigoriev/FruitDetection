# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_select(object):
    def setupUi(self, select):
        select.setObjectName("select")
        select.resize(600, 600)
        select.setMinimumSize(QtCore.QSize(600, 600))
        select.setMaximumSize(QtCore.QSize(600, 600))

        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.label = QtWidgets.QLabel(select)
        self.label.setGeometry(QtCore.QRect(40, 150, 471, 51))
        self.label.setFont(font)
        self.label.setObjectName("label")

        font.setPointSize(13)
        self.pushButton = QtWidgets.QPushButton(select)
        self.pushButton.setGeometry(QtCore.QRect(43, 260, 261, 42))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(select)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 350, 341, 42))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        icon = QtGui.QIcon()

        # Выйти
        self.pushButton_3 = QtWidgets.QPushButton(select)
        self.pushButton_3.setFont(QtGui.QFont('SansSerif', 11))
        self.pushButton_3.setGeometry(QtCore.QRect(520, 540, 67, 47))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 116))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_2 = QtWidgets.QLabel(select)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 261, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\Таня\\Documents\\Snimok.PNG"))
        self.label_2.setObjectName("label_2")
        self.retranslateUi(select)
        QtCore.QMetaObject.connectSlotsByName(select)

    def retranslateUi(self, select):
        _translate = QtCore.QCoreApplication.translate
        select.setWindowTitle(_translate("select", "Меню"))
        self.label.setText(_translate("select", "Выбирете дальнейшие действия:"))
        self.pushButton.setText(_translate("select", "Внести изменения"))
        self.pushButton_2.setText(_translate("select", "Сформировать приказ"))
        self.pushButton_3.setText(_translate("select", "Выйти"))

