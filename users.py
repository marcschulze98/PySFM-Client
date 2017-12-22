# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'users.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_users(object):
    def setupUi(self, users):
        users.setObjectName("users")
        users.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(users)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(users)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.userlist = QtWidgets.QListWidget(users)
        self.userlist.setObjectName("userlist")
        self.gridLayout.addWidget(self.userlist, 1, 0, 1, 1)
        self.allusersbtn = QtWidgets.QPushButton(users)
        self.allusersbtn.setObjectName("allusersbtn")
        self.gridLayout.addWidget(self.allusersbtn, 2, 0, 1, 1)
        self.onlineusersbtn = QtWidgets.QPushButton(users)
        self.onlineusersbtn.setObjectName("onlineusersbtn")
        self.gridLayout.addWidget(self.onlineusersbtn, 3, 0, 1, 1)

        self.retranslateUi(users)
        QtCore.QMetaObject.connectSlotsByName(users)

    def retranslateUi(self, users):
        _translate = QtCore.QCoreApplication.translate
        users.setWindowTitle(_translate("users", "Users"))
        self.label.setText(_translate("users", "Users:"))
        self.allusersbtn.setText(_translate("users", "Show all users"))
        self.onlineusersbtn.setText(_translate("users", "Show online users"))

