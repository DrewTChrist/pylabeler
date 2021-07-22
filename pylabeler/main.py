# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 862)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setIconSize(QtCore.QSize(28, 28))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.dragAndDrop = QtWidgets.QWidget()
        self.dragAndDrop.setEnabled(True)
        self.dragAndDrop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dragAndDrop.setObjectName("dragAndDrop")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dragAndDrop)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.elementTree = QtWidgets.QTreeWidget(self.dragAndDrop)
        self.elementTree.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elementTree.sizePolicy().hasHeightForWidth())
        self.elementTree.setSizePolicy(sizePolicy)
        self.elementTree.setAcceptDrops(True)
        self.elementTree.setColumnCount(1)
        self.elementTree.setObjectName("elementTree")
        self.elementTree.headerItem().setText(0, "1")
        self.elementTree.header().setVisible(False)
        self.elementTree.header().setCascadingSectionResizes(False)
        self.elementTree.header().setSortIndicatorShown(False)
        self.elementTree.header().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.elementTree, 4, 0, 1, 1)
        self.labelView = QtWidgets.QWidget(self.dragAndDrop)
        self.labelView.setObjectName("labelView")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.labelView)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.labelView)
        self.webEngineView.setMaximumSize(QtCore.QSize(400, 600))
        self.webEngineView.setProperty("url", QtCore.QUrl("file:///home/andrew/development/pylabeler/assets/test.html"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout_4.addWidget(self.webEngineView, 0, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_2.addWidget(self.labelView, 4, 1, 1, 1)
        self.toolButtonBar = QtWidgets.QWidget(self.dragAndDrop)
        self.toolButtonBar.setObjectName("toolButtonBar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.toolButtonBar)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolButton_barcode = QtWidgets.QToolButton(self.toolButtonBar)
        self.toolButton_barcode.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_barcode.setCheckable(False)
        self.toolButton_barcode.setAutoRaise(True)
        self.toolButton_barcode.setObjectName("toolButton_barcode")
        self.gridLayout_3.addWidget(self.toolButton_barcode, 0, 1, 1, 1)
        self.toolButton_text = QtWidgets.QToolButton(self.toolButtonBar)
        self.toolButton_text.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_text.setAutoRaise(True)
        self.toolButton_text.setObjectName("toolButton_text")
        self.gridLayout_3.addWidget(self.toolButton_text, 0, 3, 1, 1)
        self.toolButton_image = QtWidgets.QToolButton(self.toolButtonBar)
        self.toolButton_image.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_image.setAutoRaise(True)
        self.toolButton_image.setObjectName("toolButton_image")
        self.gridLayout_3.addWidget(self.toolButton_image, 0, 2, 1, 1)
        self.toolButton_table = QtWidgets.QToolButton(self.toolButtonBar)
        self.toolButton_table.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_table.setAutoRaise(True)
        self.toolButton_table.setObjectName("toolButton_table")
        self.gridLayout_3.addWidget(self.toolButton_table, 0, 4, 1, 1)
        self.toolButton_qrcode = QtWidgets.QToolButton(self.toolButtonBar)
        self.toolButton_qrcode.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_qrcode.setAutoRaise(True)
        self.toolButton_qrcode.setObjectName("toolButton_qrcode")
        self.gridLayout_3.addWidget(self.toolButton_qrcode, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.toolButtonBar, 1, 0, 1, 2, QtCore.Qt.AlignLeft)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.dragAndDrop, "")
        self.htmlEditor_2 = QtWidgets.QWidget()
        self.htmlEditor_2.setObjectName("htmlEditor_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.htmlEditor_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.htmlLabel = QtWidgets.QLabel(self.htmlEditor_2)
        self.htmlLabel.setObjectName("htmlLabel")
        self.gridLayout_5.addWidget(self.htmlLabel, 0, 0, 1, 1)
        self.cssEditor = QtWidgets.QTextEdit(self.htmlEditor_2)
        self.cssEditor.setObjectName("cssEditor")
        self.gridLayout_5.addWidget(self.cssEditor, 4, 0, 1, 1)
        self.cssLabel = QtWidgets.QLabel(self.htmlEditor_2)
        self.cssLabel.setObjectName("cssLabel")
        self.gridLayout_5.addWidget(self.cssLabel, 3, 0, 1, 1)
        self.htmlEditor = QtWidgets.QTextEdit(self.htmlEditor_2)
        self.htmlEditor.setObjectName("htmlEditor")
        self.gridLayout_5.addWidget(self.htmlEditor, 2, 0, 1, 1)
        self.labelView_2 = QtWidgets.QWidget(self.htmlEditor_2)
        self.labelView_2.setObjectName("labelView_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.labelView_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.webEngineView_2 = QtWebEngineWidgets.QWebEngineView(self.labelView_2)
        self.webEngineView_2.setMaximumSize(QtCore.QSize(400, 600))
        self.webEngineView_2.setProperty("url", QtCore.QUrl("file:///home/andrew/development/pylabeler/assets/test.html"))
        self.webEngineView_2.setObjectName("webEngineView_2")
        self.gridLayout_7.addWidget(self.webEngineView_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.labelView_2, 2, 1, 3, 2)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.tabWidget.addTab(self.htmlEditor_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dataSourceView = QtWidgets.QTableView(self.tab_3)
        self.dataSourceView.setObjectName("dataSourceView")
        self.gridLayout_6.addWidget(self.dataSourceView, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        self.gridLayout_6.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1450, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose_Project = QtWidgets.QAction(MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionClose_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyLabeler"))
        self.toolButton_barcode.setText(_translate("MainWindow", "..."))
        self.toolButton_text.setText(_translate("MainWindow", "..."))
        self.toolButton_image.setText(_translate("MainWindow", "..."))
        self.toolButton_table.setText(_translate("MainWindow", "..."))
        self.toolButton_qrcode.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dragAndDrop), _translate("MainWindow", "Drag and Drop"))
        self.htmlLabel.setText(_translate("MainWindow", "HTML"))
        self.cssLabel.setText(_translate("MainWindow", "CSS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.htmlEditor_2), _translate("MainWindow", "HTML Editor"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "CSV"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Text"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Excel"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Quickbooks"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Access"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "SQL"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "ODBC"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Data Source"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionClose_Project.setText(_translate("MainWindow", "Close Project"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
from PyQt5 import QtWebEngineWidgets
