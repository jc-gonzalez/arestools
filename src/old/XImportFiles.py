#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
XImportFiles.py

Import data files to ARES, using a PySide GUI
'''

from PySide.QtGui import * 
from PySide.QtCore import *

from guitools.dlgimport import Ui_DlgImporter

from ares_import.ares_import import Importer

import sys, os
import logging
import argparse


VERSION = '0.0.1'

__author__ = "jcgonzalez"
__version__ = VERSION
__email__ = "jcgonzalez@sciops.esa.int"
__status__ = "Prototype" # Prototype | Development | Production


TypeRegex = {
   "TC_REQUEST" : { "re" : "^TCRequest", "dir" : "command" },
   "TC_IMPORT" : { "re" : "^TCImport", "dir" : "command" },
   "TC_BRIEF_REQUEST" : { "re" : "^TCBriefRequest", "dir" : "command" },
   "TM_IMPORT" : { "re" : "^TMImport", "dir" : "tmpacket" },
   "MPS_PARAM_IMPORT" : { "re" : "^MpsParam", "dir" : "parameter" },
   "TM_PARAM_REQUEST" : { "re" : "^ParamRequest", "dir" : "parameter/eddsBinary" },
   "BATCH_EVENT_REQUEST" : { "re" : "^BatchRequest.EventRecordReport", "dir" : "s2kevent" },
   "BATCH_PARAM_REQUEST" : { "re" : "^BatchRequest.Param", "dir" : "parameter/eddsBinary" },
   "MPS_EVENT_IMPORT" : { "re" : "^MpsEvent", "dir" : "mpsevent" },
   "TC_UPDATE_IMPORT" : { "re" : "^TCUpdateImport", "dir" : "command" },
   "S2KE_REQUEST" : { "re" : "^S2keRequest", "dir" : "s2kevent" },
   "TM_REQUEST" : { "re" : "^TMReportRequest", "dir" : "tmpacket" },
   "S2KE_IMPORT" : { "re" : "^S2keImport", "dir" : "s2kevent" },
   "TM_PARAM_IMPORT" : { "re" : "^ParamImport", "dir" : "parameter" },
   "TM_PARAM_LCT_REQUEST" : { "re" : "^ParamLctRequest", "dir" : "parameter" },
   "TM_PARAM_DEF_IMPORT" : { "re" : "^TMParamDef", "dir" : "paramdef" }
}

# Change INFO for DEBUG to get debug messages
log_level = logging.INFO

# Set up logging information
format_string = '%(asctime)s %(levelname).1s %(message)s'
logging.basicConfig(level=log_level, format=format_string, stream=sys.stderr)


class MainWindow(QDialog, Ui_DlgImporter): 

    def __init__(self): 
        super(MainWindow, self).__init__() 
        self.setupUi(self) 

        self.lblHelp.setText(
        '''
        <h3>ARES Data Import</h3>
        Imports data from CSV files into ARES

        <h4>Data selection</h4>
        This tool requires:
        <ul><li>One data file to get the data to be imported, or</li>
        <li>One folder, where all the .dat files will be used to read the data to be imported, or</li>
        <li>One file name template, using wildcards</li></ul>
        The final data set will be imported from the resulting or specified files into the ARES system.
        The way the wildcards are used is the same as in the Unix shell command line.

        <h4>ARES Runtime Folder</h4>
        The tool is required to be executed in a machine where the ARES Server is installed and running.
        In the process of installation, a folder to be used as host of the runtime and the server being
        launched is used.  This tool needs to know which is this folder.

        If the folder <code>$HOME/ARES_RUNTIME</code> exists, this is taken as the assumed value for
        the runtime folder name

        <h4>New paramerter definition</h4>
        Usually, we will import data corresponding to an already defined parameter.  But in case we want 
        to create a new parameter to be used by ARES, it requires that a file with the type and
        name definition of this (or these) new parameter(s) is injected into de system, prior to the 
        actual data import.  The entries "Definition file" and "Import folder" define these characteristics,
        the former, and the subdirectory where the data file is to be placed for import, the later.

        <h4>Common data type for all imported files</h4>
        A series of rules (regular expressions) can be used to obtain the parameter type, from the 
        data import file names.  But it is possible to skip this type preemption just by specifying an 
        existing data type, which will be used for all the imported data files.
        ''')

        self.cboxDataType.addItems(TypeRegex.keys())
        self.Home = os.environ['HOME']
        self.AresRuntimeDir = ''
        if os.path.isdir(self.Home + '/ARES_RUNTIME'):
            self.AresRuntimeDir = self.Home + '/ARES_RUNTIME'
        if "ARES_RUNTIME" in os.environ:
            # Nominally, the QPFWA env. variable should point to the QPF Working Area
            # main directory (usually /home/eucops/qpf)
            self.AresRuntimeDir = os.environ["ARES_RUNTIME"]
        self.reset()

        self.show()

    def showHelp(self):
        self.stackMain.setCurrentIndex(2)

    def goBack(self):
        self.stackMain.setCurrentIndex(0)

    def closeHelp(self):
        self.stackMain.setCurrentIndex(0)

    def reset(self):
        self.edFile.setText('')
        self.edFolder.setText('')
        self.edRuntime.setText(self.AresRuntimeDir)
        self.edDefnFile.setText('')
        self.edImportFolder.setText('')

    def go(self):
        args = {}
        args['input'] = self.edFolder.text() if self.rbtnFolder.isChecked() else None
        args['ifile'] = self.edFile.text() if self.rbtnFile.isChecked() else None
        args['runtime'] = self.edRuntime.text()

        if self.grpboxParamDef.isChecked():
            args['defn'] = self.edDefnFile.text()
            args['dir']  = self.edImportFolder.text()
        else:
            args['defn'] = None
            args['dir']  = None

        args['type'] = self.cboxDataType.currentText() if self.grpboxDataType.isChecked() else None

        # self.stackMain.setCurrentIndex(1)

        importer = Importer(data_dir=args['input'], input_file=args['ifile'],
                            def_file=args['defn'], import_dir=args['dir'],
                            ares_runtime=args['runtime'], data_type=args['type'],
                            batch_mode=True)
        importer.set_predef_type_patterns(TypeRegex)
        importer.run_import()

    def selectFile(self):
        pth, _ = QFileDialog.getOpenFileName(self, "Select Data File", os.getcwd())
        self.edFile.setText(pth)

    def selectFolder(self):
        pth = QFileDialog.getExistingDirectory(self, "Select Data Folder", os.getcwd())
        self.edFolder.setText(pth)

    def selectRuntime(self):
        pth = QFileDialog.getExistingDirectory(self, "Select ARES Runtime Folder", os.getcwd())
        self.edRuntime.setText(pth)

    def selectDefnFile(self):
        pth, _ = QFileDialog.getOpenFileName(self, "Select Definition File", os.getcwd())
        self.edDefnFile.setText(pth)

    def selectImportFolder(self):
        pth = QFileDialog.getExistingDirectory(self, "Select Target Import Folder", os.getcwd())
        self.edImportFolder.setText(pth)

    def showFilePage(self, tgl=True):
        self.stackFileSel.setCurrentIndex(0 if tgl else 1)
        self.rbtnFolder.setChecked(not tgl)

    def showFolderPage(self, tgl=True):
        self.stackFileSel.setCurrentIndex(1 if tgl else 0)
        self.rbtnFile.setChecked(not tgl)

        
def main():
    app = QApplication(sys.argv) 
    mainWin = MainWindow() 
    ret = app.exec_() 
    sys.exit( ret ) 

   
if __name__ == "__main__":
    main()
