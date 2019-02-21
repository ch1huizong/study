#! /bin/bash

# "a"和"b"既可以认为是整型又可以认为是字符串, 上下文决定
a=4  
b=5

echo

if [ "$a" -ne "$b" ] # 数字比较
then
    echo "$a is not equal to $b"
    echo "(arithmetic comparison)"
fi

echo

if [ "$a" != "$b" ] # 字符串比较
then
    echo "$a is not equal to $b"  # 52 != 53
    echo "(string comparison)"
fi

echo

exit 0
