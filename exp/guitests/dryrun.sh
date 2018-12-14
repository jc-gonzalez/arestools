#!/bin/bash

rndint () {
    n=$(dd if=/dev/random bs=1 count=1  2>/dev/null |od -i|awk '(NR==1){print $2;}')
    echo "$n"
}

m=$(wc -l test6.log | cut -d" " -f1)

k=1
n=1
while [ $k -lt $m ]; do 
    head -$k test6.log | tail -$n 
    sleep 1 
    n=$(( RANDOM % 100 + 20 ))
    k=$(( k + $n ))
done

n=$(( k - m ))
tail -$n test6.log
