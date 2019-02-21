#! /bin/bash
# 算术测试
# 本质是计算后的最终结果

(( 0 ))
echo "Exit status of \"((0))\" is $?"

(( 1 ))
echo "Exit status of \"((1))\" is $?"

(( 5>4 ))
echo "Exit status of \"((5>4))\" is $?"

(( 5>9 ))
echo "Exit status of \"((5>9))\" is $?"


(( 5-5 ))
echo "Exit status of \"((5-5))\" is $?"

(( 5/4 ))
echo "Exit status of \"((5/4))\" is $?"

(( 1/2 )) # 截取之后结果为0
echo "Exit status of \"((1/2))\" is $?"

(( 1/0 )) 2>/dev/null # 除数为0,非法计算
echo "Exit status of \"((1/0))\" is $?"


exit 0
