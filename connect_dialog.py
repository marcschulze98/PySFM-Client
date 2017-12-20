# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(343, 232)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.connectbtn = QtWidgets.QPushButton(Dialog)
        self.connectbtn.setDefault(True)
        self.connectbtn.setObjectName("connectbtn")
        self.gridLayout_2.addWidget(self.connectbtn, 1, 3, 1, 1)
        self.quitbtn = QtWidgets.QPushButton(Dialog)
        self.quitbtn.setObjectName("quitbtn")
        self.gridLayout_2.addWidget(self.quitbtn, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.passwordlbl = QtWidgets.QLabel(self.widget)
        self.passwordlbl.setObjectName("passwordlbl")
        self.gridLayout.addWidget(self.passwordlbl, 2, 0, 1, 1)
        self.usernamele = QtWidgets.QLineEdit(self.widget)
        self.usernamele.setObjectName("usernamele")
        self.gridLayout.addWidget(self.usernamele, 1, 1, 1, 1)
        self.usernamelbl = QtWidgets.QLabel(self.widget)
        self.usernamelbl.setObjectName("usernamelbl")
        self.gridLayout.addWidget(self.usernamelbl, 1, 0, 1, 1)
        self.addressle = QtWidgets.QLineEdit(self.widget)
        self.addressle.setObjectName("addressle")
        self.gridLayout.addWidget(self.addressle, 0, 1, 1, 1)
        self.addresslbl = QtWidgets.QLabel(self.widget)
        self.addresslbl.setObjectName("addresslbl")
        self.gridLayout.addWidget(self.addresslbl, 0, 0, 1, 1)
        self.passwordle = QtWidgets.QLineEdit(self.widget)
        self.passwordle.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordle.setObjectName("passwordle")
        self.gridLayout.addWidget(self.passwordle, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 2)
        self.statuslbl = QtWidgets.QLabel(self.widget)
        self.statuslbl.setObjectName("statuslbl")
        self.gridLayout.addWidget(self.statuslbl, 3, 0, 1, 1)
        self.statusoutputlbl = QtWidgets.QLabel(self.widget)
        self.statusoutputlbl.setObjectName("statusoutputlbl")
        self.gridLayout.addWidget(self.statusoutputlbl, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.addressle, self.usernamele)
        Dialog.setTabOrder(self.usernamele, self.passwordle)
        Dialog.setTabOrder(self.passwordle, self.connectbtn)
        Dialog.setTabOrder(self.connectbtn, self.quitbtn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connect to server"))
        self.connectbtn.setText(_translate("Dialog", "Connect"))
        self.quitbtn.setText(_translate("Dialog", "Quit"))
        self.passwordlbl.setText(_translate("Dialog", "Password:"))
        self.usernamelbl.setText(_translate("Dialog", "Username:"))
        self.addresslbl.setText(_translate("Dialog", "Server address:"))
        self.statuslbl.setText(_translate("Dialog", "Status:"))
        self.statusoutputlbl.setText(_translate("Dialog", "Waiting for input."))

