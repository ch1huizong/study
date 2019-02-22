#! /bin/bash
# “break N”退出N层循环

for outerloop in 1 2 3 4 5
do
    echo -n "Group $outerloop: "

    for innerloop in 1 2 3 4 5
    do
        echo -n "$innerloop"
        
        if [ "$innerloop" -eq 3 ]
        then
            break 2 # break 2
        fi
    done

    echo
done

echo 

exit 0
