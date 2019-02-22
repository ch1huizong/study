#! /bin/bash
# 在for循环中产生文件名扩展

echo

for file in *  # 当前目录下所有文件,但不能匹配"."文件的
do
    ls -l "$file"

    # 如果没有匹配到任何文件，那它将扩展成自己.
    # 为了防止这种情况发生，那就设置nullglob选项
    # (shopt -s nullglob)
done

echo; echo

for file in [jx]*
do
    rm -f $file # 只删除当前目录以"j"或"x"开头的文件
    echo "Removed file \"$file\""
done

echo

exit 0
