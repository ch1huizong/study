#!/usr/bin/env bash
# $IFS被设置了，但值为空, 查看"$*"和"$@"行为

mecho(){
    echo "$1, $2, $3";
}

IFS="" # 空
set a b c

mecho "$*"
mecho $*

mecho $@
mecho "$@"
# $IFS为空时， $*和$@的行为依赖于正在运行的bash或sh版本

exit 0
