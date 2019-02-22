#! /bin/bash
# Faxing

EXPECTED_ARGS=2
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
    echo "Usage: `basename $0` phone# text-file"
    exit $E_BADARGS
fi

if [ ! -f "$2" ]
then
    echo "File $2 is not a text file"
    exit $E_BADARGS
fi

fax make $2 # 创建传真格式的文件

for file in $(ls $2.0*)
do
    fil="$fil $file"
done
efax -d /dev/ttyS3 -o1 -t "T$1" $fil # 开始

#efax -d /dev/ttyS3 -o1 -t "T$1" $2.0* # 开始

exit 0
