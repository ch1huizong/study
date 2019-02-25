#!/usr/bin/env bash
# 定时输入

TIMELIMIT=3

PrintAnswer(){
    if [ "$answer" = TIMEOUT ]
    then
        echo "$answer"
    else
        echo "Your favorite vegetable is $answer."
        kill $! # 不再需要后台运行的TimerOut了， $!存储上一个后台作业的PID
    fi
}

TimerOn(){
    sleep $TIMELIMIT && kill -s 14 $$ &   # $$存储脚本PID
}

Int14Vector(){  # 超时处理器
    answer="TIMEOUT"
    PrintAnswer
    exit 14
}

trap Int14Vector 14 # 设置超时处理器

echo "What is your favorite vegetable?"
TimerOn
read answer
PrintAnswer

exit 0
