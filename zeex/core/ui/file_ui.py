# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created: Mon Jan  9 18:14:46 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FileWindow(object):
    def setupUi(self, FileWindow):
        FileWindow.setObjectName("FileWindow")
        FileWindow.resize(1124, 894)
        self.centralwidget = QtGui.QWidget(FileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        FileWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FileWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        FileWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FileWindow)
        self.statusbar.setObjectName("statusbar")
        FileWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(FileWindow)
        self.toolBar.setObjectName("toolBar")
        FileWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtGui.QAction(FileWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/standard_icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionDelete = QtGui.QAction(FileWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/standard_icons/delete.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/standard_icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName("actionDelete")
        self.actionMergePurge = QtGui.QAction(FileWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/standard_icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMergePurge.setIcon(icon2)
        self.actionMergePurge.setObjectName("actionMergePurge")
        self.actionSuppress = QtGui.QAction(FileWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/standard_icons/suppress.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSuppress.setIcon(icon3)
        self.actionSuppress.setObjectName("actionSuppress")
        self.actionRename = QtGui.QAction(FileWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/standard_icons/rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon4)
        self.actionRename.setObjectName("actionRename")
        self.actionExecuteScript = QtGui.QAction(FileWindow)
        self.actionExecuteScript.setObjectName("actionExecuteScript")
        self.actionEditFields = QtGui.QAction(FileWindow)
        self.actionEditFields.setIcon(icon4)
        self.actionEditFields.setObjectName("actionEditFields")
        self.actionSplit = QtGui.QAction(FileWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/standard_icons/split.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSplit.setIcon(icon5)
        self.actionSplit.setObjectName("actionSplit")
        self.actionAnalyze = QtGui.QAction(FileWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/standard_icons/count.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalyze.setIcon(icon6)
        self.actionAnalyze.setObjectName("actionAnalyze")
        self.actionNormalize = QtGui.QAction(FileWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/standard_icons/normalize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNormalize.setIcon(icon7)
        self.actionNormalize.setObjectName("actionNormalize")
        self.actionSaveAs = QtGui.QAction(FileWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/standard_icons/saveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon8)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionTranspose = QtGui.QAction(FileWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/standard_icons/transpose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTranspose.setIcon(icon9)
        self.actionTranspose.setObjectName("actionTranspose")
        self.actionDropNaN = QtGui.QAction(FileWindow)
        self.actionDropNaN.setObjectName("actionDropNaN")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionDelete)
        self.menuAction.addAction(self.actionAnalyze)
        self.menuAction.addAction(self.actionEditFields)
        self.menuAction.addAction(self.actionExecuteScript)
        self.menuAction.addAction(self.actionMergePurge)
        self.menuAction.addAction(self.actionNormalize)
        self.menuAction.addAction(self.actionSplit)
        self.menuAction.addAction(self.actionSuppress)
        self.menuAction.addAction(self.actionTranspose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMergePurge)
        self.toolBar.addAction(self.actionSplit)
        self.toolBar.addAction(self.actionNormalize)
        self.toolBar.addAction(self.actionEditFields)
        self.toolBar.addAction(self.actionAnalyze)
        self.toolBar.addAction(self.actionTranspose)
        self.toolBar.addAction(self.actionDropNaN)

        self.retranslateUi(FileWindow)
        QtCore.QMetaObject.connectSlotsByName(FileWindow)

    def retranslateUi(self, FileWindow):
        FileWindow.setWindowTitle(QtGui.QApplication.translate("FileWindow", "MyFile", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("FileWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAction.setTitle(QtGui.QApplication.translate("FileWindow", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("FileWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("FileWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("FileWindow", "Save the file to disk.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("FileWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("FileWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setToolTip(QtGui.QApplication.translate("FileWindow", "Deletes the current file from the program and disk!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergePurge.setText(QtGui.QApplication.translate("FileWindow", "Merge/Purge", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergePurge.setShortcut(QtGui.QApplication.translate("FileWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSuppress.setText(QtGui.QApplication.translate("FileWindow", "Suppress", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setText(QtGui.QApplication.translate("FileWindow", "Rename Headers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setShortcut(QtGui.QApplication.translate("FileWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExecuteScript.setText(QtGui.QApplication.translate("FileWindow", "Execute Script", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditFields.setText(QtGui.QApplication.translate("FileWindow", "Edit Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditFields.setShortcut(QtGui.QApplication.translate("FileWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSplit.setText(QtGui.QApplication.translate("FileWindow", "Split", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalyze.setText(QtGui.QApplication.translate("FileWindow", "Analyze", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalyze.setToolTip(QtGui.QApplication.translate("FileWindow", "View statistics on each column.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalyze.setShortcut(QtGui.QApplication.translate("FileWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNormalize.setText(QtGui.QApplication.translate("FileWindow", "Normalize", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNormalize.setToolTip(QtGui.QApplication.translate("FileWindow", "Normalize data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNormalize.setShortcut(QtGui.QApplication.translate("FileWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("FileWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setToolTip(QtGui.QApplication.translate("FileWindow", "Save the file to another path on the disk.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTranspose.setText(QtGui.QApplication.translate("FileWindow", "Transpose", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTranspose.setToolTip(QtGui.QApplication.translate("FileWindow", "Convert rows to columns & vice versa (150 rows max)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTranspose.setShortcut(QtGui.QApplication.translate("FileWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDropNaN.setText(QtGui.QApplication.translate("FileWindow", "Drop NaN", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDropNaN.setToolTip(QtGui.QApplication.translate("FileWindow", "Replaces \'nan\' values with blanks on string fields.", None, QtGui.QApplication.UnicodeUTF8))

from zeex.icons import icons_rc
