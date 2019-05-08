#!/usr/bin/env bash

# 这里的\转义了一个换行符（变成续行符），
# 效果就是variable=echo "$variable"
# \不能单独赋值
variable=\
echo "$variable" 

variable=\
23skidoo
echo "$variable" 

variable=\  # 转义一个空格
echo "$variable" 

variable=\\
echo "$variable" 

# 第一个\转义第二个，但第3个\又变成裸体了
variable=\\\
echo "$variable" 

# 又恢复正常了
variable=\\\\
echo "$variable" 
