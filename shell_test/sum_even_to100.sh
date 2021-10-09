#!/bin/bash

#求出1到100的偶数和
typeset -i sum=0;

for i in `seq 0 2 100`
    do
        #let sum+=$i
        sum=$[$sum+$i]
    done
echo $sum
