#!/usr/bin/env bash
# while的多条件循环, 写法有点特殊

var1=unset
previous=$var1

while echo "previous-variable=$previous"
    echo
    previous=$var1
    [ "$var1" != end ] # 只有最后的一个条件控制退出状态
do
    echo "Input variable #1 (end to exit)"
    read var1
    echo "variable #1 = $var1"
done

exit 0
