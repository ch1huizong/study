#!/usr/bin/env bash

true
echo "exit status of \"true\" = $?"

! true  # !和true间有空格, 反转命令的结果
echo "exit status of \"! true\" = $?" 

true
!true # 因为bash脚本中禁用了历史机制
