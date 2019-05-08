#! /bin/bash
# escaped.sh转义符

echo; echo

echo "\v\v\v\v"

echo "========"
echo "VERTICAL TABS"
echo -e "\v\v\v\v"   # 打印特殊含义
echo "========"

echo "QUOTATION MARK"
echo -e "\042"   # 打印引号
echo "========"

# 如果使用$'\X'结构， -e选项不必要了
echo; echo "NEWLINE AND BEEP"
echo $'\n' # 新行
echo $'\a' # 警告

echo "========"
echo "QUOTATION MARK"
echo $'\t\042\t' # 8进制字码
echo $'\t\x22\t' # 16进制字码

echo "========"
echo

# 分配ASCII字符到变量中
quote=$'\042'
echo "$quote this is a quoted string, $quote and this lies outside the quotes."
echo

# 变量中的连续ASCII字符.
triple_underline=$'\137\137\137'
echo "$triple_underline UNDERLINE $triple_underline"

echo

ABC=$'\101\102\103\010'
echo $ABC
echo; echo

escape=$'\033'   # 033是八进制的esc.
echo "\"escape\" echoes as $escape"  # 没有变量输出
echo; echo

exit 0
