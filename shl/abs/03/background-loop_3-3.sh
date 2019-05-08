#! /bin/bash
# background-loop.sh
# 出现问题的原因？

for i in 1 2 3 4 5 6 7 8 9 10
do
    echo -n "$i"
    sleep 1
done &   # 后台运行这个循环

echo  # 某些时候将不显示

for i in 11 12 13 14 15 16 17 18 19 20
do
    echo -n "$i"
    sleep 1
done

echo  # 某些时候将不显示

exit 0
