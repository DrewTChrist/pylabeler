# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/qrcode_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qrcodeDialog(object):
    def setupUi(self, qrcodeDialog):
        qrcodeDialog.setObjectName("qrcodeDialog")
        qrcodeDialog.resize(400, 300)
        qrcodeDialog.setMaximumSize(QtCore.QSize(400, 300))
        qrcodeDialog.setSizeGripEnabled(False)
        qrcodeDialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(qrcodeDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(qrcodeDialog)
        self.buttonBox.accepted.connect(qrcodeDialog.accept)
        self.buttonBox.rejected.connect(qrcodeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(qrcodeDialog)

    def retranslateUi(self, qrcodeDialog):
        _translate = QtCore.QCoreApplication.translate
        qrcodeDialog.setWindowTitle(_translate("qrcodeDialog", "QR Code Options"))
