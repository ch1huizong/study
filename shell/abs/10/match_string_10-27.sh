#! /bin/bash
# 简单的字符串匹配

match_string(){
    MATCH=0
    NOMATCH=90
    PARAMS=2
    BAD_PARAMS=91

    [ $# -eq $PARAMS ] || return $BAD_PARAMS
    
    case "$1" in
        "$2") return $MATCH;;
        *) return $NOMATCH;;
    esac
}

a=one
b=two
c=three
d=two

match_string $a
echo $?

match_string $a $b
echo $?

match_string $b $d
echo $?

exit 0
