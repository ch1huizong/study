#!/usr/bin/env bash

ROOT_UID=0

if [ "$UID" -eq "$ROOT_UID" ]
then
    echo "You are root."
else
    echo "You are an ordinary user."
fi

# 另一种方法
ROOTUSER_NAME=root

username=`id -nu` # username=`whoami`
if [ "$username" = "$ROOTUSER_NAME" ]
then
    echo "Rooty, toot, toot. you are root."
else
    echo "You are just a regular fella."
fi
