#! /bin/bash
# 测试字符串范围

echo
echo "Hit a key, then hit return"

read keypress

case "$keypress" in 
    [[:lower:]] ) 
    echo "Lowercase letter"
    ;;
    [[:upper:]] ) 
    echo "Uppercase letter"
    ;;
    [0-9] ) 
        echo "Digit"
    ;;
    * ) 
    echo "Punntuation, whitespace, or other"
    ;;
esac
