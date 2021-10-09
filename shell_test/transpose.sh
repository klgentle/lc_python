#!/bin/bash
# 解题思路：建立数组，数组内容为每一列拼接后的结果
# 第一行不用拼接，从第二行开始

awk '{
    for(i=1;i<=NF;i++) {
        if(NR==1) {
            arr[i] = $i
        } else {
            arr[i] = arr[i]" "$i
        }
    }
}
END {
    for(j=1;j<=NF;j++){
        print arr[j]
    }
}' transpose.txt
