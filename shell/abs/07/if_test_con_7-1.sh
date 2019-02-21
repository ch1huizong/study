#! /bin/bash

file=/etc/passwd


if [[ -e $file ]]
then
    echo "Password file exits."
fi

dir=/home/che
if cd "$dir" 2>/dev/null
then
    echo "Now in $dir."
else
    echo "Cant't change to $dir."
fi

var1=20
var2=22

[ "$var1" -ne "$var2" ] && echo "$var1 is not equal to $var2" # 不一定非用if

home=/home/che
[ -d "$home" ] || echo "$home directory does not exists."
