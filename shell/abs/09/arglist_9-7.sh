#!/usr/bin/env bash
# 内部Bash变量"$*"和"$@"的古怪行为，
# 都依赖于它们是否被双引号引用起来.
# 单词拆分和换行的不一致处理

set -- "First one" "second" "third:one" "" "Fifth: :one" # 设置位置参数$1, $2

echo

echo 'IFS unchanged, using "$*"'
c=0
for i in "$*"
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS unchanged, using $*'
c=0
for i in $*  # 未引用
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS unchanged, using "$@"'
c=0
for i in "$@"
do
    echo "$((c+=1)): [$i]"
done
echo ---

echo 'IFS unchanged, using $@'
c=0
for i in $@ # 未引用
do
    echo "$((c+=1)): [$i]"
done
echo ---
