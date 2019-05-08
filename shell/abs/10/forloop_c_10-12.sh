#! /bin/bash
# 一种类似C语言for循环的写法

echo

# 标准语法
for a in 1 2 3 4 5 6 7 8 9 10
do
    echo -n "$a"
done 

echo; echo

# C风格
LIMIT=10

for ((a=1; a<=LIMIT; a++)) # 双圆括号并且LIMIT前没有$
do
    echo -n "$a"
done

echo; echo

# 使用C语言的"逗号操作符"来增加两个变量的值
for ((a=1, b=1; a<=LIMIT; a++, b++))
do
    echo -n "$a - $b"
done

echo

exit 0
