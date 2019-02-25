#!/usr/bin/env bash
# 使用stty设置超时

INTERVAL=5

timedout_read(){  # 相当于改造了read了
    timeout=$1
    varname=$2
    old_tty_settings=`stty -g`
    stty -icanon min 0 time ${timeout}0
    eval read $varname
    stty "$old_tty_settings"
}

echo; echo -n "What's your name? Quick!"
timedout_read $INTERVAL your_name # why
echo

if [ ! -z "$your_name" ]   # 与上一个脚本有所不同，每次按键，计时器都会重置
then
    echo "Your name is $your_name."
else
    echo "Timed out."
fi

echo

exit 0
