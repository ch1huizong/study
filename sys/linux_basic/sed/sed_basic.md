# Sed基础

一. 概括
    1. 问题: 自动化编辑

    2. 用法: sed [-nefr] [action] [file1 file2 file3 ... ]

    3. 选项

        * -n     安静模式，只有经过sed特殊处理的行才会被列出来

        * -e     命令模式下的动作

        * -f     脚本文件

        * -r     扩展正则

        * -i['后缀']     直接修改文件,如果有后缀，则会另外备份一份，*代表现在的文件名

        * -s     分割,把每一个输入文件当作单一的流，而不是整个大流的一部分

        * -l N   折行长度

        * -z		输入行以'\0'结尾

        概念:
            - patt空间: 存在待处理的一行,下一行就没了
            - hold空间: 缓存 



二. 关键点
    1. 地址

        * 内容
            - 数字
            - 正则/re/

        * 地址个数
            - 0 所有行
            - 1 指定行
            - 2 范围

        * 例子
            - 'number'  特定行
            - 'start~step'  阶

            - '$' 输入文件最后一行,若指定-i和-s则是每个输入文件最后一行

            - '/p1/,/p2/'  正则范围,也可以用%作分割符号

            - '0,/p1/'  p1匹配从第一行开始

            - 'add1,+N'

            - 'add1,~N'

        第二个地址匹配默认是从第一个地址下面的行开始


    2. 动作
        * d     删除
        * a\    数据行之后追加 
        * i\    数据行之前插入
        * c\    改变
        * p     打印
        * P     多行p中，打印第一行
        * l     与p相同，但会列出非打印字符
        * r f   读
        * w f   写
        * y     映射转换
        * !     否，不执行函数参数动作
        * q     退出程序
        * =     打印行数
        * #     注释
        * {}    命令组
        * :     标签
        * b/t   跳到

        * h     p数据暂存hold, 原hold被覆盖,流程p -> h
        * H     append
        * g     h数据放回patt, 原patt被覆盖,流程h -> p
        * G     append，
        * x     p <-> h

        * w f   写数据到文件f
        * r f   从文件f读数据

        * d     删除p内存在的所有行,并读入下一行

                删除f空白行:
                    sed -e '/^$/d' f      

        * D     删除p内的第一行,不读入下一行,里面存在的数据下一步处理

                合并f空白行:
                    sed -e '/^$/{N; /^$/D}' f 不行啊?

        * n     下一行

                偶数行:
                    sed -n -e 'n' -e 'p' input.dat
                奇数行：
                    sed -n -e 'N' -e 'P' input.dat


        * N     追加至pattern，pattern会包括两行,以\n分割
                
                合并:
                    sed -e 'N' -e 's/\n/ /' input.dat

        * s     替换

            + 形式:
                [address1[,address2]]s/patt/repl/flags

            + 注意点:
                - repl包括
                    - \1-9反向引用,被\(..\)包起来的
                    - &代表前面patt字符串
                    - \L,\l, \U,\u,\E 小写形式

                - 定界符还可以是:或|或#

            + flags:
                + g     全行
                + N     第N个匹配
                + p     打印
                + w f   写到文件
                + I/i   忽略大小写
                + M/m   多行模式

            + 例子:
                * s/pattern/new/Ng 从第N处开始替换



三. 问题：
    + 替换换行符\n问题;

    + 外部数据引擎如何驱动数据读入的？

    + 内部命令如何改变数据驱动流程的？

    + 多个命令行序列-e如何执行 ?
