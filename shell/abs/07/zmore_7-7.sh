#! /bin/bash
# 使用'more'来查看gzip文件

NOARGS=65
NOTFOUND=66
NOTGZIP=67

if [ $# -eq 0 ]
then
    echo "Usage: `basename $0` filename" >&2
    exit $NOARGS
fi

filename=$1

if [ ! -f "$filename" ]
then
    echo "File $filename not found!" >&2
    exit $NOTFOUND
fi

if [ ${filename##*.} != "gz" ]   # 判断文件gz结尾
then
    echo "File $1 is not a gzipped file!"
    exit $NOTGZIP
fi

zcat $1 | more

exit $?
