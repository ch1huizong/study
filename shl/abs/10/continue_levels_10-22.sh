#!/usr/bin/env bash
# 演示"continue N"命令

for outer in I II III IV V
do
    echo; echo -n "Group $outer: "

    for inner in 1 2 3 4 5 6 7 8 9 10 
    do
        if [ "$inner" -eq 7 ] 
        then
            continue 2 # continue外部循环, 开启下一轮外部循环
        fi
        echo -n "$inner" 
    done

echo '-------------' # 此处不会输出

done

echo; echo

exit 0
