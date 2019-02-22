#! /bin/bash
# 嵌套的for循环

outer=1 # 外部循环的计数

for a in 1 2 3 4 5
do
    echo "Pass $outer in outer loop."
    echo "--------------------"

    inner=1 # 内部循环计数
    for b in 1 2 3 4 5
    do
        echo "Pass $inner in inner loop."
        let "inner+=1"  # increase counter
    done

    let "outer+=1"
    echo # 每次外部循环之间的间隔
done

exit 0
