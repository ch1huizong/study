#!/usr/bin/env bash
# 使用-t选项的read实现定时输入

TIMELIMIT=4

read -t $TIMELIMIT variable<&1

echo

if [ -z "$variable" ]
then
    echo "Timed out, variable still unset."
else
    echo "variable = $variable"
fi

exit 0
