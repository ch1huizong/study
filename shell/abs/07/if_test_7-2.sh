#!/usr/bin/env bash

echo

if test -z "$1"
then
    echo "No command-line arguments."
else
    echo "First command-line argument is $1."
fi

echo 

if /usr/bin/test -z "$1" # 与shell内建的test命令结果相同
then
    echo "No command-line arguments."
else
    echo "First command-line argument is $1."
fi
echo 

if [ -z "$1" ]
then
    echo "No command-line arguments."
else
    echo "First command-line argument is $1."
fi
echo


if /usr/bin/[ -z "$1" ]  # 等价于/usr/bin/test
then
    echo "No command-line arguments."
else
    echo "First command-line argument is $1."
fi
echo

exit 0
