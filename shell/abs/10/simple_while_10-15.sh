#! /bin/bash

echo

while [ "$var1" != "end" ] # 结束条件
do
    echo "Input variable #1 (end to exit)"
    read var1
    echo "variable #1 = $var1"
    echo
done

exit 0
