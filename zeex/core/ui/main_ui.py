# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Jan 22 19:23:00 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(1129, 901)
        self.HomeWidget = QtGui.QWidget(HomeWindow)
        self.HomeWidget.setObjectName("HomeWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.HomeWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnOpenProject = QtGui.QPushButton(self.HomeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenProject.sizePolicy().hasHeightForWidth())
        self.btnOpenProject.setSizePolicy(sizePolicy)
        self.btnOpenProject.setObjectName("btnOpenProject")
        self.gridLayout.addWidget(self.btnOpenProject, 0, 1, 1, 1)
        self.labelFiles = QtGui.QLabel(self.HomeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFiles.sizePolicy().hasHeightForWidth())
        self.labelFiles.setSizePolicy(sizePolicy)
        self.labelFiles.setObjectName("labelFiles")
        self.gridLayout.addWidget(self.labelFiles, 1, 0, 1, 1)
        self.comboBoxProject = QtGui.QComboBox(self.HomeWidget)
        self.comboBoxProject.setMinimumSize(QtCore.QSize(350, 0))
        self.comboBoxProject.setMaximumSize(QtCore.QSize(500, 16777215))
        self.comboBoxProject.setObjectName("comboBoxProject")
        self.gridLayout.addWidget(self.comboBoxProject, 0, 2, 1, 1)
        self.btnOpenFile = QtGui.QPushButton(self.HomeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenFile.sizePolicy().hasHeightForWidth())
        self.btnOpenFile.setSizePolicy(sizePolicy)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.gridLayout.addWidget(self.btnOpenFile, 1, 1, 1, 1)
        self.comboBoxFile = QtGui.QComboBox(self.HomeWidget)
        self.comboBoxFile.setMaximumSize(QtCore.QSize(500, 16777215))
        self.comboBoxFile.setObjectName("comboBoxFile")
        self.gridLayout.addWidget(self.comboBoxFile, 1, 2, 1, 1)
        self.labelProjects = QtGui.QLabel(self.HomeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProjects.sizePolicy().hasHeightForWidth())
        self.labelProjects.setSizePolicy(sizePolicy)
        self.labelProjects.setObjectName("labelProjects")
        self.gridLayout.addWidget(self.labelProjects, 0, 0, 1, 1)
        self.labelFilter = QtGui.QLabel(self.HomeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFilter.sizePolicy().hasHeightForWidth())
        self.labelFilter.setSizePolicy(sizePolicy)
        self.labelFilter.setObjectName("labelFilter")
        self.gridLayout.addWidget(self.labelFilter, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.lineEditFilter = QtGui.QLineEdit(self.HomeWidget)
        self.lineEditFilter.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.gridLayout.addWidget(self.lineEditFilter, 2, 2, 1, 1)
        self.btnClearFilter = QtGui.QPushButton(self.HomeWidget)
        self.btnClearFilter.setObjectName("btnClearFilter")
        self.gridLayout.addWidget(self.btnClearFilter, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = FileSystemTreeView(self.HomeWidget)
        self.treeView.setMaximumSize(QtCore.QSize(350, 16777215))
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.treeView_2 = QtGui.QTreeView(self.HomeWidget)
        self.treeView_2.setObjectName("treeView_2")
        self.horizontalLayout.addWidget(self.treeView_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        HomeWindow.setCentralWidget(self.HomeWidget)
        self.homemenu = QtGui.QMenuBar(HomeWindow)
        self.homemenu.setGeometry(QtCore.QRect(0, 0, 1129, 21))
        self.homemenu.setObjectName("homemenu")
        self.menuProjects = QtGui.QMenu(self.homemenu)
        self.menuProjects.setObjectName("menuProjects")
        self.menuActions = QtGui.QMenu(self.homemenu)
        self.menuActions.setObjectName("menuActions")
        self.menuSettings = QtGui.QMenu(self.homemenu)
        self.menuSettings.setObjectName("menuSettings")
        HomeWindow.setMenuBar(self.homemenu)
        self.statusbar = QtGui.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(HomeWindow)
        self.toolBar.setObjectName("toolBar")
        HomeWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpenProject = QtGui.QAction(HomeWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/standard_icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenProject.setIcon(icon)
        self.actionOpenProject.setObjectName("actionOpenProject")
        self.actionNewProject = QtGui.QAction(HomeWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/standard_icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewProject.setIcon(icon1)
        self.actionNewProject.setObjectName("actionNewProject")
        self.actionSaveFile = QtGui.QAction(HomeWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/standard_icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveFile.setIcon(icon2)
        self.actionSaveFile.setObjectName("actionSaveFile")
        self.actionEdit = QtGui.QAction(HomeWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/standard_icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon3)
        self.actionEdit.setObjectName("actionEdit")
        self.actionGeneralSettings = QtGui.QAction(HomeWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/standard_icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGeneralSettings.setIcon(icon4)
        self.actionGeneralSettings.setObjectName("actionGeneralSettings")
        self.actionZip = QtGui.QAction(HomeWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/standard_icons/archive.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionZip.setIcon(icon5)
        self.actionZip.setObjectName("actionZip")
        self.actionViewCloud = QtGui.QAction(HomeWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/standard_icons/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewCloud.setIcon(icon6)
        self.actionViewCloud.setObjectName("actionViewCloud")
        self.actionUnzip = QtGui.QAction(HomeWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/standard_icons/unzip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnzip.setIcon(icon7)
        self.actionUnzip.setObjectName("actionUnzip")
        self.actionSQL = QtGui.QAction(HomeWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/standard_icons/sql.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSQL.setIcon(icon8)
        self.actionSQL.setObjectName("actionSQL")
        self.actionProjectSettings = QtGui.QAction(HomeWindow)
        self.actionProjectSettings.setIcon(icon4)
        self.actionProjectSettings.setObjectName("actionProjectSettings")
        self.actionRename = QtGui.QAction(HomeWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/standard_icons/rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon9)
        self.actionRename.setObjectName("actionRename")
        self.actionOpenSheet = QtGui.QAction(HomeWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/standard_icons/spreadsheet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenSheet.setIcon(icon10)
        self.actionOpenSheet.setObjectName("actionOpenSheet")
        self.actionImportSheet = QtGui.QAction(HomeWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/standard_icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImportSheet.setIcon(icon11)
        self.actionImportSheet.setObjectName("actionImportSheet")
        self.actionPurgeFile = QtGui.QAction(HomeWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/standard_icons/suppress.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPurgeFile.setIcon(icon12)
        self.actionPurgeFile.setObjectName("actionPurgeFile")
        self.actionMergePurge = QtGui.QAction(HomeWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/standard_icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMergePurge.setIcon(icon13)
        self.actionMergePurge.setObjectName("actionMergePurge")
        self.actionFTP = QtGui.QAction(HomeWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/standard_icons/ftp.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionFTP.setIcon(icon14)
        self.actionFTP.setObjectName("actionFTP")
        self.menuProjects.addAction(self.actionOpenProject)
        self.menuProjects.addAction(self.actionNewProject)
        self.menuProjects.addAction(self.actionSaveFile)
        self.menuProjects.addAction(self.actionEdit)
        self.menuActions.addAction(self.actionFTP)
        self.menuActions.addAction(self.actionImportSheet)
        self.menuActions.addAction(self.actionMergePurge)
        self.menuActions.addAction(self.actionPurgeFile)
        self.menuActions.addAction(self.actionRename)
        self.menuActions.addAction(self.actionSQL)
        self.menuActions.addAction(self.actionViewCloud)
        self.menuActions.addAction(self.actionUnzip)
        self.menuActions.addAction(self.actionZip)
        self.menuSettings.addAction(self.actionProjectSettings)
        self.menuSettings.addAction(self.actionGeneralSettings)
        self.homemenu.addAction(self.menuProjects.menuAction())
        self.homemenu.addAction(self.menuActions.menuAction())
        self.homemenu.addAction(self.menuSettings.menuAction())
        self.toolBar.addAction(self.actionOpenProject)
        self.toolBar.addAction(self.actionNewProject)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImportSheet)
        self.toolBar.addAction(self.actionRename)
        self.toolBar.addAction(self.actionOpenSheet)
        self.toolBar.addAction(self.actionPurgeFile)
        self.toolBar.addAction(self.actionMergePurge)
        self.toolBar.addAction(self.actionSaveFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZip)
        self.toolBar.addAction(self.actionUnzip)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSQL)
        self.toolBar.addAction(self.actionViewCloud)
        self.toolBar.addAction(self.actionFTP)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QtGui.QApplication.translate("HomeWindow", "Zeex Home", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOpenProject.setText(QtGui.QApplication.translate("HomeWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFiles.setText(QtGui.QApplication.translate("HomeWindow", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOpenFile.setText(QtGui.QApplication.translate("HomeWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProjects.setText(QtGui.QApplication.translate("HomeWindow", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFilter.setText(QtGui.QApplication.translate("HomeWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClearFilter.setText(QtGui.QApplication.translate("HomeWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProjects.setTitle(QtGui.QApplication.translate("HomeWindow", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("HomeWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("HomeWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("HomeWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenProject.setText(QtGui.QApplication.translate("HomeWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenProject.setToolTip(QtGui.QApplication.translate("HomeWindow", "Open the selected project.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenProject.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setText(QtGui.QApplication.translate("HomeWindow", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setToolTip(QtGui.QApplication.translate("HomeWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFile.setText(QtGui.QApplication.translate("HomeWindow", "Save File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFile.setToolTip(QtGui.QApplication.translate("HomeWindow", "Sync the currently selected file to disk", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setText(QtGui.QApplication.translate("HomeWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeneralSettings.setText(QtGui.QApplication.translate("HomeWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeneralSettings.setToolTip(QtGui.QApplication.translate("HomeWindow", "Open general settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZip.setText(QtGui.QApplication.translate("HomeWindow", "Zip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZip.setToolTip(QtGui.QApplication.translate("HomeWindow", "Zip the currently selected file/folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZip.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewCloud.setText(QtGui.QApplication.translate("HomeWindow", "View Cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewCloud.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnzip.setText(QtGui.QApplication.translate("HomeWindow", "Unzip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSQL.setText(QtGui.QApplication.translate("HomeWindow", "SQL", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSQL.setToolTip(QtGui.QApplication.translate("HomeWindow", "Open SQL manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSQL.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProjectSettings.setText(QtGui.QApplication.translate("HomeWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProjectSettings.setToolTip(QtGui.QApplication.translate("HomeWindow", "View project settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setText(QtGui.QApplication.translate("HomeWindow", "Rename Path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setToolTip(QtGui.QApplication.translate("HomeWindow", "Rename a file or folder.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSheet.setText(QtGui.QApplication.translate("HomeWindow", "Open Sheet", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSheet.setToolTip(QtGui.QApplication.translate("HomeWindow", "Open the selected sheet", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSheet.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportSheet.setText(QtGui.QApplication.translate("HomeWindow", "Import Sheet", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportSheet.setToolTip(QtGui.QApplication.translate("HomeWindow", "Import a file to the current project\'s folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportSheet.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPurgeFile.setText(QtGui.QApplication.translate("HomeWindow", "Purge File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPurgeFile.setToolTip(QtGui.QApplication.translate("HomeWindow", "Opens settings to purge the selected file path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPurgeFile.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergePurge.setText(QtGui.QApplication.translate("HomeWindow", "Merge/Purge", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergePurge.setToolTip(QtGui.QApplication.translate("HomeWindow", "Opens Merge/Purge settings for the selected sheet", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergePurge.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFTP.setText(QtGui.QApplication.translate("HomeWindow", "FTP", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFTP.setToolTip(QtGui.QApplication.translate("HomeWindow", "Open the FTP Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFTP.setShortcut(QtGui.QApplication.translate("HomeWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))

from zeex.core.views.basic.treeview import FileSystemTreeView
from zeex.icons import icons_rc
