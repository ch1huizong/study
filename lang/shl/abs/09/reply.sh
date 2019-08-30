#!/usr/bin/env bash
# REPLY是提供给'read'命令的默认变量

echo
echo -n "What is your favorite vegetable?"
read

echo "Your favorite vegetable is $REPLY."  # 把这个变量给了read命令


echo
echo -n "What is your favorite fruit?"
read fruit
echo "Your favorite vegetable is $fruit."
echo "But..."
echo "Value of \$REPLY is still $REPLY."  # 仍保留上一个变量的值

echo

exit 0
