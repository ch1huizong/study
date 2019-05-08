#!/usr/bin/env bash

var0=0
LIMIT=10

while [ "$var0" -lt "$LIMIT" ]
do
    echo -n "$var0"
    var0=`expr $var0 + 1` 
    # 或var0=$(($var0+1))
    # 或var0=$((var0+1))
    # 或let "var0 +=1"
done
