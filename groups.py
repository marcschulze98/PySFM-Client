# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groups.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_groups(object):
    def setupUi(self, groups):
        groups.setObjectName("groups")
        groups.resize(358, 429)
        self.gridLayout = QtWidgets.QGridLayout(groups)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(groups)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.grouplist = QtWidgets.QListWidget(groups)
        self.grouplist.setObjectName("grouplist")
        self.gridLayout.addWidget(self.grouplist, 1, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(groups)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.memberlist = QtWidgets.QListWidget(groups)
        self.memberlist.setObjectName("memberlist")
        self.gridLayout.addWidget(self.memberlist, 3, 0, 1, 3)
        self.adduserbtn = QtWidgets.QPushButton(groups)
        self.adduserbtn.setObjectName("adduserbtn")
        self.gridLayout.addWidget(self.adduserbtn, 6, 2, 1, 1)
        self.creategroupbtn = QtWidgets.QPushButton(groups)
        self.creategroupbtn.setObjectName("creategroupbtn")
        self.gridLayout.addWidget(self.creategroupbtn, 7, 2, 1, 1)
        self.refreshbtn = QtWidgets.QPushButton(groups)
        self.refreshbtn.setObjectName("refreshbtn")
        self.gridLayout.addWidget(self.refreshbtn, 4, 0, 1, 3)
        self.deletegroupbtn = QtWidgets.QPushButton(groups)
        self.deletegroupbtn.setObjectName("deletegroupbtn")
        self.gridLayout.addWidget(self.deletegroupbtn, 8, 0, 1, 3)
        self.creategrouple = QtWidgets.QLineEdit(groups)
        self.creategrouple.setObjectName("creategrouple")
        self.gridLayout.addWidget(self.creategrouple, 7, 0, 1, 2)
        self.deleteuserbtn = QtWidgets.QPushButton(groups)
        self.deleteuserbtn.setObjectName("deleteuserbtn")
        self.gridLayout.addWidget(self.deleteuserbtn, 5, 0, 1, 3)
        self.adduserle = QtWidgets.QLineEdit(groups)
        self.adduserle.setObjectName("adduserle")
        self.gridLayout.addWidget(self.adduserle, 6, 0, 1, 2)

        self.retranslateUi(groups)
        QtCore.QMetaObject.connectSlotsByName(groups)

    def retranslateUi(self, groups):
        _translate = QtCore.QCoreApplication.translate
        groups.setWindowTitle(_translate("groups", "Groups"))
        self.label.setText(_translate("groups", "Groups:"))
        self.label_2.setText(_translate("groups", "Members:"))
        self.adduserbtn.setText(_translate("groups", "Add member"))
        self.creategroupbtn.setText(_translate("groups", "Create group"))
        self.refreshbtn.setText(_translate("groups", "Refresh groups"))
        self.deletegroupbtn.setText(_translate("groups", "Delete group"))
        self.deleteuserbtn.setText(_translate("groups", "Delete member"))

