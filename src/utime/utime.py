# -*- coding: utf-8 -*-
'''utime.py

Simple functions to convert calendar dates to Unix time
'''

import datetime
#import tzlocal  # $ pip install tzlocal


VERSION = '0.0.1'

__author__ = "jcgonzalez"
__version__ = VERSION
__email__ = "jcgonzalez@sciops.esa.int"
__status__ = "Prototype"  # Prototype | Development | Production


def unix_ymd_to_ms(y,m,d,h=0,mi=0,s=0,ms=0):
    '''
    Convert calendar date in (year, month, day, hour, min, sec, millisec) to
    Unix time in milliseconds from Unix Epoch-0

    :param y: Year
    :param m: Month
    :param d: Day
    :param h: Hours
    :param mi: Minutes
    :param s: Seconds
    :param ms: Milliseconds
    :return: Date in milliseconds from Unix Epoch 0
    '''
    epoch = datetime.datetime.utcfromtimestamp(0)
    dt = datetime.datetime(y,m,d,h,mi,s)
    return int((dt - epoch).total_seconds() * 1000.0 + ms)


def unix_ydoy_to_ms(y,doy,h=0,mi=0,s=0,ms=0):
    '''
    Convert calendar date in (year, day-of-year, hour, min, sec, millisec) to
    Unix time in milliseconds from Unix Epoch-0

    :param y: Year
    :param doy: Day of year
    :param h: Hours
    :param mi: Minutes
    :param s: Seconds
    :param ms: Milliseconds
    :return: Date in milliseconds from Unix Epoch 0
    '''
    epoch = datetime.datetime.utcfromtimestamp(0)
    dt = datetime.datetime(y, 1, 1, h, mi, s) + datetime.timedelta(doy - 1)
    return int((dt - epoch).total_seconds() * 1000.0 + ms)


def unix_ms_to_datestr(ms):
    '''
    Convert ms from Unix Epoch 0 to local time string
    '''
    if isinstance(ms, str):
        ms = float(ms) if len(ms) > 0 else 0.   
    utc_time = datetime.datetime.utcfromtimestamp(ms)
    return utc_time.strftime("%Y-%m-%d %H:%M:%S.%f")
    #print(local_time.strftime("%B %d %Y"))  # print date in your format