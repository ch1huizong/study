#! /bin/bash
# 嵌入Ctrl-H到一个字符串
# why?
# 问题？

a="^H^H"
echo "abcdef"
echo -n "abcdef$a"
echo -n "abcdef$a"
echo; echo
