#!/usr/bin/env bash

PS3='Choose your favorite vegetable: ' # 设置提示符

echo

select vagetable in "beans" "carrots" "potatoes" "oninos" "rutabagas"
do
    echo
    echo "Your favoriate vegetable is $vagetable."
    echo "Yuck!"
    echo
    break
done

exit 0
