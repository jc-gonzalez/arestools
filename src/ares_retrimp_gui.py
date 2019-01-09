#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
'''

# make print & unicode backwards compatible
from __future__ import print_function
from __future__ import unicode_literals

from tkinter import *

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

from gui.app import App

# details
__author__ = "J C Gonzalez"
__copyright__ = "Copyright 2015-2019, J C Gonzalez"
__license__ = "LGPL 3.0"
__version__ = "0.1"
__maintainer__ = "J C Gonzalez"
__email__ = "jcgonzalez@sciops.esa.int"
__status__ = "Development"
#__url__ = ""


def main():
    root = Tk()
    app = App(parent=root)
    root.mainloop()


if __name__ == '__main__':
    main()
