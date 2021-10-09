#!/bin/bash

read -p "请输入一个文件路径: " filedir

#ls -l $filedir >/dev/null 2>&1

#if [ $? -eq 0 ]; then
if [ -e $filedir ]; then
    echo "ok"
else
    echo "No such file"
fi

