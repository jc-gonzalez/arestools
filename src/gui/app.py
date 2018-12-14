#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
'''

# make print & unicode backwards compatible
from __future__ import print_function
from __future__ import unicode_literals

from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import simpledialog as SimpleDialog
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font as tkFont

from tkinter import ttk

# used to check if functions have a parameter
from inspect import getfullargspec as getArgs
PYTHON2 = False
PY_NAME = "python3"
STRING = str

# import other useful classes
import os, sys
import time
import datetime
import logging
import argparse

import subprocess
import configparser
import json

from .simpleeditor import launch_modal_editor
from .gui_elements import EntrySpinbox, YMDSpinboxes,  YDoYSpinboxes,  HMSmsSpinboxes, DateTime, StatusBar, CustomText

# details
__author__ = "J C Gonzalez"
__copyright__ = "Copyright 2015-2019, J C Gonzalez"
__license__ = "LGPL 3.0"
__version__ = "0.1"
__maintainer__ = "J C Gonzalez"
__email__ = "jcgonzalez@sciops.esa.int"
__status__ = "Development"
#__url__ = ""


RetrievalConfigFile = './retrieval_config.ini'
ImportConfigFile = './import_config.json'


def getContentOfFile(file=None):
    '''
    Gets the content of a text file
    '''
    with open(file, 'r') as f:
        return f.read()

def run(command):
    '''
    Executes a command and returns the list of lines in stdout
    '''
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while True:
        line = process.stdout.readline() #.rstrip()
        if not line:
            break
        yield line.decode('utf-8')


class App:
    '''
    Main application class for the GUI
    '''
    def __init__(self, parent):
        '''
        Initialize the class
        '''
        self.parent = parent

        #=== Variables

        self.from_pid, self.to_pid, self.pids_step = (0, 0, 0)
        self.retrieval_params = {}

        self.retrieveConfigFile = StringVar()
        self.retrieveConfigFile.set(RetrievalConfigFile)

        self.importConfigFile = StringVar()
        self.importConfigFile.set(ImportConfigFile)

        self.retrFromPid = StringVar()
        self.retrFromPid.set(1)

        self.retrToPid = StringVar()
        self.retrToPid.set(100)

        self.retrPidBlk = StringVar()
        self.retrPidBlk.set(10)

        #=== Dialog menu bar

        menu = Menu(parent)
        parent.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New', command=self.menuCallback)
        filemenu.add_command(label='Open...', command=self.menuCallback)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=self.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='Help...', command=self.help)
        helpmenu.add_separator()
        helpmenu.add_command(label='About...', command=self.about)

        #=== Main GUI structure - notebook

        self.notebook = ttk.Notebook(parent, name='notebook')

        #======================================================================
        #=== 1 - Retrieval from ARES
        #======================================================================

        # Tab 0 - Retrieve from ARES
        tab0 = ttk.Frame(self.notebook)
        self.notebook.add(tab0, text='Retrieve from ARES')
        self.notebook.pack(fill='both', expand=Y, side='top', padx=2, pady=2)

        #----- First section - Show config file name
        frm11 = ttk.Frame(tab0)
        ttk.Label(frm11, text='Applicable retrieval config. file:').pack(side=LEFT, padx=2, pady=2)
        self.retrCfgFileShow = ttk.Entry(frm11, textvariable=self.retrieveConfigFile,state='readonly')
        self.retrCfgFileShow.pack(side=LEFT, expand=1, fill=X, padx=2, pady=2)

        #----- Second section - Retrieval parameters

        lfrm11 = ttk.LabelFrame(tab0, text='Retrieval parameters')

        frm111 = ttk.Frame(lfrm11)
        frm112 = ttk.Frame(lfrm11)

        self.spbxFromPid = EntrySpinbox(frm111, label='From Param Id.:', first=1, last=50000)
        self.spbxFromPid.set(self.retrFromPid.get())
        self.spbxFromPid.pack(side=LEFT, fill=X, expand=Y)
        self.spbxToPid = EntrySpinbox(frm111, label='To Param Id.:', first=1, last=50000)
        self.spbxToPid.set(self.retrToPid.get())
        self.spbxToPid.pack(side=RIGHT, fill=X, expand=Y)

        self.spbxPidsBlock = EntrySpinbox(frm112, label='Param. Ids. block size (for FITS files)',
                                          first=1, last=50000)
        self.spbxPidsBlock.set(self.retrPidBlk.get())
        self.spbxPidsBlock.pack(side=LEFT, fill=X, expand=Y)
        ttk.Label(frm112, text='', width=20).pack(side=LEFT, fill=X, expand=Y)

        frm111.pack(fill=X, expand=Y)
        frm112.pack(fill=X, expand=Y)

        #----- Third section - Date range

        lfrm12 = ttk.LabelFrame(tab0, text='Date range')

        ttk.Label(lfrm12, text='From timestamp:').grid(row=0, column=0, padx=2, pady=2, sticky=N+W)
        self.fromDateTime = DateTime(lfrm12)
        self.fromDateTime.grid(row=0, column=1, padx=2, pady=10)

        ttk.Label(lfrm12, text='To timestamp:').grid(row=1, column=0, padx=2, pady=2, sticky=N+W)
        self.toDateTime = DateTime(lfrm12)
        self.toDateTime.grid(row=1, column=1, padx=2, pady=10)

        #----- Fourth section - button to activate the process

        frm12 = ttk.Frame(tab0)
        ttk.Button(frm12, text=' Retrieve data ', command=self.retrieveData).pack(side=RIGHT)

        #----- Last section - text box to show output

        self.retrOut = Text(tab0)

        #----- Complete packing

        frm11.pack(side=TOP, fill=X, expand=N, padx=2, pady=2)
        lfrm11.pack(fill=BOTH, expand=N, padx=6, pady=6)
        lfrm12.pack(fill=BOTH, expand=N, padx=6, pady=6)
        frm12.pack(fill=BOTH, expand=N, padx=10, pady=10)
        self.retrOut.pack(side=BOTTOM, expand=Y, fill=BOTH)
        self.retrOut.pack_forget()

        #======================================================================
        #=== 2 - Import into ARES
        #======================================================================

        # Tab 1 - Import into ARES
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Import into ARES")
        self.notebook.pack(fill='both', expand=Y, side='top')

        #self.notesBox = Text(tab1, wrap=WORD, width=40, height=10)
        #vscroll = ttk.Scrollbar(tab1, orient=VERTICAL, command=self.notesBox.yview)
        #self.notesBox['yscroll'] = vscroll.set
        #vscroll.pack(side=RIGHT, fill=Y)

        #self.notesBox.pack(fill=BOTH, expand=Y, padx=2, pady=2)

        #----- First section - Show config file name
        frm21 = ttk.Frame(tab1)
        ttk.Label(frm21, text='Applicable import config. file:').pack(side=LEFT, padx=2, pady=2)
        self.imprtCfgFileShow = ttk.Entry(frm21, textvariable=self.importConfigFile,state='readonly')
        self.imprtCfgFileShow.pack(side=LEFT, expand=1, fill=X, padx=2, pady=2)

        #----- Second section - Retrieval parameters

        lfrm21 = ttk.LabelFrame(tab1, text='Input data source')

        self.inputMode = StringVar()
        self.inputDir = StringVar()
        self.inputFiles = StringVar()

        frm211 = ttk.Frame(lfrm21)
        frm212 = ttk.Frame(lfrm21)
        
        rbtnInp0 = ttk.Radiobutton(frm211, text='Input directory', command=self.useInputDir,
                                   variable=self.inputMode, value='dir', width=10)
        rbtnInp0.pack(side=LEFT, padx=10, pady=2, expand=Y, fill=X)
        self.edInputDir = ttk.Entry(frm211, textvariable=self.inputDir)
        self.edInputDir.pack(side=LEFT, padx=2, pady=2, expand=Y, fill=X)
        ttk.Button(frm211, text='...', command=self.setInputDir, width=2)\
            .pack(side=RIGHT, padx=2, pady=2)
        frm211.pack(expand=Y, fill=X)
        
        rbtnInp1 = ttk.Radiobutton(frm212, text='Input files', command=self.useInputFiles,
                                   variable=self.inputMode, value='files', width=10)
        rbtnInp1.pack(side=LEFT, padx=10, pady=2, expand=Y, fill=X)
        self.edInputFiles = ttk.Entry(frm212, textvariable=self.inputFiles)
        self.edInputFiles.pack(side=LEFT, padx=2, pady=2, expand=Y, fill=X)
        ttk.Button(frm212, text='...', command=self.setInputFiles, width=2)\
            .pack(side=RIGHT, padx=2, pady=2)
        frm212.pack(expand=Y, fill=X)

        self.inputMode.set('dir')

        #----- Third section - Retrieval parameters

        lfrm22 = ttk.LabelFrame(tab1, text='ARES Runtime directory')

        self.aresRunTime = StringVar()
        if 'ARES_RUNTIME' in os.environ:
            self.aresRunTime = os.environ['ARES_RUNTIME']
            
        self.edAresRunTime = ttk.Entry(lfrm22, textvariable=self.aresRunTime)
        self.edAresRunTime.pack(side=LEFT, expand=Y, fill=X, padx=2, pady=2)
        ttk.Button(lfrm22, text='...', command=self.setAresRunTime, width=2)\
            .pack(side=RIGHT, padx=2, pady=2)

        #----- Fourth section - Retrieval parameters

        lfrm23 = ttk.LabelFrame(tab1, text='New parameter description')

        frm231 = ttk.Frame(lfrm23)
        frm232 = ttk.Frame(lfrm23)
        frm233 = ttk.Frame(lfrm23)

        self.useParamDescripFile = StringVar()
        self.descFile = StringVar()
        self.paramImpFolder = StringVar()

        chkUseDescFile = ttk.Checkbutton(frm231, text="Use parameter description file", 
	                                 command=self.changedUseParamDescFile,
                                         variable=self.useParamDescripFile,
	                                 onvalue='yes', offvalue='no')
        chkUseDescFile.pack(side=LEFT, pady=2)
        frm231.pack(expand=Y, fill=X)
        
        ttk.Label(frm232, text="Description file: ")\
           .pack(side=LEFT, padx=10, pady=2)
        self.edDescripFile = ttk.Entry(frm232, textvariable=self.descFile)
        self.edDescripFile.pack(side=LEFT, expand=Y, fill=X, padx=2, pady=2)
        ttk.Button(frm232, text='...', command=self.setAresRunTime, width=2)\
            .pack(side=RIGHT, padx=2, pady=2)
        frm232.pack(expand=Y, fill=X)

        ttk.Label(frm233, text="Parameter import folder: ")\
           .pack(side=LEFT, padx=10, pady=2)
        self.edParImportFolder = ttk.Entry(frm233, textvariable=self.paramImpFolder)
        self.edParImportFolder.pack(side=LEFT, expand=Y, fill=X, padx=2, pady=2)
        #ttk.Button(frm232, text='...', command=self.setAresRunTime, width=2)\
        #    .pack(side=RIGHT, padx=2, pady=2)
        frm233.pack(expand=Y, fill=X)

        #----- Fifth section - Retrieval parameters

        lfrm24 = ttk.LabelFrame(tab1, text='Import data types')

        frm241 = ttk.Frame(lfrm24)
        frm242 = ttk.Frame(lfrm24)

        self.useSameParamDataType = StringVar()
        self.paramDataType = StringVar()

        chkUseSameParamDataType = ttk.Checkbutton(frm241, text="Assume same data type for all import data files", 
	                                          command=self.changedUseSameParamDataType,
                                                  variable=self.useSameParamDataType,
	                                          onvalue='yes', offvalue='no')
        chkUseSameParamDataType.pack(side=LEFT, pady=2)
        frm241.pack(expand=Y, fill=X)
        
        ttk.Label(frm242, text="Parameter data type: ")\
           .pack(side=LEFT, padx=10, pady=2)
        self.cboxParamDataType = ttk.Combobox(frm242, textvariable=self.paramDataType)
        self.cboxParamDataType.pack(side=LEFT, expand=Y, fill=X, padx=2, pady=2)
        self.cboxParamDataType['values'] = ('uno', 'dos', 'tres')
        frm242.pack(expand=Y, fill=X)

        #----- Sixth section - button to activate the process

        frm22 = ttk.Frame(tab1)
        ttk.Button(frm22, text=' Import data ', command=self.importData).pack(side=RIGHT)

        #----- Last section - text box to show output

        self.imprtOut = Text(tab1)

        #----- Complete packing

        frm21.pack(side=TOP, fill=X, expand=N, padx=2, pady=2)
        lfrm21.pack(fill=BOTH, expand=N, padx=6, pady=6)
        lfrm22.pack(fill=BOTH, expand=N, padx=6, pady=6)
        lfrm23.pack(fill=BOTH, expand=N, padx=6, pady=6)
        lfrm24.pack(fill=BOTH, expand=N, padx=6, pady=6)
        frm22.pack(fill=BOTH, expand=N, padx=10, pady=10)
        self.imprtOut.pack(side=BOTTOM, expand=Y, fill=BOTH)
        self.imprtOut.pack_forget()

        #======================================================================
        #=== 3 - Configuration
        #======================================================================

        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab2, text="Configuration files")
        self.notebook.pack(fill='both', expand=Y, side='top')

        #----- 3.1 Retrieval configuration

        lfrm31 = ttk.LabelFrame(tab2, text='Retrieval configuration')

        frm311 = ttk.Frame(lfrm31)
        self.showRetrCfgFileName = ttk.Entry(frm311, textvariable=self.retrieveConfigFile)
        self.showRetrCfgFileName.pack(side=LEFT, expand=Y, fill=X, padx=2, pady=6)
        ttk.Button(frm311, text='...', command=self.setRetrCfgFileName, width=2)\
           .pack(side=RIGHT, padx=2, pady=6, expand=N)

        frm312 = ttk.Frame(lfrm31)
        self.txtRetrCfg = Text(frm312, wrap=WORD, width=40, height=10)
        vscroll1 = ttk.Scrollbar(frm312, orient=VERTICAL, command=self.txtRetrCfg.yview)
        self.txtRetrCfg['yscroll'] = vscroll1.set
        vscroll1.pack(side=RIGHT, fill=Y)
        self.txtRetrCfg.pack(fill=BOTH, expand=Y, padx=2, pady=2)

        self.txtRetrCfg.insert(END, getContentOfFile(file=self.retrieveConfigFile.get()))

        frm311.pack(side=TOP, expand=N, fill=X, padx=6, pady=6)
        frm312.pack(expand=Y, fill=BOTH, ipadx=10, ipady=10)
        ttk.Button(lfrm31, text='Edit', command=self.editRetrCfg).pack(padx=10, pady=10)

        #----- 3.2 Import configuration

        lfrm32 = ttk.LabelFrame(tab2, text='Import configuration')

        frm321 = ttk.Frame(lfrm32)
        self.showImprtCfgFileName = ttk.Entry(frm321, textvariable=self.importConfigFile)
        self.showImprtCfgFileName.pack(side=LEFT, expand=Y, fill=X, padx=2, pady=6)
        ttk.Button(frm321, text='...', command=self.setImprtCfgFileName, width=2)\
            .pack(side=RIGHT, padx=2, pady=6, expand=N)

        frm322 = ttk.Frame(lfrm32)
        self.txtImprtCfg = Text(frm322, wrap=WORD, width=40, height=10)
        vscroll2 = ttk.Scrollbar(frm322, orient=VERTICAL, command=self.txtImprtCfg.yview)
        self.txtImprtCfg['yscroll'] = vscroll2.set
        vscroll2.pack(side=RIGHT, fill=Y)
        self.txtImprtCfg.pack(fill=BOTH, expand=Y, padx=2, pady=2)

        self.txtImprtCfg.insert(END, getContentOfFile(file=self.importConfigFile.get()))

        frm321.pack(side=TOP, expand=N, fill=X, padx=6, pady=6)
        frm322.pack(side=TOP, expand=Y, fill=BOTH, ipadx=10, ipady=10)
        ttk.Button(lfrm32, text='Edit', command=self.editImprtCfg).pack(padx=10, pady=10)

        #----- Wrap up

        lfrm31.pack(side=LEFT, expand=Y, fill=BOTH, padx=6, pady=6)
        lfrm32.pack(side=LEFT, expand=Y, fill=BOTH, padx=6, pady=6)

        #=== Finally, a status bar

        status = StatusBar(parent)
        status.pack(side=BOTTOM, fill=X)
        status.set("Loaded.")

    def help(self):
        win = Toplevel(self.parent)
        win.title("About")
        hlp = '''Top/bottom 3 - Reports only the top/bottom 3 rows for a param you will later specify.
        Set noise threshold - Filters results with deltas below the specified noise threshold in ps.
        Sort output - Sorts by test,pre,post,unit,delta,abs(delta).
        Top 2 IDD2P/IDD6 registers - Reports only the top 2 IDD2P/IDD6 registers.
        Only critical registers - Reports only critical registers.
        Use tilda output format - Converts the output file from csv to tilda.
        Use html output format - Converts the output file from csv to html.'''
        hlp = re.sub('\n\s*', '\n', hlp) # remove leading whitespace from each line
        t = CustomText(win, wrap='word', width=140, height=40, borderwidth=0)
        t.pack(sid='top',fill='both',expand=True)
        t.tag_configure('blue', foreground='blue')
        t.tag_configure('red', background='red')
        t.tag_configure('important', foreground='red')
        t.insert('1.0', hlp)
        t.insert('end', 'first text', ('important'))
        t.insert('end', 'second text', ('important'))
        t.apply_tag(tag='blue', pattern='^.*? - ')
        t.apply_tag(tag='important', pattern='output', regexp=False)
        ttk.Button(win, text='OK', command=win.destroy).pack()

    def about(self):
        win = Toplevel(self.parent)
        win.title("About")
        t = CustomText(win, wrap='word', width=60, height=9, borderwidth=0)
        t.insert('1.0', 'XAresTools\n', ('title'))
        t.insert(END, 'The AresTools interface\n\n', ('subtitle'))
        t.insert(END, 'This application is a simplified interface to the\n')
        t.insert(END, 'AresTools scripts, to make their use a bit easier.\n\n')
        t.insert(END, 'The Euclid SOC Team at ESAC\n')
        t.pack(sid='top',fill='both',expand=True)
        t.tag_configure('title', font=('Times', 16, 'bold'))
        t.tag_configure('subtitle', font=('Times', 12, 'bold italic'))
        t.tag_configure('centered', justify=CENTER)
        t.apply_tag(tag='centered', pattern='^.')
        ttk.Button(win, text='OK', command=win.destroy).pack()

    def quit(self):
        '''
        Quit the application
        '''
        self.parent.destroy()

    def menuCallback(self, item):
        '''
        Callback for the menu bar menu options
        '''
        pass

    def retrieveData(self):
        '''
        Callback to retrive data from ARES cluster
        '''
        # Get information
        print(json.dumps(self.getRetrievalParams()))
        self.retrOut.delete('1.0', END)
        self.retrOut.pack(expand=Y, fill=BOTH)
        for path in run('find . -name "*.so" -ls'):
            print(path)
            self.retrOut.insert(END, path)

    def editRetrCfg(self):
        '''
        Edit retrieval data from ARES parameter configuration file
        '''
        launch_modal_editor(parent=self.parent, file=self.retrieveConfigFile.get())

    def setRetrCfgFileName(self):
        '''
        Select retrieval config. file name
        '''
        filepath = filedialog.askopenfilename()
        if filepath != None  and filepath != '':
            self.retrieveConfigFile.set(filepath)
            self.txtRetrCfg.delete('1.0', END)
            self.txtRetrCfg.insert(END, getContentOfFile(file=filepath))

    def getRetrievalParams(self):
        '''
        Get JSON object with the current retrieval configuration parameters
        '''
        return {
            'from_pid': self.spbxFromPid.get(),
            'to_pid': self.spbxToPid.get(),
            'pids_step': self.spbxPidsBlock.get(),
            'from_date_time': self.fromDateTime.get(), 
            'to_date_time': self.toDateTime.get()
        }

    def importData(self):
        pass

    def useInputDir(self):
        pass

    def useInputFiles(self):
        pass

    def setInputDir(self):
        pass

    def setInputFiles(self):
        pass

    def setAresRunTime(self):
        pass

    def changedUseParamDescFile(self):
        pass

    def changedUseSameParamDataType(self):
        pass
    
    def editImprtCfg(self):
        '''
        Edit import into ARES parameter configuration file
        '''
        launch_modal_editor(parent=self.parent, file=self.importConfigFile.get())

    def setImprtCfgFileName(self):
        '''
        Select import config. file name
        '''
        filepath = filedialog.askopenfilename()
        if filepath != None  and filepath != '':
            self.importConfigFile.set(filepath)
            self.txtImprtCfg.delete('1.0', END)
            self.txtImprtCfg.insert(END, getContentOfFile(file=filepath))


if __name__ == '__main__':
    print('This is a library class and cannot be executed.')
    sys.exit()
