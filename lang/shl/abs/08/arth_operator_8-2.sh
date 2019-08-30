#!/usr/bin/env bash
# 10种不同的方法计数到11
# let, ((...)), $((...)), $[...]

n=1 
echo -n "$n"

let "n=$n+1" # 1
echo -n "$n"

: $((n=$n+1)) # 2, :必需
echo -n "$n"

((n=n+1)) # 3
echo -n "$n"

n=$(($n+1)) # 4
echo -n "$n"

: $[n=$n+1] # 5, :必需
echo -n "$n"

n=$[$n+1] # 6
echo -n "$n"


# 接下来是C风格的增量操作
let "n++"  # 7
echo -n "$n"

(( n++ )) # 8
echo -n "$n"

: $((n++)) # 9 
echo -n "$n"

: $[n++] # 10
echo -n "$n"

echo

exit 0
