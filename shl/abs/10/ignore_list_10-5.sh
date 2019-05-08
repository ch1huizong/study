#! /bin/bash
# 脚本省略in [list]部分
# 分别通过带参数和不带参数调用脚本

for a  # 省略了list部分，循环会操作"$@"
do
    echo -n "$a"
done

echo

exit 0
