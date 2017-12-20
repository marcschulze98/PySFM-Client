# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groups.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_groups(object):
    def setupUi(self, groups):
        groups.setObjectName("groups")
        groups.resize(225, 383)
        self.gridLayout = QtWidgets.QGridLayout(groups)
        self.gridLayout.setObjectName("gridLayout")
        self.grouplist = QtWidgets.QListWidget(groups)
        self.grouplist.setObjectName("grouplist")
        self.gridLayout.addWidget(self.grouplist, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(groups)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.deletegroupbtn = QtWidgets.QPushButton(groups)
        self.deletegroupbtn.setObjectName("deletegroupbtn")
        self.gridLayout.addWidget(self.deletegroupbtn, 7, 1, 1, 1)
        self.adduserbtn = QtWidgets.QPushButton(groups)
        self.adduserbtn.setObjectName("adduserbtn")
        self.gridLayout.addWidget(self.adduserbtn, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(groups)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.memberlist = QtWidgets.QListWidget(groups)
        self.memberlist.setObjectName("memberlist")
        self.gridLayout.addWidget(self.memberlist, 3, 1, 1, 1)
        self.creategroupbtn = QtWidgets.QPushButton(groups)
        self.creategroupbtn.setObjectName("creategroupbtn")
        self.gridLayout.addWidget(self.creategroupbtn, 6, 1, 1, 1)
        self.refreshbtn = QtWidgets.QPushButton(groups)
        self.refreshbtn.setObjectName("refreshbtn")
        self.gridLayout.addWidget(self.refreshbtn, 4, 1, 1, 1)

        self.retranslateUi(groups)
        QtCore.QMetaObject.connectSlotsByName(groups)

    def retranslateUi(self, groups):
        _translate = QtCore.QCoreApplication.translate
        groups.setWindowTitle(_translate("groups", "Groups"))
        self.label_2.setText(_translate("groups", "Members:"))
        self.deletegroupbtn.setText(_translate("groups", "Delete group"))
        self.adduserbtn.setText(_translate("groups", "Add user"))
        self.label.setText(_translate("groups", "Groups:"))
        self.creategroupbtn.setText(_translate("groups", "Create group"))
        self.refreshbtn.setText(_translate("groups", "Refresh groups"))

