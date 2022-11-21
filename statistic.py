# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\statistic.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stat(object):
    def setupUi(self, Stat):
        Stat.setObjectName("Stat")
        Stat.resize(453, 341)
        self.verticalLayout = QtWidgets.QVBoxLayout(Stat)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Stat)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.level = QtWidgets.QLabel(Stat)
        self.level.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.level.setFont(font)
        self.level.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.level.setScaledContents(False)
        self.level.setWordWrap(False)
        self.level.setObjectName("level")
        self.verticalLayout.addWidget(self.level)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Stat)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.stocks = QtWidgets.QLabel(Stat)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        self.stocks.setFont(font)
        self.stocks.setObjectName("stocks")
        self.horizontalLayout.addWidget(self.stocks)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Stat)
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.bonds = QtWidgets.QLabel(Stat)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        self.bonds.setFont(font)
        self.bonds.setObjectName("bonds")
        self.horizontalLayout_2.addWidget(self.bonds)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Stat)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(Stat)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(Stat)
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.rub = QtWidgets.QLabel(Stat)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        self.rub.setFont(font)
        self.rub.setObjectName("rub")
        self.horizontalLayout_5.addWidget(self.rub)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(Stat)
        self.label_5.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.usd = QtWidgets.QLabel(Stat)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        self.usd.setFont(font)
        self.usd.setObjectName("usd")
        self.horizontalLayout_3.addWidget(self.usd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(Stat)
        self.label_6.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.eur = QtWidgets.QLabel(Stat)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        self.eur.setFont(font)
        self.eur.setObjectName("eur")
        self.horizontalLayout_4.addWidget(self.eur)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Stat)
        QtCore.QMetaObject.connectSlotsByName(Stat)

    def retranslateUi(self, Stat):
        _translate = QtCore.QCoreApplication.translate
        Stat.setWindowTitle(_translate("Stat", "Статистика"))
        self.label.setText(_translate("Stat", "Уровень рискованности вашего портфеля:"))
        self.level.setText(_translate("Stat", "КОНСЕРВАТИВНЫЙ"))
        self.label_2.setText(_translate("Stat", "Акции:"))
        self.stocks.setText(_translate("Stat", "0"))
        self.label_4.setText(_translate("Stat", "Облигации/вклады:"))
        self.bonds.setText(_translate("Stat", "0"))
        self.label_3.setText(_translate("Stat", "Доли валют:"))
        self.label_7.setText(_translate("Stat", "Рубли (₽):"))
        self.rub.setText(_translate("Stat", "0"))
        self.label_5.setText(_translate("Stat", "Доллары ($):"))
        self.usd.setText(_translate("Stat", "0"))
        self.label_6.setText(_translate("Stat", "Евро (€):"))
        self.eur.setText(_translate("Stat", "0"))
