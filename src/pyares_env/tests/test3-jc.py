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


import pyarex as pa

#from astropy.table import Table

import datetime
import os
import argparse
import time
import gzip


VERSION = '0.0.1'

__author__ = "jcgonzalez"
__version__ = VERSION
__email__ = "jcgonzalez@sciops.esa.int"
__status__ = "Prototype"  # Prototype | Development | Production


# Default configuration
DefaultConfig = 'pyarex.ini'


def get_args():
    '''
    Parse arguments from command line

    :return: args structure
    '''
    parser = argparse.ArgumentParser(description='Test script to retrieve data from ARES system',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config', dest='config_file', default=DefaultConfig,
                        help='Configuration file to use (default:{})'.format(DefaultConfig))
    parser.add_argument('-f', '--from_pid', dest='from_pid', type=int, default=1,
                        help='Initial parameter identifier')
    parser.add_argument('-t', '--to_pid', dest='to_pid', type=int, default=100,
                        help='Final parameter identifier')
    parser.add_argument('-F', '--from_date', dest='from_date', type=int, nargs=5,
                        help='Initial date in the format Y DOY h m s')
    parser.add_argument('-T', '--to_date', dest='to_date', type=int, nargs=5,
                        help='Final date in the format Y DOY h m s')

    return parser.parse_args()

def gzip_file(src_path, dst_path):
    '''
    Gzip file to file.gz

    :param src_path: Existing file
    :param dst_path: Compressed file
    '''
    with open(src_path, 'rb') as src, gzip.open(dst_path, 'wb') as dst:
        for chunk in iter(lambda: src.read(10240), b""):
            dst.write(chunk)

    os.remove(src_path)

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


def main():
    # Get start time
    start_time = time.time()

    # Parse command line arguments
    args = get_args()
    #print(args)

    # Define config. file if not set in the local environment
    if not 'PYAREX_INI_FILE' in os.environ:
        os.environ['PYAREX_INI_FILE'] = args.config_file

    # Initalize the needed datasources. Right now this is hardcoded into the initializer, so for config you need to manage this yourself.
    data_provider = pa.init_param_sampleprovider()

    # Get some params that you want to look for and of course some times as well
    from_pid, to_pid = (args.from_pid, args.to_pid)

    year1, doy1, h1, m1, s1 = args.from_date
    timestamp_start = unix_ydoy_to_ms(year1, doy1, h1, m1, s1)

    year2, doy2, h2, m2, s2 = args.to_date
    timestamp_end   = unix_ydoy_to_ms(year2, doy2, h2, m2, s2)

    base_name = ("test3_{0}-{1}__" +
                 "{2}-{3}_{4:02d}{5:02d}{6:02d}_" +
                 "{7}-{8}_{9:02d}{10:02d}{11:02d}").format(from_pid, to_pid,
                                                           year1, doy1, h1, m1, s1,
                                                           year2, doy2, h2, m2, s2)

    prep_time = time.time()

    print(("Retrieving samples for parameters with parameter ids in the range {0}:{1}\n" + 
           "from the date {2}.{3}.{4:02d}:{5:02d}:{6:02d} " + 
           "to the date {7}.{8}.{9:02d}:{10:02d}:{11:02d}\n").format(from_pid, to_pid,
                                                                     year1, doy1, h1, m1, s1,
                                                                     year2, doy2, h2, m2, s2))

    # Get parameter names for the range of parameter ids
    param_names = data_provider.get_parameter_names_from_pids(from_pid, to_pid)

    # Getting as data frame
    df = data_provider.get_parameter_data_df(param_names, timestamp_start, timestamp_end)

    exec_time = time.time()

    df.info()
    #df.describe()
    print(df.shape)

    # Save to picle
    df.to_pickle('test3-32424params-1min.pkl')

    # Save to FITS
    #t = Table.from_pandas(df)
    #t.write('test3-1000params-1h.fits', format='fits')

    # Save to HDF
    #df.to_hdf(base_name + '.h5', key='df', mode='w')

    # Save to CSV
    df.to_csv(base_name + '.csv')

    gzip_time = time.time()

    gzip_file(base_name + '.csv', base_name + '.csv.gz')

    end_time = time.time()

    print('''
         Data retrieval:   {:10.3f} s
         Data storing:     {:10.3f} s
         Compressing:      {:10.3f} s
         Total exec. time: {:10.3f} s
         '''.format(exec_time - prep_time,
                      gzip_time - exec_time,
                      end_time - gzip_time,
                      end_time - start_time))


if __name__ == '__main__':
    main()
