#!/bin/bash

s=`wc -l /etc/inittab | awk '{print $1'}`
#echo $s

if [ $s -gt 100 ]; then
    echo "/etc/inittab is a big file."
else
    echo "/etc/inittab is a small file."
fi
