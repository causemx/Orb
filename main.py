# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from os import walk

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QFormLayout, QGroupBox, QScrollArea, QVBoxLayout


class Ui_MainWindow(object):
    def __init__(self):
        self.src = []
        self.index = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pbPrevious = QtWidgets.QPushButton(self.centralwidget)
        self.pbPrevious.setGeometry(QtCore.QRect(260, 500, 113, 32))
        self.pbPrevious.setObjectName("pbPrevious")
        self.pbPrevious.clicked.connect(self.btn_click_event)

        self.pbNext = QtWidgets.QPushButton(self.centralwidget)
        self.pbNext.setGeometry(QtCore.QRect(380, 500, 113, 32))
        self.pbNext.setObjectName("pbNext")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        self.menuOrb = QtWidgets.QMenu(self.menubar)
        self.menuOrb.setObjectName("menuOrb")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")

        self.actionOpen_File.triggered.connect(self.processtrigger)

        self.menuOrb.addAction(self.actionOpen_File)
        self.menuOrb.addAction(self.actionSetting)
        self.menuOrb.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOrb.menuAction())

        self.formlayout = QFormLayout()
        self.groupbox = QGroupBox()
        self.groupbox.setLayout(self.formlayout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(self.groupbox)
        scroll.setCornerWidget(True)

        layout = QVBoxLayout(self.centralwidget)
        layout.addWidget(scroll)

        #self.labelPic = QtWidgets.QLabel(self.centralwidget)
        #self.labelPic.setGeometry(QtCore.QRect(110, 50, 561, 391))
        self.labelPic = QtWidgets.QLabel()
        self.labelPic.setObjectName("labelPic")
        self.labelPic.setScaledContents(True)
        self.formlayout.addRow(self.labelPic)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btn_click_event(self):
        self.labelPic.setPixmap(QPixmap(self.path + '/' + self.src[(self.index + 1) % len(self.src)]))

    def processtrigger(self):
        # In PyQt5, QFileDialog.getOpenFileName returns two parameters as a tuple
        # frame, _ = QFileDialog.getOpenFileName(self.centralwidget, 'open file', '.', "Image files (*.jpg *.png)")
        # self.labelPic.setPixmap(QPixmap(frame))
        self.path = QFileDialog.getExistingDirectory(self.centralwidget, 'open directory', '.')
        for root, dirs, files in walk(self.path):
            self.src = files

        self.labelPic.setPixmap(QPixmap(self.path + '/' + self.src[0]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbPrevious.setText(_translate("MainWindow", "Previous"))
        self.pbNext.setText(_translate("MainWindow", "Next"))
        self.labelPic.setText(_translate("MainWindow", "image here"))
        self.menuOrb.setTitle(_translate("MainWindow", "Orb"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
