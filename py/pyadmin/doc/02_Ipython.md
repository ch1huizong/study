# 第二章 Ipython

1. ### shell执行

    * alias
 
    * rehashx

    * result = !ps aux | grep $user | grep $process

    * cd [-bq]

    * bookmak [-ldr]  name [target]

    * dhist  num或range

    * pwd

    * 可变扩展
    	```python
    for i in range(10):
        !date > ${i}.txt
    	```
    	
    * 字符串处理

        ```python
        ps = !ps aux
        ps.fields(0, 1).grep('root', prune=True).fields(1)s
        ```

2. ### 信息收集

    * page [-r]

    * pdef/pdoc/pfile/pinfo/psource/psearch或者??

    * who/who_ls/whos

3. ### 历史

    * 行模式(Ctrl-r)

    * hist命令

    * 历史结果_[num]

4. ### 快捷

    * macro name num/line-range

    * store [-drz]

    * reset

    * run [...]

    * save -r

    * rep
        -           不带参数， 变量行编辑
        - rep 2     编辑第二行
        - rep 2-3   第2-3行立即执行
