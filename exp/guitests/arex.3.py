#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''ImportFiles.py

Import data files to ARES

Usage: ImportFiles.py [-h] [-i INPUT] [-f IFILE] [-D DEF] [-r RUNTIME]
                      [-d DIR] [-t TYPE]

optional arguments:
  -h, --help                        show this help message and exit
  -i INPUT, --input INPUT           Data files directory
  -f IFILE, --files IFILE           Input data file(s) (can include wildcards)
  -D DEF, --def DEF                 Definition file (this makes -d option
                                    mandatory)
  -r RUNTIME, --runtime RUNTIME     ARES Runtime Folder
  -d DIR, --dir DIR                 Import subdirectory to inject the input files
  -t TYPE, --type TYPE              Files data type
where:

  INPUT      Directory where the input data file to import are located
  IFILE      Single input file to be imported
  DEF        Definition file for user-defined data types
  RUNTIME    Directory where the ARES runtime environment is installed
             If non present, then ~/ARES_RUNTIME is assumed, unless
             the env. var. ARES_RUNTIME is set.
  DIR        Subdirectory of ARES_RUNTIME/import where the input files
             have to be placed for import
  TYPE       Assumed data type for all the files

Note that when specifying a definition file, the "paramdef|parameter" part of
the import folder must be omitted. In addition, if you use the -f option to
specify more that one file (by using wildcards), you must include the argument
between quotes, like './*.dat')

Alternatively, you can activate the execution permissions of this script, and
call it directly.

Usage example:

  $ python src/ImportFiles.py --input $(pwd)/in --runtime $(pwd)/runtime

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

from simpleeditor.simpleeditor import launch_modal_editor

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
    with open(file, 'r') as f:
        return f.read()

def run(command):
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
        helpmenu.add_command(label='About...', command=self.menuCallback)

        #=== Main GUI structure - notebook

        self.notebook = ttk.Notebook(parent, name='notebook')

        # Tab 0 - Retrieve from ARES
        tab0 = ttk.Frame(self.notebook)
        self.notebook.add(tab0, text='Retrieve from ARES')
        self.notebook.pack(fill='both', expand=Y, side='top', padx=2, pady=2)

        #=== 1 - Retrieval from ARES

        #----- First section - Show config file name
        frm11 = ttk.Frame(tab0)
        ttk.Label(frm11, text='Applicable retrieval config. file:')\
           .pack(side=LEFT, padx=2, pady=2)
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

        #=== 2 - Import into ARES

        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Import into ARES")
        self.notebook.pack(fill='both', expand=Y, side='top')

        self.notesBox = Text(tab1, wrap=WORD, width=40, height=10)
        vscroll = ttk.Scrollbar(tab1, orient=VERTICAL, command=self.notesBox.yview)
        self.notesBox['yscroll'] = vscroll.set
        vscroll.pack(side=RIGHT, fill=Y)

        self.notesBox.pack(fill=BOTH, expand=Y, padx=2, pady=2)


        #=== 3 - Configuration

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

    def editImprtCfg(self):
        '''
        Edit import into ARES parameter configuration file
        '''
        launch_modal_editor(parent=self.parent, file=self.importConfigFile.get())

    def setRetrCfgFileName(self):
        '''
        Select retrieval config. file name
        '''
        filepath = filedialog.askopenfilename()
        if filepath != None  and filepath != '':
            self.retrieveConfigFile.set(filepath)
            self.txtRetrCfg.delete('1.0', END)
            self.txtRetrCfg.insert(END, getContentOfFile(file=filepath))

    def setImprtCfgFileName(self):
        '''
        Select import config. file name
        '''
        filepath = filedialog.askopenfilename()
        if filepath != None  and filepath != '':
            self.importConfigFile.set(filepath)
            self.txtImprtCfg.delete('1.0', END)
            self.txtImprtCfg.insert(END, getContentOfFile(file=filepath))

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

class EntrySpinbox(ttk.Frame):
    def __init__(self, master, label='Enter data:', first=1, last=100):
        self.data = StringVar()

        ttk.Frame.__init__(self, master)
        ttk.Label(self, text=label).pack(side=LEFT, padx=2, pady=2)
        self.spbx = Spinbox(self, textvariable=self.data, from_=first, to=last, width=10)
        self.spbx.pack(side=LEFT, expand=1, fill=X, padx=2, pady=2)

    def get(self):
        return self.data.get()

    def set(self, value):
        self.data.set(value)


class YMDSpinboxes(ttk.Frame):
    '''
    Handy class to add three spinboxes to set the date as year-month-day
    '''
    def __init__(self, master):
        self.year = StringVar()
        self.month = StringVar()
        self.day = StringVar()

        ttk.Frame.__init__(self, master)
        self.spbxYear = Spinbox(self, from_=2010, to=2100, textvariable=self.year, width=6)
        self.spbxYear.grid(row=0, column=0)
        self.dash1 = ttk.Label(self, text=' - ').grid(row=0, column=1)
        self.spbxMonth = Spinbox(self, from_=1, to=12, textvariable=self.month, width=4)
        self.spbxMonth.grid(row=0, column=2)
        self.dash2 = ttk.Label(self, text=' - ').grid(row=0, column=3)
        self.spbxDay = Spinbox(self, from_=1, to=31, textvariable=self.day, width=4)
        self.spbxDay.grid(row=0, column=4)

        self.clear()

    def enable(self):
        self.spbxYear.config(state=NORMAL)
        self.spbxMonth.config(state=NORMAL)
        self.spbxDay.config(state=NORMAL)

    def disable(self):
        self.spbxYear.config(state=DISABLED)
        self.spbxMonth.config(state=DISABLED)
        self.spbxDay.config(state=DISABLED)

    def set(self, year, month, day):
        self.year.set(year)
        self.month.set(month)
        self.day.set(day)

    def get(self):
        return [ int(self.year.get()), int(self.month.get()), int(self.day.get()) ]

    def clear(self):
        self.set(2018, 5, 11)


