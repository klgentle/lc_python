#!/bin/bash

for i in `seq 9`
    do
    for j in `seq 9`
        do
            [ $j -ge $i ] && echo -n -e "$i*$j=$[$i*$j]\t"
        done
    echo " "
    done
