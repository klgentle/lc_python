#!/bin/bash

declare -i ind=1
declare -i sum=0

while read line
do
    num=`echo $line | grep -o [12345] | wc -l`
    echo line$ind number:$num
    let ind+=1
    let sum+=$num

done < readline.txt 
echo sum is $sum
