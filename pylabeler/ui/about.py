# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(400, 175)
        self.label = QtWidgets.QLabel(aboutDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(aboutDialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 201, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(aboutDialog)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 261, 21))
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(aboutDialog)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(aboutDialog)
        self.label_5.setGeometry(QtCore.QRect(40, 130, 91, 21))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About"))
        self.label.setText(_translate("aboutDialog", "About"))
        self.label_2.setText(_translate("aboutDialog", "Author: Andrew Christiansen"))
        self.label_3.setText(_translate("aboutDialog", "Homepage: <a href=\"https://github.com/drewtchrist/pylabeler\">https://github.com/drewtchrist/pylabeler</a>"))
        self.label_4.setText(_translate("aboutDialog", "Version: 0.1.0"))
        self.label_5.setText(_translate("aboutDialog", "License: MIT"))
