#!/bin/bash
#sleep.sh
echo -n Count:
#存储光标位置
tput sc

count=0;
while true;
do 
    if [ $count -lt 40 ];
    then 
        let count++;
        sleep 1;
        #恢复光标位置
        tput rc
        #清除从当前光标位置到行尾之间的所有内容
        tput ed
        echo -n $count;
    else exit 0;
    fi
done
