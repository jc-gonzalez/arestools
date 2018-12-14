import pyarex as pa

import datetime
def unix_time_ms(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000.0)

# Initalize the needed datasources. Right now this is hardcoded into the initializer, so for config you need to manage this yourself.
data_provider = pa.init_param_sampleprovider()

# Get some params that you want to look for and of course some times as well
params = ['ALPHA_AN', 'SOLAR_AA']
#timestamp_start = 1387324800000
#timestamp_end = 1388584759000
timestamp_start = unix_time_ms(datetime.datetime(2021,1,1,0,0))
timestamp_end   = unix_time_ms(datetime.datetime(2021,1,10,0,0))

# Get the data from HBase and transform into Pandas DF
df = data_provider.get_parameter_data_df(params, timestamp_start, timestamp_end)
print(df.shape)

# Or, if you prefer, get them into sample objects and get information from the objects.
# The method returns a nested generator.
samples = data_provider.get_parameter_data_objs(params, timestamp_start, timestamp_end)
for sample in samples:
    for s in sample:
        print(s.get_value())

