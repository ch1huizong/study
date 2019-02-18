#! /bin/bash

LOG_DIR=/var/log
ROOT_UID=0
LINES=50
E_XCD=66
E_NOTROOT=67

if [ "$UID" -ne "$ROOT_UID" ] # 用户身份
then
    echo "Must be root to run this script."
    exit $E_NOTROOT
fi

if [ -n "$1" ] # 保留行数
then
    lines=$1
else
    lines=$LINES
fi

#E_WRONGARGS=65
#case "$1" in
#    "" ) lines=50;;
#    *[!0-9]* ) echo "Usage: `basename $0` file-to-cleanup"; exit $E_WRONGARGS;;
#    * ) lines=$1;;
#esac

cd $LOG_DIR # 切换目录并检查
if [ `pwd` != "$LOG_DIR" ] # if [ "$PWD" != "$LOG_DIR" ]
then
    echo "Cant't change to $LOG_DIR."
    exit $E_XCD
fi


#cd /var/log || {
#    echo "Cannot change to necessary directory.">&2
#    exit $E_XCD;
#}

# 清理工作
tail -$lines messages > mesg.temp
mv mesg.temp messages

cat /dev/null > wtmp
echo "Logs cleaned up."
exit 0
