# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgimport.ui'
#
# Created: Sat May 19 23:24:12 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DlgImporter(object):
    def setupUi(self, DlgImporter):
        DlgImporter.setObjectName("DlgImporter")
        DlgImporter.resize(534, 484)
        self.verticalLayout_5 = QtGui.QVBoxLayout(DlgImporter)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackMain = QtGui.QStackedWidget(DlgImporter)
        self.stackMain.setObjectName("stackMain")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grpboxFileSel = QtGui.QGroupBox(self.page_3)
        self.grpboxFileSel.setObjectName("grpboxFileSel")
        self.verticalLayout = QtGui.QVBoxLayout(self.grpboxFileSel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbtnFile = QtGui.QRadioButton(self.grpboxFileSel)
        self.rbtnFile.setObjectName("rbtnFile")
        self.horizontalLayout_3.addWidget(self.rbtnFile)
        self.rbtnFolder = QtGui.QRadioButton(self.grpboxFileSel)
        self.rbtnFolder.setChecked(True)
        self.rbtnFolder.setObjectName("rbtnFolder")
        self.horizontalLayout_3.addWidget(self.rbtnFolder)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.stackFileSel = QtGui.QStackedWidget(self.grpboxFileSel)
        self.stackFileSel.setObjectName("stackFileSel")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edFile = QtGui.QLineEdit(self.page)
        self.edFile.setObjectName("edFile")
        self.horizontalLayout_2.addWidget(self.edFile)
        self.tbtnFileSel = QtGui.QToolButton(self.page)
        self.tbtnFileSel.setObjectName("tbtnFileSel")
        self.horizontalLayout_2.addWidget(self.tbtnFileSel)
        self.stackFileSel.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edFolder = QtGui.QLineEdit(self.page_2)
        self.edFolder.setObjectName("edFolder")
        self.horizontalLayout.addWidget(self.edFolder)
        self.tbtnFolderSel = QtGui.QToolButton(self.page_2)
        self.tbtnFolderSel.setObjectName("tbtnFolderSel")
        self.horizontalLayout.addWidget(self.tbtnFolderSel)
        self.stackFileSel.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackFileSel)
        self.verticalLayout_2.addWidget(self.grpboxFileSel)
        self.grpboxRuntime = QtGui.QGroupBox(self.page_3)
        self.grpboxRuntime.setObjectName("grpboxRuntime")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.grpboxRuntime)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edRuntime = QtGui.QLineEdit(self.grpboxRuntime)
        self.edRuntime.setObjectName("edRuntime")
        self.horizontalLayout_4.addWidget(self.edRuntime)
        self.tbtnRuntimeSel = QtGui.QToolButton(self.grpboxRuntime)
        self.tbtnRuntimeSel.setObjectName("tbtnRuntimeSel")
        self.horizontalLayout_4.addWidget(self.tbtnRuntimeSel)
        self.verticalLayout_2.addWidget(self.grpboxRuntime)
        self.grpboxParamDef = QtGui.QGroupBox(self.page_3)
        self.grpboxParamDef.setCheckable(True)
        self.grpboxParamDef.setChecked(False)
        self.grpboxParamDef.setObjectName("grpboxParamDef")
        self.gridLayout = QtGui.QGridLayout(self.grpboxParamDef)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.grpboxParamDef)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edDefnFile = QtGui.QLineEdit(self.grpboxParamDef)
        self.edDefnFile.setObjectName("edDefnFile")
        self.horizontalLayout_5.addWidget(self.edDefnFile)
        self.tbtnDefnFileSel = QtGui.QToolButton(self.grpboxParamDef)
        self.tbtnDefnFileSel.setObjectName("tbtnDefnFileSel")
        self.horizontalLayout_5.addWidget(self.tbtnDefnFileSel)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.grpboxParamDef)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.edImportFolder = QtGui.QLineEdit(self.grpboxParamDef)
        self.edImportFolder.setObjectName("edImportFolder")
        self.horizontalLayout_7.addWidget(self.edImportFolder)
        self.tbtnImportFolderSel = QtGui.QToolButton(self.grpboxParamDef)
        self.tbtnImportFolderSel.setObjectName("tbtnImportFolderSel")
        self.horizontalLayout_7.addWidget(self.tbtnImportFolderSel)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.grpboxParamDef)
        self.grpboxDataType = QtGui.QGroupBox(self.page_3)
        self.grpboxDataType.setCheckable(True)
        self.grpboxDataType.setChecked(False)
        self.grpboxDataType.setObjectName("grpboxDataType")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.grpboxDataType)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtGui.QLabel(self.grpboxDataType)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.cboxDataType = QtGui.QComboBox(self.grpboxDataType)
        self.cboxDataType.setObjectName("cboxDataType")
        self.horizontalLayout_6.addWidget(self.cboxDataType)
        spacerItem1 = QtGui.QSpacerItem(157, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)
        self.horizontalLayout_6.setStretch(2, 2)
        self.verticalLayout_2.addWidget(self.grpboxDataType)
        spacerItem2 = QtGui.QSpacerItem(20, 86, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnHelp = QtGui.QPushButton(self.page_3)
        self.btnHelp.setObjectName("btnHelp")
        self.horizontalLayout_8.addWidget(self.btnHelp)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.btnDiscard = QtGui.QPushButton(self.page_3)
        self.btnDiscard.setObjectName("btnDiscard")
        self.horizontalLayout_8.addWidget(self.btnDiscard)
        spacerItem4 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.btnReset = QtGui.QPushButton(self.page_3)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout_8.addWidget(self.btnReset)
        self.btnImport = QtGui.QPushButton(self.page_3)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_8.addWidget(self.btnImport)
        self.horizontalLayout_8.setStretch(1, 10)
        self.horizontalLayout_8.setStretch(2, 3)
        self.horizontalLayout_8.setStretch(3, 1)
        self.horizontalLayout_8.setStretch(4, 3)
        self.horizontalLayout_8.setStretch(5, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1000)
        self.verticalLayout_2.setStretch(5, 1)
        self.stackMain.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pltxtLog = QtGui.QPlainTextEdit(self.page_4)
        self.pltxtLog.setObjectName("pltxtLog")
        self.verticalLayout_4.addWidget(self.pltxtLog)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.btnBack = QtGui.QPushButton(self.page_4)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout_9.addWidget(self.btnBack)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.stackMain.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtGui.QScrollArea(self.page_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 514, 433))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblHelp = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblHelp.setText("")
        self.lblHelp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblHelp.setWordWrap(True)
        self.lblHelp.setObjectName("lblHelp")
        self.verticalLayout_6.addWidget(self.lblHelp)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.btnCloseHelp = QtGui.QPushButton(self.page_5)
        self.btnCloseHelp.setObjectName("btnCloseHelp")
        self.horizontalLayout_10.addWidget(self.btnCloseHelp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.setStretch(0, 1000)
        self.verticalLayout_3.setStretch(1, 1)
        self.stackMain.addWidget(self.page_5)
        self.verticalLayout_5.addWidget(self.stackMain)

        self.retranslateUi(DlgImporter)
        self.stackMain.setCurrentIndex(0)
        self.stackFileSel.setCurrentIndex(1)
        QtCore.QObject.connect(self.btnCloseHelp, QtCore.SIGNAL("clicked()"), DlgImporter.closeHelp)
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), DlgImporter.goBack)
        QtCore.QObject.connect(self.btnDiscard, QtCore.SIGNAL("clicked()"), DlgImporter.accept)
        QtCore.QObject.connect(self.btnReset, QtCore.SIGNAL("clicked()"), DlgImporter.reset)
        QtCore.QObject.connect(self.btnImport, QtCore.SIGNAL("clicked()"), DlgImporter.go)
        QtCore.QObject.connect(self.tbtnFileSel, QtCore.SIGNAL("clicked()"), DlgImporter.selectFile)
        QtCore.QObject.connect(self.tbtnRuntimeSel, QtCore.SIGNAL("clicked()"), DlgImporter.selectRuntime)
        QtCore.QObject.connect(self.tbtnDefnFileSel, QtCore.SIGNAL("clicked()"), DlgImporter.selectDefnFile)
        QtCore.QObject.connect(self.tbtnImportFolderSel, QtCore.SIGNAL("clicked()"), DlgImporter.selectImportFolder)
        QtCore.QObject.connect(self.tbtnFolderSel, QtCore.SIGNAL("clicked()"), DlgImporter.selectFolder)
        QtCore.QObject.connect(self.rbtnFile, QtCore.SIGNAL("clicked(bool)"), DlgImporter.showFilePage)
        QtCore.QObject.connect(self.rbtnFolder, QtCore.SIGNAL("clicked(bool)"), DlgImporter.showFolderPage)
        QtCore.QObject.connect(self.btnHelp, QtCore.SIGNAL("clicked()"), DlgImporter.showHelp)
        QtCore.QMetaObject.connectSlotsByName(DlgImporter)

    def retranslateUi(self, DlgImporter):
        DlgImporter.setWindowTitle(QtGui.QApplication.translate("DlgImporter", "ARES CSV Data Importer", None, QtGui.QApplication.UnicodeUTF8))
        self.grpboxFileSel.setTitle(QtGui.QApplication.translate("DlgImporter", "File or folder of files to get the data to import into ARES:", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtnFile.setToolTip(QtGui.QApplication.translate("DlgImporter", "Select one file, or enter a file name template, including the full path, (check the documentation on wildcard usage)", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtnFile.setText(QtGui.QApplication.translate("DlgImporter", "File(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtnFolder.setToolTip(QtGui.QApplication.translate("DlgImporter", "Select a folder and take all .dat files from there", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtnFolder.setText(QtGui.QApplication.translate("DlgImporter", "Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.tbtnFileSel.setText(QtGui.QApplication.translate("DlgImporter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tbtnFolderSel.setText(QtGui.QApplication.translate("DlgImporter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.grpboxRuntime.setTitle(QtGui.QApplication.translate("DlgImporter", "ARES Runtime directory", None, QtGui.QApplication.UnicodeUTF8))
        self.tbtnRuntimeSel.setText(QtGui.QApplication.translate("DlgImporter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.grpboxParamDef.setTitle(QtGui.QApplication.translate("DlgImporter", "Specify new parameter definition", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DlgImporter", "Definition file:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbtnDefnFileSel.setText(QtGui.QApplication.translate("DlgImporter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DlgImporter", "Import folder", None, QtGui.QApplication.UnicodeUTF8))
        self.tbtnImportFolderSel.setText(QtGui.QApplication.translate("DlgImporter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.grpboxDataType.setTitle(QtGui.QApplication.translate("DlgImporter", "Assume the same data type for all the files:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DlgImporter", "Data type:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHelp.setText(QtGui.QApplication.translate("DlgImporter", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDiscard.setText(QtGui.QApplication.translate("DlgImporter", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnReset.setText(QtGui.QApplication.translate("DlgImporter", "&Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.btnImport.setText(QtGui.QApplication.translate("DlgImporter", "&Import", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBack.setText(QtGui.QApplication.translate("DlgImporter", "&Back", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCloseHelp.setText(QtGui.QApplication.translate("DlgImporter", "&Back", None, QtGui.QApplication.UnicodeUTF8))

