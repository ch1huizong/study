#!/usr/bin/env bash

PS3='Choose your favorite vegetable: ' # 设置提示符

echo

choice_of(){
    select vagetable  # 忽略[in list], select选择传递给函数的参数
    do
        echo
        echo "Your favoriate vegetable is $vagetable."
        echo "Yuck!"
        echo
        break
    done

}

choice_of "beans" "carrots" "potatoes" "oninos" "rutabagas"

exit 0
