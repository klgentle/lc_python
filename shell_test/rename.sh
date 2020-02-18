#!/bin/bash
# 用途: 重命名.jpg和.png文件

count=1;
for img in `find . -maxdepth 1 -iname '*.png' -o -iname '*.jpg' -type f`
do
    new=image-$count.${img##*.}

    echo "Rename $img to $new"
    mv "$img" "$new"
    let count++

done
