#! /bin/bash

E_PARAM=65

case "$1" in
    "")
    echo "Usage: ${0##*/} <filename>"  # 等价于${var##pattern}, 等到结果为$0
    exit $E_PARAM
    ;;

    -*)  # 文件名以-开头
    FILENAME=./$1  
    ;;

    *)
    FILENAME=$1
    ;;
esac


E_CONFFILE=66
while [ $# -gt 0 ]
do
    case "$1" in
        -d|--debug)
        DEBUG=1
        ;;

        -c|--conf)
        CONFFILE="$2"
        shift
        if [ ! -f $CONFFILE ]
        then
            echo "Error: Supplied file doesn't exist!"
            exit $E_CONFFILE
        fi
        ;; 
    esac
    shift
done

