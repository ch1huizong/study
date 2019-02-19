#! /bin/bash
# 描述，列表和确定是否可以安装一个rpm包
# 在一个文件中保存输出.

SUCCESS=0
E_NOARGS=65

if [ -z "$1" ]
then
    echo "Usage: `basename $0` rpm-file"
    exit $E_NOARGS
fi

{
    echo
    echo "Archieve Description:"
    rpm -qpi $1     # 查询
    echo
    echo "Archieve Listing:"
    rpm -qpl $1 # 列表
    echo 
    rpm -i --test $1 # 查询rpm包是否可以被安装
    if [ "$?" -eq $SUCCESS ]
    then
        echo "$1 can be installed."
    else
        echo "$1 cannot be installed."
    fi
    echo
} > "$1.test"

echo "Results of rpm test in file $1.test"
exit 0
