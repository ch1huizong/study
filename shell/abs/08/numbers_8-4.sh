#!/usr/bin/env bash
# numbers.sh: 几种不同数制的数字表示法.

# 10进制, 默认
let "dec=32"
echo "decimal number=$dec"

# 8进制,以'0'开头
let "oct=032"
echo "octal number=$oct"

# 16进制,以'0x'或者'0X'开头
let "hex=0x32"
echo "hex a decimal number = $hex"


# 其他进制: BASE#NUMBER
let "bin = 2#111100111001101"
echo "binary number = $bin"

let "b32=32#77"
echo "base-32 number = $b32"

let "b64=64#@_"  # 字符集ascii(2-64), 10个数字, 26个大小写字符, @, _
echo "base-64 number = $b64"

echo

echo $((36#zz)) $((2#10101010)) $((16#AF16)) $((53#1aA))

# 超出给定进制的数字范围
let "bad_oct=081"

exit 0
