#! /bin/bash
# 列出目录中所有的符号链接文件

directory=${1-`pwd`}  # 否则默认当前工作目录

#ARGS=1
#if [ $# -ne "$ARGS" ]
#then
#    directory=`pwd`
#else
#    directory=$1
#fi

echo "symbolic links in  directory \"$directory\"" 
#若没括起来，会把一个带有空白部分的文件名拆分成以空白分割的两部分
for file in "$(find $directory -type l )" # 不把它当一个参数吗?
do
    echo "$file"
done | sort  # 可以通过管道

echo 

echo "symbolic links in  directory \"$directory\""
OLDIFS=$IFS
IFS=:

for file in $(find $directory -type l -printf "%p$IFS")
do
    echo "$file"
done | sort
