#! /bin/bash
# bash变量是不区分类型的

a=2334
let "a += 1"
echo "a = $a"  # 整型
echo

b=${a/23/BB} # 将"23"替换为"BB"
echo "b = $b"
declare -i b
echo "b = $b"

let "b +=1" # BB35 + 1
echo "b = $b"
echo 

c=BB34
echo "c = $c"
d=${c/BB/23} # 将BB替换成23

echo "d = $d"
let "d +=1"
echo "d = $d"
echo

# 看一下null变量
e=""
echo "e = $e"
let "e += 1"
echo "e = $e"
echo

# 如果变量没有声明
echo "f = $f"
let "f +=1"
echo "f = $f"
echo

exit 0
