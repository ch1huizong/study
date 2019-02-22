#! /bin/bash
# fileinfo.sh
# 循环迭代文件

FILES="/usr/sbin/accept
/usr/sbin/pwck
/usr/sbin/chroot
/usr/bin/fakefile
/usr/bin/python2.7
/sbin/badblocks
/sbin/ypbind"

echo

for file in $FILES
do
    if [ ! -e "$file" ]
    then
        echo "$file does not exists."; echo
        continue
    fi
    
    ls -l $file | awk '{print $9 "    filesize: " $5}'
    whatis `basename $file`
    echo
done

exit 0
