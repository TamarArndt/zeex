# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Dec 29 17:11:45 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(800, 600)
        self.HomeWidget = QtGui.QWidget(HomeWindow)
        self.HomeWidget.setObjectName("HomeWidget")
        self.treeView = FileSystemTreeView(self.HomeWidget)
        self.treeView.setGeometry(QtCore.QRect(35, 81, 721, 441))
        self.treeView.setObjectName("treeView")
        HomeWindow.setCentralWidget(self.HomeWidget)
        self.homemenu = QtGui.QMenuBar(HomeWindow)
        self.homemenu.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.homemenu.setObjectName("homemenu")
        self.menuProjects = QtGui.QMenu(self.homemenu)
        self.menuProjects.setObjectName("menuProjects")
        self.menuActions = QtGui.QMenu(self.homemenu)
        self.menuActions.setObjectName("menuActions")
        HomeWindow.setMenuBar(self.homemenu)
        self.statusbar = QtGui.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(HomeWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtGui.QAction(HomeWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtGui.QAction(HomeWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionEdit = QtGui.QAction(HomeWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionSettings = QtGui.QAction(HomeWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionZip = QtGui.QAction(HomeWindow)
        self.actionZip.setObjectName("actionZip")
        self.actionZipFolder = QtGui.QAction(HomeWindow)
        self.actionZipFolder.setObjectName("actionZipFolder")
        self.actionViewCloud = QtGui.QAction(HomeWindow)
        self.actionViewCloud.setObjectName("actionViewCloud")
        self.actionUnzip = QtGui.QAction(HomeWindow)
        self.actionUnzip.setObjectName("actionUnzip")
        self.actionSQL = QtGui.QAction(HomeWindow)
        self.actionSQL.setObjectName("actionSQL")
        self.menuProjects.addAction(self.actionOpen)
        self.menuProjects.addAction(self.actionNew)
        self.menuProjects.addAction(self.actionSave)
        self.menuProjects.addAction(self.actionEdit)
        self.menuProjects.addAction(self.actionSettings)
        self.menuActions.addAction(self.actionZipFolder)
        self.menuActions.addAction(self.actionViewCloud)
        self.menuActions.addAction(self.actionUnzip)
        self.menuActions.addAction(self.actionSQL)
        self.homemenu.addAction(self.menuProjects.menuAction())
        self.homemenu.addAction(self.menuActions.menuAction())

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QtGui.QApplication.translate("HomeWindow", "Zeex Home", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProjects.setTitle(QtGui.QApplication.translate("HomeWindow", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("HomeWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("HomeWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("HomeWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("HomeWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setText(QtGui.QApplication.translate("HomeWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("HomeWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZip.setText(QtGui.QApplication.translate("HomeWindow", "Zip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZipFolder.setText(QtGui.QApplication.translate("HomeWindow", "Zip Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewCloud.setText(QtGui.QApplication.translate("HomeWindow", "View Cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnzip.setText(QtGui.QApplication.translate("HomeWindow", "Unzip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSQL.setText(QtGui.QApplication.translate("HomeWindow", "SQL", None, QtGui.QApplication.UnicodeUTF8))

from core.views.basic.treeview import FileSystemTreeView
