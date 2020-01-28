# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inform(object):
    def setupUi(self, inform):
        inform.setObjectName("inform")
        inform.resize(450, 450)
        inform.setMinimumSize(QtCore.QSize(550, 200))
        inform.setMaximumSize(QtCore.QSize(550, 200))

        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.label = QtWidgets.QLabel(inform)
        self.label.setGeometry(QtCore.QRect(40, 70, 499, 41))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(inform)
        QtCore.QMetaObject.connectSlotsByName(inform)

    def retranslateUi(self, select):
        _translate = QtCore.QCoreApplication.translate
        select.setWindowTitle(_translate("inform", "Ошибка"))
        self.label.setText(_translate("inform", ""))