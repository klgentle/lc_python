#!/bin/sh
#Filename: password.sh
echo -e "Enter password: "
# 选项-echo禁止将输出发送到终端
stty -echo
read password
stty echo
echo 
echo Password read.

