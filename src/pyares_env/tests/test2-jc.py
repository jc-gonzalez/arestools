import pyarex as pa

import datetime
import os

def unix_ymd_to_ms(y,m,d,h=0,mi=0,s=0,ms=0):
    epoch = datetime.datetime.utcfromtimestamp(0)
    dt = datetime.datetime(y,m,d,h,mi,s)
    return int((dt - epoch).total_seconds() * 1000.0 + ms)

def unix_ydoy_to_ms(y,doy,h=0,mi=0,s=0,ms=0):
    epoch = datetime.datetime.utcfromtimestamp(0)
    dt = datetime.datetime(y, 1, 1, h, mi, s) + datetime.timedelta(doy - 1)
    return int((dt - epoch).total_seconds() * 1000.0 + ms)

if not 'PYAREX_INI_FILE' in os.environ:
    os.environ['PYAREX_INI_FILE'] = os.getcwd() + '/jc.ini'

# Initalize the needed datasources. Right now this is hardcoded into the initializer, so for config you need to manage this yourself.
data_provider = pa.init_param_sampleprovider()

# Get some params that you want to look for and of course some times as well
from_pid = 1
to_pid = 32424
timestamp_start = unix_ydoy_to_ms(2013, 354)
timestamp_end   = unix_ydoy_to_ms(2013, 355)

# Get the data from HBase and transform into Pandas DF
#df = data_provider.get_parameter_data_df(params, timestamp_start, timestamp_end)
#print(df.shape)

# Or, if you prefer, get them into sample objects and get information from the objects.
# The method returns a nested generator.
(param_names, samples) = data_provider.get_parameter_pids_data_objs(from_pid, to_pid,
                                                                    timestamp_start, timestamp_end)

print(param_names)

i = 0
for sample in samples:
    print ("{0} {1} : ".format(i+1, param_names[i]), end='')
    for s in sample:
        print("{0} ".format(s.get_value()), end='')
    print("")
    i = i + 1

print("", flush=True)
