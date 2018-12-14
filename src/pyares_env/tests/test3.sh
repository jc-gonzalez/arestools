#!/usr/bin/env bash

CFG="-c ./jc.ini"

YEAR=2018
DOY=197

for h in 6 7 8 9 10 11 12 13 14 15 16 17; do

    hh=$(( h + 1 ))
    INTERVAL="-F $YEAR $DOY $h 0 0 -T $YEAR $DOY $hh 0 0"
    INTERVAL_NAME="${h}h"

    #---------------------------------------------------------------------

    if [ ! -d . ]; then
    # Retrieve params 1-10000, 1 h
    python test3-jc.py $CFG -f 1 -t 5000 ${INTERVAL} | tee t_1-5000_${INTERVAL_NAME}.out
    ls -ltr

    # Retrieve params 1-10000, 1 h
    python test3-jc.py $CFG -f 5001 -t 10000 ${INTERVAL} | tee t_5001-10000_${INTERVAL_NAME}.out
    ls -ltr

    # Retrieve params 10001-20000, 1 h
    python test3-jc.py $CFG -f 10001 -t 15000 ${INTERVAL} | tee t_10001-15000_${INTERVAL_NAME}.out
    ls -ltr

    # Retrieve params 10001-20000, 1 h
    python test3-jc.py $CFG -f 15001 -t 20000 ${INTERVAL} | tee t_15001-20000_${INTERVAL_NAME}.out
    ls -ltr

    # Retrieve params 20001-32424, 1 h
    python test3-jc.py $CFG -f 20001 -t 25000 ${INTERVAL} | tee t_20001-25000_${INTERVAL_NAME}.out
    ls -ltr
    fi
    # Retrieve params 20001-32424, 1 h
    python test3-jc.py $CFG -f 25001 -t 32424 ${INTERVAL} | tee t_25001-32424_${INTERVAL_NAME}.out
    ls -ltr

    # Retrieve all params, 1 h
    #python test3-jc.py $CFG -f 1 -t 32424 ${INTERVAL} | tee t_1-32424_${INTERVAL_NAME}.out
    #ls -ltr


done



