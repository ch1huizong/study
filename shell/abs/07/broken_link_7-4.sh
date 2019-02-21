#! /bin/bash
# broken_link.sh
# 
# 用来找出特定目录下断掉的符号链接文件并且输出他们所
# 指向的文件，便于它们可以输出提供给xargs来进行处理,比如：
# broken_link /somedir /someotherdir | xargs rm

# 非脚本，但是可能更好
#find "somedir" -type l -print0 | \
#xargs -r0 file | \
#grep "broken symbolic" |
#sed -e 's/^\|:*broken symbolic.*$/"/g'
#
# 谨防在/proc文件系统和任何死循环链接中使用

[ $# -eq 0 ] && directorys=`pwd` || directorys=$@

# 若传递的元素包含子目录，子目录递归
linkchk() {
    for element in $1/*
    do
        [ -h "$element" -a ! -e "$element" ] && echo \"$element\"
        [ -d "$element" ] && linkchk $element #  目录，递归
    done
}

for directory in $directorys
do
    if [ -d "$directory" ]
    then
        linkchk $directory
    else
        echo "$directory is not a directory"
        echo "Usage: $0 dir1 dir2 ..."
    fi
done

exit 0
