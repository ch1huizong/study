#!/usr/bin/env bash
# 在一个指定目录的所有文件中查找一个特定的字符串

#directory=/usr/bin
#fstring="Free Software Foundation"
directory=$1
fstring=$2

for file in $(find $directory -type f -name '*' | sort)
do
    strings -f $file | grep "$fstring" | sed -e "s%$directory%%" 
    #替换文件名前
done

exit 0
