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


from astropy.table import Table
from astropy.io import fits

from utime.utime import *

import pyarex as pa
import pandas as pd
import numpy as np
#import fitsio
#import matplotlib.pyplot as plt

import os, errno
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

# Correspondence ARES Types => FITS BinaryTable Types
Ares2FitsConversion = {
    '1':   'X',   # BIT
    '2':   'B',   # UTINYINT
    '3':   'B',   # STINYINT
    '4':   'I',   # USMALLINT
    '5':   'I',   # SSMALLINT
    '6':   'J',   # UMEDIUMINT
    '7':   'J',   # SMEDIUMINT
    '8':   'K',   # SINT
    '9':   'K',   # UINT
    '10':  'E',   # FLOAT
    '11':  'D',   # DOUBLE
    '12':  'A{}', # STRING
    '13':  '!',   # DATETIME
    '14':  '!',   # JOB
    '15':  '!'    # LOG
}
StringType = 12
DateTimeType = 13
        

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
    parser.add_argument('-n', '--num_pids_per_file', dest='num_pids_per_file', type=int, default=1000000,
                        help='Maximum number of PIDs per file')

    return parser.parse_args()


def silent_remove(filename):
    '''
    Silently remove file if it does exist
    '''
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

            
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


def define_inputs(args):
    '''
    Define inputs to retrieval process from the arguments
    '''
    # Get some params that you want to look for and of course some times as well
    from_pid, to_pid = (args.from_pid, args.to_pid)
    pids_step = args.num_pids_per_file

    year1, doy1, h1, m1, s1 = args.from_date
    timestamp_start = unix_ydoy_to_ms(year1, doy1, h1, m1, s1)

    year2, doy2, h2, m2, s2 = args.to_date
    timestamp_end   = unix_ydoy_to_ms(year2, doy2, h2, m2, s2)

    base_name = ("ares_{0}-{1}__" +
                 "{2}-{3}_{4:02d}{5:02d}{6:02d}_" +
                 "{7}-{8}_{9:02d}{10:02d}{11:02d}").format(from_pid, to_pid,
                                                           year1, doy1, h1, m1, s1,
                                                           year2, doy2, h2, m2, s2)

    print(("-----------------------------------------------------------------------------------\n" +
           "Retrieving samples for parameters with parameter ids in the range {0}:{1}\n" + 
           "from the date {2}.{3}.{4:02d}:{5:02d}:{6:02d}\n" + 
           "to the date {7}.{8}.{9:02d}:{10:02d}:{11:02d}\n" +
           "and storing the data in FITS files, in blocks of {12} param.ids").format(from_pid, to_pid,
                                                                                     year1, doy1, h1, m1, s1,
                                                                                     year2, doy2, h2, m2, s2,
                                                                                     pids_step))

    return (from_pid, to_pid, timestamp_start, timestamp_end, base_name, pids_step)


def fits_build_hdr(i, j):
    '''
    Build FITS header for resulting file
    '''
    # Build initial primary HDU for FITS file
    hdr = fits.Header()
    hdr['OBSERVER'] = 'J C Gonzalez'
    hdr['COMMENT'] = 'Multitable FITS file, with data retrieved fro ARES system'
    hdr['COMMENT'] = 'File contains data for PIDs in range {}:{}'.format(i, j)
    primary_hdu = fits.PrimaryHDU(header=hdr)
    return fits.HDUList([primary_hdu]) # HDU List with only primary_hdu


def save_to_fits(hdu_list, file_name):
    '''
    Save HDU List to FITS file
    '''
    silent_remove(file_name)
    hdu_list.writeto(file_name)


def main():
    # Get start time
    start_time = time.time()

    # Parse command line arguments
    args = get_args()

    # Define config. file if not set in the local environment
    if not 'PYAREX_INI_FILE' in os.environ:
        os.environ['PYAREX_INI_FILE'] = args.config_file

    # Initalize the needed datasources. Right now this is hardcoded into the initializer, so for config you need to manage this yourself.
    data_provider = pa.init_param_sampleprovider()

    # Define process inputs
    from_pid, to_pid, timestamp_start, timestamp_end, base_name, pids_step = define_inputs(args)

    retr_time_total, conv_time_total = (0, 0)

    keep_retrieving = True
    i_pid = from_pid
    j_pid = i_pid + pids_step - 1
    param_names_invalid = {}    

    while keep_retrieving:
     
        # Set preparation time stamp
        prep_time = time.time()
    
        # Get parameter names for the range of parameter ids, and retrieve samples as DataFrame
        param_names = data_provider.get_parameter_names_from_pids(i_pid, j_pid)
        samples = data_provider.get_parameter_data_objs(param_names, timestamp_start, timestamp_end)
    
        # Set retrieval time stamp
        retr_time = time.time()
        
        # Build initial primary HDU for FITS file
        hdul = fits_build_hdr(i_pid, j_pid)
    
        # Convert sample columns to binary tables
        i = 0
        pid = i_pid
        
        for column in samples:

            # Loop on samples to add values to the resulting vectors
            time_stamps = []
            values = []
            start = True
            
            for s in column:
                if start:
                    var_name = s.get_name()
                    var_type = s.get_type()
                    if var_name != param_names[i]:
                        print("ERROR: Param. name does not match with expectation!")
                    print('Generating table {} of {} for PID {} - {} (type={})'
                          .format(i + 1, pids_step, pid, var_name, var_type))
                    start = False
                    
                time_stamps.append(s.get_time())
    
                value = s.get_value()
                if var_type == DateTimeType:
                    value = unix_ms_to_datestr(value)
                
                values.append(value)
    
                if var_type == DateTimeType:
                    var_type = StringType
    
            i = i + 1
            pid = pid + 1

            if start:
                param_names_invalid[str(pid - 1)] = param_names[i - 1]
                continue
    
            type_conv = Ares2FitsConversion[str(var_type)]
            if var_type == StringType:
                size_fld = len(max(values, key=len))
                type_conv = type_conv.format(size_fld if size_fld > 0 else 1)
            
            t = fits.BinTableHDU.from_columns([fits.Column(name='TIMESTAMP', 
                                                            array=np.array(time_stamps), 
                                                            format='K'), 
                                                fits.Column(name=var_name, 
                                                            array=np.array(values), 
                                                            format=type_conv)])
            hdul.append(t)
            
        # Remove FITS file if exists, and (re)create it
        file_name = base_name + '.{}-{}.fits'.format(i_pid, j_pid)
        save_to_fits(hdul, file_name)
        print('Saved file {}'.format(file_name))
    
        end_time = time.time()

        retr_time_total = retr_time_total + (retr_time - prep_time)
        conv_time_total = conv_time_total + (end_time - retr_time)

        i_pid = j_pid + 1
        j_pid = i_pid + pids_step - 1
        if j_pid > to_pid:
            j_pid = to_pid

        keep_retrieving = (i_pid < to_pid)
        
    full_time_total = end_time - start_time

    print(("Data retrieval:   {:10.3f} s\n" +
           "Data conversion:  {:10.3f} s\n" +
           "Total exec. time: {:10.3f} s").format(retr_time_total,
                                                  conv_time_total,
                                                  full_time_total))
    if len(param_names_invalid) > 0:
        print("The following parameters could not be converted:")
        print('\n'.join(['{}: "{}"'.format(i, param_names_invalid[i]) 
                         for i in param_names_invalid.keys()]))


if __name__ == '__main__':
    main()
