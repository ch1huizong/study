#! /bin/bash
# 命令替换产生for循环的list

NUMBERS="9 7 3 8 37.53"

for number in `echo $NUMBERS`
do
    echo -n "$number"
done

echo 

exit 0
