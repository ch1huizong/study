#! /bin/bash
# 使用'more'来查看gzip文件

NOARGS=65
NOTFOUND=66
NOTGZIP=67

if [ $# -eq 0 ]
then
    echo "Usage: `basename $0` filename" >&2
    exit $NOARGS # 没有提供参数
fi

filename=$1

if [ ! -f "$filename" ] # 但是没提供文件
then
    echo "File $filename not found!" >&2
    exit $NOTFOUND
fi

if [ ${filename##*.} != "gz" ]   # 但是文件没以gz结尾
then
    echo "File $1 is not a gzipped file!"
    exit $NOTGZIP
fi

zcat $1 | more

exit $?
