#!/usr/bin/env bash
# 每个数组元素包含两个参数

for planet in "Mercury 36" "Venus 67" "Earth 93"  "Mars 142" "Jupiter 483"
do
    set -- $planet # 强制解析变量"planet"并且设置位置参数
    # "--" 可以防止$planet为空，或者是以一个破折号开头.
    #
    # original_params=("$@") # 可以保留原始的位置参数

    echo "$1        $2,000,000 miles from the sun"  # 分配后的位置参数
done

exit 0
