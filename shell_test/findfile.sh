#!/bin/bash

read -p "请输入文件名: " filename

find $filename &>/dev/null

if [ $? -eq 0 ]; then
    echo "$filename exists."
else
    echo "$filename doesn't exists."
fi
