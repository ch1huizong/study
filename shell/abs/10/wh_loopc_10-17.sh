#! /bin/bash
# C语言风格的while

# 标准
LIMIT=10
a=1

while [ "$a" -le $LIMIT ]
do
    echo -n "$a"
    let "a+=1"
done
echo; echo

# C风格
((a = 1)) # a=1

while (( a <= LIMIT )) # 变量两边没有"$"
do
    echo -n "$a"
    ((a += 1))
done
echo

exit 0
