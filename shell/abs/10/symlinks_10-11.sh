#! /bin/bash
# 列出目录中所有的符号链接文件并保存到一个文件中

OUTFILE=symlinks.list
directory=${1-`pwd`}

echo "symbolic links in directory \"$directory\"" > "$OUTFILE"
echo "--------------------------------------" >> "$OUTFILE"

for file in "$( find $directory -type l )"
do
    echo "$file"
done | sort >> "$OUTFILE"

exit 0
