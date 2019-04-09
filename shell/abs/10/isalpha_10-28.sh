#! /bin/bash
# 使用"case"结构来过滤字符串

SUCCESS=0
FAILURE=-1

isalpha(){ # 检查第一个字母是不是字母字符
    if [ -z "$1" ]
    then
        return $FAILURE
    fi

    case "$1" in
        [a-zA-Z]*) return $SUCCESS;;
        *) return $FAILURE;;
    esac
}

isalpha2(){ # 测试整个字符串是否都是字母字符
    [ $# -eq 1 ] || return $FAILURE
    
    case "$1" in
        *[!a-zA-Z]*| "")  return $FAILURE;; # 有不是字母的别的符号?
        *) return $SUCCESS;;
    esac
}

isdigit(){ # 测试整个字符串是否都是数字
    [ $# -eq 1 ] || return $FAILURE

    case "$1" in
        *[!0-9]*| "")  return $FAILURE;; # 有不是数字的字符
        *) return $SUCCESS;;
    esac
}

isfloat(){ 
    [ $# -eq 1 ] || return $FAILURE

    case "$1" in
        *[!0-9.]*)  return $FAILURE;;
        *[.]*) return $SUCCESS;;  # 必需包含.?
    esac
}


check_var(){ # 测试isalpha
    if isalpha "$@"
    then
        echo "\"$*\" begins with an alpha character."

        if isalpha2 "$@"
        then
            echo "\"$*\" contains only alpha characters."
        else
            echo "\"$*\" contains at least one non-alpha character."
        fi
    else
        echo "\"$*\" begins with a non-alpha character."
    fi
    echo
}

digit_check(){ # 测试isdigit
    if isdigit "$@"
    then
        echo "\"$*\" contains only digits [0-9]."
    else
        echo "\"$*\" has at least one one-digit character." 
    fi
    echo
}

float_check(){
    if isfloat "$@"
    then
        echo "\"$*\" is a float."
    else
        echo "\"$*\" has at least one one-digit character." 
    fi
    echo
}

a=23skidoo
b=H3llo
c=-What?
d=What?
e=`echo $b`
f=AbcDef
g=27234
h=27a34
i=27.34
m=3

check_var $a
check_var $b
check_var $c
check_var $d
check_var $e
check_var $f
check_var   # 没有参数传递

digit_check $g
digit_check $h
digit_check $i

float_check $i
float_check $m

exit 0
