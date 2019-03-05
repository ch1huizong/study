#! /bin/bash

echo

echo "Testing \"0\""

if [ 0 ]
then
    echo "0 is true."
else
    echo "0 is false."
fi

echo

echo "Testing \"1"\"
if [ 1 ]
then
    echo "1 is true"
else
    echo "1 is false."
fi

echo

echo "Testing \"-1\""
if [ -1 ]
then
    echo "-1 is true"
else
    echo "-1 is false"
fi

echo

echo "Testing \"NULL\""
if [  ]  # 为假
then
    echo "NULL is true."
else
    echo "NULL is false."
fi

echo

echo "Testing \"xyz\""
if [ xyz ]
then
    echo "Random string is true."
else
    echo "Random string is false."
fi

echo

echo "Testing \"\$xyz\""
if [ $xyz ] # 未初始化的变量为false
then
    echo "Uninitiaized variable is true."
else
    echo "Uninitiaized variable is false."
fi

echo

echo "Testing \"-n \$xyz\""
if [ -n "$xyz" ] # 更加正式的检查, 未初始化的变量为false
then
    echo "Uninitiaized variable is true."
else
    echo "Uninitiaized variable is false."
fi

echo

xyz=  # 初始化但是赋值为null
echo "Testing \"-n \$xyz\""
if [ -n "$xyz" ] # null变量为假
then
    echo "Null variable is true."
else
    echo "Null variable is false."
fi

echo

# 何时"false"为真？
echo "Testing \"false\""
if [ "false" ]   # "false"竟然为真
then
    echo "\"false\" is true."
else
    echo "\"false\" is false."
fi

echo

echo "Testing \"\$false\"" 

if [ "$false" ]  # 未初始化的变量, 为假
then
    echo "\"\$false\" is true."
else
    echo "\"\$false\" is false."
fi

echo

exit 0
