#! /bin/bash
# 在一个二进制文件中定位匹配字符串
# 与"grep -a"效果类似

E_BADARGS=65
E_NOFILE=66

if [ $# -ne 2 ]
then
    echo "Usage: `basename $0` search_string filename"
    exit $E_BADARGS
fi

if [ ! -f "$2" ]
then
    echo "File \"$2\" does not exist."
    exit $E_NOFILE
fi

IFS=$'\012'  # 类似IFS="\n"
for word in $( strings "$2" | grep "$1" )
do
    echo $word   
done

# strings "$2" | grep "$1" | tr -s "$IFS" '[\n*]'  # 可以一行代替

exit 0
