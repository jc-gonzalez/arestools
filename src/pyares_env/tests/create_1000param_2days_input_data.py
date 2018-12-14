#!/usr/bin/python
# -*- coding: utf-8 -*-
'''test3-jc.py.py

Test script to retrieve data from ARES system

Usage: test3-jc.py [-h] [-c CONFIG_FILE] [-f FROM_PID] [-t TO_PID]
                   [-F FROM_PID FROM_PID FROM_PID FROM_PID FROM_PID]
                   [-T TO_PID TO_PID TO_PID TO_PID TO_PID]

PyArEx package test script

optional arguments:
  -h, --help                               Show this help  message and exit
  -c CONFIG_FILE, --config CONFIG_FILE     Configuration file to use
                                           (default:pyarex.ini)
  -f FROM_PID, --from_pid FROM_PID         Initial parameter identifier
  -t TO_PID, --to_pid TO_PID               Final parameter identifier
  -F Y DOY h m s, --from_date Y DOY h m s  Initial date in the format Y DOY h m s
  -T Y DOY h m s, --to_date Y DOY h m s    Final date in the format Y DOY h m s

Usage example:

  $ python test3-jc.py -c ./cfg.ini -f 1 -t 2 -F 2013 354 0 0 0 -T 2013 354 1 0 0
'''


from utime.utime import *

import math, random

import os, errno
import argparse
import time


VERSION = '0.0.1'

__author__ = "jcgonzalez"
__version__ = VERSION
__email__ = "jcgonzalez@sciops.esa.int"
__status__ = "Prototype"  # Prototype | Development | Production


def get_args():
    '''
    Parse arguments from command line

    :return: args structure
    '''
    parser = argparse.ArgumentParser(description='Test script to retrieve data from ARES system',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-F', '--from_date', dest='from_date', type=int, nargs=5,
                        help='Initial date in the format Y DOY h m s')
    parser.add_argument('-T', '--to_date', dest='to_date', type=int, nargs=5,
                        help='Final date in the format Y DOY h m s')

    return parser.parse_args()


def define_inputs(args):
    '''
    Define inputs to retrieval process from the arguments
    '''
    # Get some params that you want to look for and of course some times as well
    year1, doy1, h1, m1, s1 = args.from_date
    timestamp_start = unix_ydoy_to_ms(year1, doy1, h1, m1, s1)

    year2, doy2, h2, m2, s2 = args.to_date
    timestamp_end   = unix_ydoy_to_ms(year2, doy2, h2, m2, s2)

    base_name = ("ares_" +
                 "{}-{}_{:02d}{:02d}{:02d}_" +
                 "{}-{}_{:02d}{:02d}{:02d}").format(year1, doy1, h1, m1, s1,
                                                    year2, doy2, h2, m2, s2)

    return (timestamp_start, timestamp_end, base_name)


def main():
    # Get start time
    start_time = time.time()

    # Parse command line arguments
    args = get_args()

    # Define process inputs
    timestamp_start, timestamp_end, base_name = define_inputs(args)

    # Initialize some variables
    parameters = {}
    tpl = 'EUCTEST{:04d}'
    
    # Create 500 parameters with period = 1s (1Hz)
    (t, dt, n, m) = (timestamp_start, 1.0, 1, 500)
    nt = int((timestamp_end - timestamp_start) / dt)
    parameters['1s'] = {
        'names': [tpl.format(k) for k in range(n, n + m - 1)],
        'times': [t + (k * dt) for k in range(0, nt)],
        'data':  [[j * math.cos((k - 10 * j)/(100 + j))/(k+10) for k in range(nt)] 
                  for j in random.sample(range(1, m + 1),m)]
    }

    # Create 200 parameters with period = 10s (0.1Hz)
    (t, dt, n, m) = (timestamp_start, 10.0, 501, 200)
    nt = int((timestamp_end - timestamp_start) / dt)
    parameters['10s'] = {
        'names': [tpl.format(k) for k in range(n, n + m - 1)],
        'times': [t + (k * dt) for k in range(0, nt)],
        'data':  [[j * math.cos((k - 10 * j)/(100 + j))/(k+10) for k in range(nt)] 
                  for j in random.sample(range(1, m + 1),m)]
    }

    # Create 200 parameters with period = 1min
    (t, dt, n, m) = (timestamp_start, 60.0, 701, 200)
    nt = int((timestamp_end - timestamp_start) / dt)
    parameters['1min'] = {
        'names': [tpl.format(k) for k in range(n, n + m - 1)],
        'times': [t + (k * dt) for k in range(0, nt)],
        'data':  [[j * math.cos((k - 10 * j)/(100 + j))/(k+10) for k in range(nt)] 
                  for j in random.sample(range(1, m + 1),m)]
    }

    # Create 50 parameters with period = 10min
    (t, dt, n, m) = (timestamp_start + 300., 600.0, 901, 50)
    nt = int((timestamp_end - timestamp_start) / dt)
    parameters['10min'] = {
        'names': [tpl.format(k) for k in range(n, n + m - 1)],
        'times': [t + (k * dt) for k in range(0, nt)],
        'data':  [[j * math.cos((k - 10 * j)/(100 + j))/(k+10) for k in range(nt)] 
                  for j in random.sample(range(1, m + 1),m)]
    }

    # Create 40 parameters with period = 1h
    (t, dt, n, m) = (timestamp_start + 1800., 3600.0, 951, 40)
    nt = int((timestamp_end - timestamp_start) / dt)
    parameters['1h'] = {
        'names': [tpl.format(k) for k in range(n, n + m - 1)],
        'times': [t + (k * dt) for k in range(0, nt)],
        'data':  [[j * math.cos((k - 10 * j)/(100 + j))/(k+10) for k in range(nt)] 
                  for j in random.sample(range(1, m + 1),m)]
    }

    # Create 10 parameters with period = 1d
    (t, dt, n, m) = (timestamp_start + 30000.0, 86400.0, 991, 10)
    nt = int((timestamp_end - timestamp_start) / dt)
    parameters['1d'] = {
        'names': [tpl.format(k) for k in range(n, n + m - 1)],
        'times': [t + (k * dt) for k in range(0, nt)],
        'data':  [[j * math.cos((k - 10 * j)/(100 + j))/(k+10) for k in range(nt)] 
                  for j in random.sample(range(1, m + 1),m)]
    }

    # Save data to file
    with open(base_name + '.csv', 'w') as csv: 
        for key,val in parameters.items():
            print('Writing {} parameters . . .'.format(key))
            names = val['names']
            times = val['times']
            for k in range(len(names)):
                name = names[k]
                datatuples = zip(times, val['data'][k])
                csv.write('\n'.join(['{},{},{}'.format(name, x[0], x[1]) for x in datatuples])) 

    end_time = time.time()    
        
    full_time_total = end_time - start_time

    print(("Total exec. time: {:10.3f} s").format(full_time_total))


if __name__ == '__main__':
    main()
