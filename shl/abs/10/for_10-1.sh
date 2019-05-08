#! /bin/bash
# 列出所有的行星名称

for planet in Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto
do
    echo $planet # 每个行星被单独打印在一行上
done

echo

for planet in "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto"
do
    echo $planet # 只有一个变量
done

exit 0
