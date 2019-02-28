#!/usr/bin/env bash

a=375 
hello=$a  # 注意：=前后无空格

echo hello
echo $hello
echo ${hello} # 引用变量的值

echo "$hello"
echo "${hello}" # 部分引用
echo

hello="A B C  D"
echo $hello # 变量替换不会保留其中空白
echo "$hello" # 部分引用保留其中空白
echo

echo '$hello' # 全引用不替换

hello=  # 设置为null值
echo "\$hello (null value) = $hello"

var1=21 var2=22 var3=$V3  # 一行引用多个变量，可读性降低
echo "var1=$var1 var2=$var2 var3=$var3" 

echo; echo

numbers="one two three"
other_numbers="1 2 3"  # 变量包含空格，需要包含引用, 不能other_numbers=1 2 3
echo "numbers=$numbers"
echo "other_numbers=$other_numbers"

mixed_bag=2\ ---\ whatever  # 转义符后边的空格
echo "$mixed_bag"
echo; echo

echo "uninitialized_variable=$uninitialized_variable"  # 未声明
uninitialized_variable=  # 声明，但是没有初始化这个变量
echo "uninitialized_variable=$uninitialized_variable"

uninitialized_variable=23
unset uninitialized_variable
echo "uninitialized_variable=$uninitialized_variable"  # 还是空值
echo

exit 0
