#! /bin/bash

DEFAULT=default

func2(){
    if [ -z "$1" ] 
    then
        echo "-Parameter #1 is zero length.-"
    else
        echo "-Parameter #1 is \"$1\".-"
    fi

    variable=${1-$DEFAULT}  # 没有$1变量的默认值
    echo "variable=$variable"

    if [ "$2" ]
    then
        echo "-Parameter #2 is \"$2\".-"
    fi

    return 0
}

echo 

echo "Nothing passed."
func2 # 不带参数调用
echo

echo "Zero-length parameter passed."
func2 ""
echo

echo "Null parameter passed."
func2 "$uninitialized_param" # 未初始化参数进行调用
echo

echo "One parameter passed."
func2 first  # 一个参数调用
echo

echo "Two parameters passed."
func2 first second
echo

echo "\"\"\"second\" passed."
func2 "" second  # 第一个参数长度为0, 第二个参数是字符串
echo

exit 0
