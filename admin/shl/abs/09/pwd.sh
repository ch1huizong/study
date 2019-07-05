#!/usr/bin/env bash

E_WRONG_DIRECTORY=73

TargetDirectory=/home/che/che

cd $TargetDirectory
echo "Deleting stale files in $TargetDirectory."

if [ "$PWD" != "$TargetDirectory" ]  # 确认是否在正确目录
then
    echo "Wrong directory!"
    echo "In $PWD, rather than $TargetDirectory!"
    echo "Bailing out!"
    exit $E_WRONG_DIRECTORY
fi

rm -fr *
rm .[A-Za-z0-9]*  # 删除点文件
rm -f .[^.]*..?*  # 删除以多个点开头的文件

# (shopt -s dotglob; rm -f *) # 也可以
echo
echo "Done."
echo "Old files deleted in $TargetDirectory"
echo

exit 0