class YDoYSpinboxes(ttk.Frame):
    '''
    Handy class to add three spinboxes to set the date as year-month-day
    '''
    def __init__(self, master):
        self.year = StringVar()
        self.doy = StringVar()

        ttk.Frame.__init__(self, master)
        self.spbxYear = Spinbox(self, from_=2010, to=2100, textvariable=self.year, width=6)
        self.spbxYear.grid(row=0, column=0)
        self.dash1 = ttk.Label(self, text=' - ').grid(row=0, column=1)
        self.spbxDoy = Spinbox(self, from_=1, to=366, textvariable=self.doy, width=5)
        self.spbxDoy.grid(row=0, column=2)

        self.clear()

    def enable(self):
        self.spbxYear.config(state=NORMAL)
        self.spbxDoy.config(state=NORMAL)

    def disable(self):
        self.spbxYear.config(state=DISABLED)
        self.spbxDoy.config(state=DISABLED)

    def set(self, year, doy):
        self.year.set(year)
        self.doy.set(doy)

    def get(self):
        return [ int(self.year.get()), int(self.doy.get()) ]

    def clear(self):
        self.set(2018, 131)


class HMSmsSpinboxes(ttk.Frame):
    '''
    Handy class to add three spinboxes to set the date as year-month-day
    '''
    def __init__(self, master):
        self.hour = StringVar()
        self.min = StringVar()
        self.sec = StringVar()
        self.msec = StringVar()

        ttk.Frame.__init__(self, master)
        self.spbxHour = Spinbox(self, from_=0, to=23, textvariable=self.hour, width=4)
        self.spbxHour.grid(row=0, column=0)
        self.dash1 = ttk.Label(self, text=' : ').grid(row=0, column=1)
        self.spbxMin = Spinbox(self, from_=0, to=59, textvariable=self.min, width=4)
        self.spbxMin.grid(row=0, column=2)
        self.dash2 = ttk.Label(self, text=' : ').grid(row=0, column=3)
        self.spbxSec = Spinbox(self, from_=0, to=60, textvariable=self.sec, width=4)
        self.spbxSec.grid(row=0, column=4)
        self.dash3 = ttk.Label(self, text='.').grid(row=0, column=5)
        self.spbxMsec = Spinbox(self, from_=0, to=999, textvariable=self.msec, width=5)
        self.spbxMsec.grid(row=0, column=6)

        self.clear()

    def set(self, hour, min, sec, msec):
        self.hour.set(hour)
        self.min.set(min)
        self.sec.set(sec)
        self.msec.set(msec)

    def get(self):
        return [ int(self.hour.get()), int(self.min.get()),
                 int(self.sec.get()), int(self.msec.get()) ]

    def clear(self):
        self.set(0, 0, 0, 0)


class DateTime(ttk.Frame):
    '''
    Handy class to add a simple status bar
    '''
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.dateMode = StringVar(self)
        self.frmDate = ttk.Frame(self)
        rbtn0 = ttk.Radiobutton(self.frmDate, text='Y-M-D', command=self.useYMD,
                                variable=self.dateMode, value='ymd')
        rbtn0.grid(row=0, column=0, padx=20)
        rbtn1 = ttk.Radiobutton(self.frmDate, text='Y-DoY', command=self.useYDoY,
                                variable=self.dateMode, value='ydoy')
        rbtn1.grid(row=1, column=0, padx=20)

        self.ymd = YMDSpinboxes(self.frmDate)
        self.ymd.grid(row=0, column=1)
        self.ydoy = YDoYSpinboxes(self.frmDate)
        self.ydoy.grid(row=1, column=1)

        self.time = HMSmsSpinboxes(self)

        self.frmDate.grid(row=0, column=0)
        self.time.grid(row=0, column=2, padx=10)

        self.dateMode.set('ymd')
        self.useYMD()

    def useYMD(self):
        self.ymd.enable()
        self.ydoy.disable()

    def useYDoY(self):
        self.ymd.disable()
        self.ydoy.enable()

    def set(self, ydoy=False, year=None, month=None, day=None, doy=None, 
            hour=None, min=None, sec=None, msec=None):
        if ydoy:
            self.dateMode.set('ydoy')
            self.ydoy.set(year, doy)
        else:
            self.dateMode.set('ymd')
            self.ymd.set(year, month, day)
        self.time.set(hour, min, sec, msec)

    def get(self):
        return { 'mode': self.dateMode.get(),
                 'ymd': self.ymd.get(),
                 'ydoy': self.ydoy.get(),
                 'time': self.time.get() }

    def clear(self):
        self.ydoy.clear()
        self.ymd.clear()
        self.time.clear()


class StatusBar(ttk.Frame):
    '''
    Handy class to add a simple status bar
    '''
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.label = ttk.Label(self, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


def main():
    root = Tk()
    app = App(parent=root)
    root.mainloop()


#####################################
# MAIN - for testing
#####################################
if __name__ == '__main__':
    main()
    #print('This is a library class and cannot be executed.')
    #sys.exit()
