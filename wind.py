# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\wind.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 667)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.currency_combobox = QtWidgets.QComboBox(Form)
        self.currency_combobox.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        self.currency_combobox.setFont(font)
        self.currency_combobox.setObjectName("currency_combobox")
        self.horizontalLayout_2.addWidget(self.currency_combobox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(35, -1, -1, -1)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.usd_course = QtWidgets.QLabel(Form)
        self.usd_course.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.usd_course.setFont(font)
        self.usd_course.setObjectName("usd_course")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usd_course)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.eur_course = QtWidgets.QLabel(Form)
        self.eur_course.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eur_course.setFont(font)
        self.eur_course.setObjectName("eur_course")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.eur_course)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(35, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_forecast = QtWidgets.QPushButton(Form)
        self.btn_forecast.setMinimumSize(QtCore.QSize(150, 45))
        self.btn_forecast.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        self.btn_forecast.setFont(font)
        self.btn_forecast.setObjectName("btn_forecast")
        self.verticalLayout_7.addWidget(self.btn_forecast)
        self.btn_statistic = QtWidgets.QPushButton(Form)
        self.btn_statistic.setMinimumSize(QtCore.QSize(150, 45))
        self.btn_statistic.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        self.btn_statistic.setFont(font)
        self.btn_statistic.setObjectName("btn_statistic")
        self.verticalLayout_7.addWidget(self.btn_statistic)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_new = QtWidgets.QPushButton(Form)
        self.btn_new.setMinimumSize(QtCore.QSize(150, 45))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        self.btn_new.setFont(font)
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout.addWidget(self.btn_new)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btn_theme = QtWidgets.QPushButton(Form)
        self.btn_theme.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_theme.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_theme.setText("")
        self.btn_theme.setObjectName("btn_theme")
        self.horizontalLayout.addWidget(self.btn_theme)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(37)
        self.tableWidget.verticalHeader().setVisible(True)
        self.verticalLayout_4.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "InvestCalc"))
        self.label.setText(_translate("Form", "Текущий баланс:"))
        self.label_2.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "USD"))
        self.usd_course.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "EUR"))
        self.eur_course.setText(_translate("Form", "0"))
        self.btn_forecast.setText(_translate("Form", "Прогноз"))
        self.btn_statistic.setText(_translate("Form", "Статистика"))
        self.btn_new.setText(_translate("Form", "Добавить"))
