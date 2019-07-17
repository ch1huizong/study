# AWK基础

一、内部变量和内部函数

    NR	到目前为止的行数
    FNR	文件的行号
            
    FILENAME 文件名

    $0	目前的行
    NF	fields数
    FS	分割符号

    NR，NF表数量，$NR,$NF表内容


    ARGV/ARGC

    文件:	FILENAME	文件名

    记录：	/FNR/NR		记录数
        /RS/ORS		记录分割符号

    字段：	/FS/OFS		字段分割符		
        NF		字段数
        OFMT		数字输出格式

    分隔符:	
    match:	/RLENGTH/RSTART/SUBSEP



二、正则表达式

    元字符：\  ^  $  .  []  |  ()  *  +  ?

    []--> \,^开头，-  特殊含义 

    | < 并列 < *,?,+

    转义序列：\t,\r,\n


    \<,\>  单词开头和结尾 

    re命令行上级联中间没有空白。


三、其他的
	-v 外部之外的参数传递
	-F 字段分割符
