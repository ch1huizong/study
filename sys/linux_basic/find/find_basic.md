# find基础

一、find命令

1. 形式: find [PATH1][path2]... [option] [action]

2. 基本: find . [-print]  print打印出匹配的文件名(-print0使用'\0'作为分隔符)

--- 

二. 相关选项和动作

1. 时间

    时间：-atime，-mtime，-ctime 元数据（权限和所有权）最后一次改变的时间 （类似有-amin/-mmin/-cmin)
	
	举例： 
        4 代表4-5前的那一天；
        +4 代表大于等于5天前文件名；（大于）
        -4 代表小于等于4天内的文件名；（小于）

	时间是一个区间。
	
	-newer file 比file新的文件

2. 与使用者或群组有关：
	
    -uid n, -gid n 数字
	-user name, -group name 名字
	-nouser, -nogroup  不在/etc/passwd或/etc/group 内的文件	

3. 与文件属性和名称有关:

	-name filename
	-iname 忽略大小写
	-path  匹配的是文件路径，是路径一部分，路径是一整体
	
	-regextype 指定正则的类型
	-regex 同上，也是路径，正则
	-iregex 

	-size [+-] Size, Size的单位有c，k ,不加符号表示>=Size
	-type  f,(b,c),d,l,s,p
	
	-perm mode 正好等于mode的文件
	    :-mode  搜寻到的文件属性包好mode,就是比mode大
	    :+mode  比mode小，搜寻到的文件被包含

4. 深度：
	-maxdepth N 1代表当前目录
	-mindepth N

5. 动作:
	+ -exec command  {} \; 
	+ -print
	+ -delete
	+ -prune 代表排除某一特定目录
	
	-exec和\;代表指令开始到结束

	在命令行上代表整体，用括号，形式\( ...\) ?
	find name后可以接通配符，不是正则表达式

5. 逻辑： -a，-o，！

--- 

三. xargs命令(-0选项与find 的-print0连用）

xargs [-0epn] cmd args... : 产生命令所需要的参数，这些命令一般并不支持管道（默认以空格或换行分割参数）
    + -0  还原特殊字符为一般字符，以字符0作为输出分割符
	+ -e[str] EOF ,遇到它结束
	+ -p  询问
	+ -n 每次命令执行，需要几个参数,一次处理几个
	+ -d 分割符号 
    + -I {} 制定替换字符串，用于固定参数的命令，以‘\n'作为参数的定界符号
