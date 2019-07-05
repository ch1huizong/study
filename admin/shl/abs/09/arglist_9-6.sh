#!/usr/bin/env bash

E_BADARGS=65

if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` argument1 argument2 etc."
    exit $E_BADARGS
fi

echo

index=1

echo "Listing args with \"\$*\":"
for arg in "$*"  # 整个 
do
    echo "Arg #$index = $arg"
    let "index +=1"
done
echo "Entire arglist seen as single word."

echo

index=1

echo "Listing args with \$*(unquoted):"
for arg in $* # 将会把参数看成单独的单词
do
    echo "Arg #$index = $arg" 
    let "index += 1"
done
echo "Arglist seen as seperate words."

exit 0
