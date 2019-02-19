#! /bin/bash
# 在一个tarball中备份最后24小时
# 当前目录下的所有修改的文件.

BACKUPFILE=backup-$(date +%m-%d-%Y)

archive=${1:-$BACKUPFILE}

# 文件太多或者文件名包含空格可能失败
#tar cvf - `find . -mtime -1 -type f -print` > $archive.tar 

find . -mtime -1 -type f -print0 | xargs -0 tar rvf "$archive.tar"
#find . -mtime -1 -type f -exec tar rvf "$archive.tar" '{}' \;  # 便于移植，比较慢

gzip $archive.tar
echo "Directory $PWD backed up in archive file \"$archive.tar.gz \"."
