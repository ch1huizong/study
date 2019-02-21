#! /bin/bash
# str_test.sh: 检查null字符串和未引用的字符串.

if [ -n $string1 ] # $string1没被声明和初始化
then
    echo "String \"string1\" is not null."  # 竟然显示为非null
else
    echo "String \"string1\" is null." 
fi

if [ -n "$string1" ] # $string1被引号括起来了
then
    echo "String \"string1\" is not null."  
else
    echo "String \"string1\" is null." 
fi

echo

if [ $string1 ] # 这次，就一个单独的$string1, 符合预期
then
    echo "String \"string1\" is not null."  
else
    echo "String \"string1\" is null." 
fi

echo

string1=
if [ $string1 ]
then
    echo "String \"string1\" is not null."  
else
    echo "String \"string1\" is null." 
fi

echo


string1="a=b"
if [ $string1 ]
then
    echo "String \"string1\" is not null."  
else
    echo "String \"string1\" is null." 
fi

exit 0
