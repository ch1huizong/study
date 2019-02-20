#! /bin/bash
# 简单赋值
echo

a=879
echo "The value of \"a\" is $a."

# 使用let赋值
let a=16+5
echo "The value of \"a\" is now $a."
echo

# for循环赋值
echo -n "Values of \"a\" in the loop are: "
for a in 7 8 9 11
do
    echo -n "$a"
done

echo
echo

# 使用read命令进行赋值
echo -n "Enter \"a\":"
read a
echo "The value of \"a\" is now $a."
echo
exit 0
