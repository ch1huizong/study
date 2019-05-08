#! /bin/bash
# echo出一些诡异变量

var="'(]\\{}\$\""
echo $var
echo "$var"

echo 

IFS='\'
echo $var   # \字符被空白替换了, 因为发生了参数分割
echo "$var"

exit 0
