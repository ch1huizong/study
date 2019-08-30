#!/usr/bin/env bash
# 内部Bash变量"$*"和"$@"的古怪行为，
# 都依赖于它们是否被双引号引用起来.
# 单词拆分和换行的不一致处理

# 共通："保持原意，不加双引号单词内字符串

set -- "First one" "second" "third:one" "" "Fifth: :one" # 设置位置参数$1, $2

echo

echo 'IFS unchanged, using "$*"'  # 就一个单词
c=0
for i in "$*"
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS unchanged, using $*'  # 空白分割整个字符串
c=0
for i in $*  # 未引用
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS unchanged, using "$@"'  # 保持每个单词
c=0
for i in "$@"
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS unchanged, using $@' # 空白分割整个字符串
c=0
for i in $@ # 未引用
do
    echo "$((c+=1)): [$i]"
done
echo ---
echo

echo ---------------------
echo

IFS=:
echo 'IFS=":", using "$*"'
c=0
for i in "$*"
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS=":", using $*'
c=0
for i in $*
do
    echo "$((c+=1)): [$i]"
done
echo ---

var=$*
echo 'IFS=":", using "$var"(var=$*)'
c=0
for i in "$var"
do
    echo "$((c+=1)): [$i]"
done
echo ---


echo 'IFS=":", using $var(var=$*)'
c=0
for i in $var
do
    echo "$((c+=1)): [$i]"
done
echo ---


var="$*"
echo 'IFS=":", using $var(var="$*")'
c=0
for i in $var # 分割了
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS=":", using $var(var="$*")'
c=0
for i in "$var" # 不分割了
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS=":", using "$@"'
c=0
for i in "$@"  # special, 自己的规则，好像没分割
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS=":", using $@'
c=0
for i in $@ # 解除了规则了，单词内分割
do
    echo "$((c+=1)): [$i]"
done
echo ---

var=$@
echo 'IFS=":", using $var(var=$@)'
c=0
for i in $var # 合一分割
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS=":", using "$var"(var=$@)'
c=0
for i in "$var"
do
    echo "$((c+=1)): [$i]"
done
echo ---

var="$@"
echo 'IFS=":", using "$var"(var="$@")'
c=0
for i in "$var"
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS=":", using "$var"(var="$@")'
c=0
for i in $var
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo

exit 0
