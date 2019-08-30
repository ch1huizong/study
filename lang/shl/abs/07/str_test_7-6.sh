#!/usr/bin/env bash
#
# 检查字符串是否为null, 在引用和为未引用场合

#### 单独的参数项目
echo "加选项的参数"

if [ -n $string1 ] # $string1没被声明和初始化
then
    echo "String \"string1\" is not null."  # 竟然显示为非null!
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

#### 单独的参数项目
echo "单独参数"

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
