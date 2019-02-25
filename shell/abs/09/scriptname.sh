#!/usr/bin/env bash
# ./scriptname 1 2 3 4 5

echo "$@"

shift
echo "$@"  # 会丢弃之前的$1, 包含剩余的参数

shift
echo "$@"  
