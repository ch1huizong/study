#! /bin/bash
# 变量赋值，储存命令结果

a=23
echo $a
b=$a
echo $b

# 命令替换, f1
a=`echo Hello!`
echo $a

a=`ls -l`
echo $a  # 没有引号会删除多余的空白
echo 
echo "$a" # 保留空白
echo

# 命令替换， f2
arch=$(uname -m)
echo "$arch"

exit 0
