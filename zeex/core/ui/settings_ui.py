# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sun Jan  1 12:55:38 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(622, 582)
        self.gridLayoutWidget_2 = QtGui.QWidget(settingsDialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 581, 521))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnSave = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 0, 0, 1, 1)
        self.btnImport = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.btnImport.setObjectName("btnImport")
        self.gridLayout.addWidget(self.btnImport, 0, 1, 1, 1)
        self.btnExport = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.btnExport.setObjectName("btnExport")
        self.gridLayout.addWidget(self.btnExport, 0, 2, 1, 1)
        self.btnSetDefault = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.btnSetDefault.setObjectName("btnSetDefault")
        self.gridLayout.addWidget(self.btnSetDefault, 0, 3, 1, 1)
        self.btnReset = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout.addWidget(self.btnReset, 0, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.SettingsTabWidget = QtGui.QTabWidget(self.gridLayoutWidget_2)
        self.SettingsTabWidget.setObjectName("SettingsTabWidget")
        self.GeneralSettingsWidget = QtGui.QWidget()
        self.GeneralSettingsWidget.setObjectName("GeneralSettingsWidget")
        self.formLayoutWidget = QtGui.QWidget(self.GeneralSettingsWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 521, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.GeneralSettingsLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.GeneralSettingsLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.GeneralSettingsLayout.setContentsMargins(0, 0, 0, 0)
        self.GeneralSettingsLayout.setObjectName("GeneralSettingsLayout")
        self.rootDirectoryLabel = QtGui.QLabel(self.formLayoutWidget)
        self.rootDirectoryLabel.setObjectName("rootDirectoryLabel")
        self.GeneralSettingsLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.rootDirectoryLabel)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnRootDirectory = QtGui.QPushButton(self.formLayoutWidget)
        self.btnRootDirectory.setObjectName("btnRootDirectory")
        self.gridLayout_3.addWidget(self.btnRootDirectory, 0, 1, 1, 1)
        self.rootDirectoryLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.rootDirectoryLineEdit.setObjectName("rootDirectoryLineEdit")
        self.gridLayout_3.addWidget(self.rootDirectoryLineEdit, 0, 0, 1, 1)
        self.GeneralSettingsLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.gridLayout_3)
        self.logDirectoryLabel = QtGui.QLabel(self.formLayoutWidget)
        self.logDirectoryLabel.setObjectName("logDirectoryLabel")
        self.GeneralSettingsLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.logDirectoryLabel)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnLogDirectory = QtGui.QPushButton(self.formLayoutWidget)
        self.btnLogDirectory.setObjectName("btnLogDirectory")
        self.gridLayout_4.addWidget(self.btnLogDirectory, 0, 1, 1, 1)
        self.logDirectoryLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.logDirectoryLineEdit.setObjectName("logDirectoryLineEdit")
        self.gridLayout_4.addWidget(self.logDirectoryLineEdit, 0, 0, 1, 1)
        self.GeneralSettingsLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.gridLayout_4)
        self.logLevelLabel = QtGui.QLabel(self.formLayoutWidget)
        self.logLevelLabel.setObjectName("logLevelLabel")
        self.GeneralSettingsLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.logLevelLabel)
        self.logLevelComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.logLevelComboBox.setObjectName("logLevelComboBox")
        self.GeneralSettingsLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.logLevelComboBox)
        self.cloudProviderLabel = QtGui.QLabel(self.formLayoutWidget)
        self.cloudProviderLabel.setObjectName("cloudProviderLabel")
        self.GeneralSettingsLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.cloudProviderLabel)
        self.cloudProviderComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.cloudProviderComboBox.setObjectName("cloudProviderComboBox")
        self.GeneralSettingsLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cloudProviderComboBox)
        self.themeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.themeLabel.setObjectName("themeLabel")
        self.GeneralSettingsLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.themeLabel)
        self.themeComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.themeComboBox.setObjectName("themeComboBox")
        self.GeneralSettingsLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.themeComboBox)
        self.SettingsTabWidget.addTab(self.GeneralSettingsWidget, "")
        self.InputSettingsWidget = QtGui.QWidget()
        self.InputSettingsWidget.setObjectName("InputSettingsWidget")
        self.formLayoutWidget_2 = QtGui.QWidget(self.InputSettingsWidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 281, 371))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.InputSettingsLayout = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.InputSettingsLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.InputSettingsLayout.setContentsMargins(0, 0, 0, 0)
        self.InputSettingsLayout.setObjectName("InputSettingsLayout")
        self.headerCaseLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.headerCaseLabel.setObjectName("headerCaseLabel")
        self.InputSettingsLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.headerCaseLabel)
        self.headerCaseComboBox = QtGui.QComboBox(self.formLayoutWidget_2)
        self.headerCaseComboBox.setObjectName("headerCaseComboBox")
        self.InputSettingsLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.headerCaseComboBox)
        self.headerSpacesLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.headerSpacesLabel.setObjectName("headerSpacesLabel")
        self.InputSettingsLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.headerSpacesLabel)
        self.headerSpacesComboBox = QtGui.QComboBox(self.formLayoutWidget_2)
        self.headerSpacesComboBox.setObjectName("headerSpacesComboBox")
        self.InputSettingsLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.headerSpacesComboBox)
        self.SettingsTabWidget.addTab(self.InputSettingsWidget, "")
        self.outputSettings = QtGui.QWidget()
        self.outputSettings.setObjectName("outputSettings")
        self.formLayoutWidget_3 = QtGui.QWidget(self.outputSettings)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 271, 421))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.outputSettingsFormLayout = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.outputSettingsFormLayout.setContentsMargins(0, 0, 0, 0)
        self.outputSettingsFormLayout.setObjectName("outputSettingsFormLayout")
        self.separatorLabel = QtGui.QLabel(self.formLayoutWidget_3)
        self.separatorLabel.setObjectName("separatorLabel")
        self.outputSettingsFormLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.separatorLabel)
        self.separatorComboBox = QtGui.QComboBox(self.formLayoutWidget_3)
        self.separatorComboBox.setObjectName("separatorComboBox")
        self.outputSettingsFormLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.separatorComboBox)
        self.encodingLabel = QtGui.QLabel(self.formLayoutWidget_3)
        self.encodingLabel.setObjectName("encodingLabel")
        self.outputSettingsFormLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.encodingLabel)
        self.encodingComboBox = QtGui.QComboBox(self.formLayoutWidget_3)
        self.encodingComboBox.setObjectName("encodingComboBox")
        self.outputSettingsFormLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.encodingComboBox)
        self.SettingsTabWidget.addTab(self.outputSettings, "")
        self.gridLayout_2.addWidget(self.SettingsTabWidget, 0, 0, 1, 1)

        self.retranslateUi(settingsDialog)
        self.SettingsTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtGui.QApplication.translate("settingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("settingsDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnImport.setText(QtGui.QApplication.translate("settingsDialog", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExport.setText(QtGui.QApplication.translate("settingsDialog", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSetDefault.setText(QtGui.QApplication.translate("settingsDialog", "Set Default", None, QtGui.QApplication.UnicodeUTF8))
        self.btnReset.setText(QtGui.QApplication.translate("settingsDialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.rootDirectoryLabel.setText(QtGui.QApplication.translate("settingsDialog", "Root Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRootDirectory.setText(QtGui.QApplication.translate("settingsDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.logDirectoryLabel.setText(QtGui.QApplication.translate("settingsDialog", "Log Directory: ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLogDirectory.setText(QtGui.QApplication.translate("settingsDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.logLevelLabel.setText(QtGui.QApplication.translate("settingsDialog", "Log Level", None, QtGui.QApplication.UnicodeUTF8))
        self.cloudProviderLabel.setText(QtGui.QApplication.translate("settingsDialog", "Cloud Provider", None, QtGui.QApplication.UnicodeUTF8))
        self.themeLabel.setText(QtGui.QApplication.translate("settingsDialog", "Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.SettingsTabWidget.setTabText(self.SettingsTabWidget.indexOf(self.GeneralSettingsWidget), QtGui.QApplication.translate("settingsDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.headerCaseLabel.setText(QtGui.QApplication.translate("settingsDialog", "Header Case", None, QtGui.QApplication.UnicodeUTF8))
        self.headerSpacesLabel.setText(QtGui.QApplication.translate("settingsDialog", "Header Spaces", None, QtGui.QApplication.UnicodeUTF8))
        self.SettingsTabWidget.setTabText(self.SettingsTabWidget.indexOf(self.InputSettingsWidget), QtGui.QApplication.translate("settingsDialog", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.separatorLabel.setText(QtGui.QApplication.translate("settingsDialog", "Separator", None, QtGui.QApplication.UnicodeUTF8))
        self.encodingLabel.setText(QtGui.QApplication.translate("settingsDialog", "Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.SettingsTabWidget.setTabText(self.SettingsTabWidget.indexOf(self.outputSettings), QtGui.QApplication.translate("settingsDialog", "Output", None, QtGui.QApplication.UnicodeUTF8))

