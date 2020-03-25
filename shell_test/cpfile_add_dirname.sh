#!/bin/bash
# 拷贝文件，在文件名中加上路径名	

for i in $(find . -name cif093*dat) 
do 
	# 获取文件名
	filename=$(basename $i)
	#echo $filename
	# 获取路径名
	dirname=$(dirname $i)
	# 去掉路径名中的./
	dirname2=$(echo ${dirname} | sed 's/\.\///')
	#echo $dirname2
        # 拷贝文件，在文件名中加上路径名	
	cp $i "$dirname2""$filename"
done
