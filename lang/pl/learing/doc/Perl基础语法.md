### Perl基础语法

#### 一.  数据

1. 标量

   * 数字

   * 字符串

     单引号'和双引号"含义不同;

     双引号中“的标量变量插值;

   * undef

     undef值表示空无一物，可变为数字0或者''字符串

     

2. 变量

   * 标量变量s
   * 数据类型的自动转换



#### 二.  控制

1.  条件

   ```perl
   if (con) {
       ....
   } else{
       ....
   }
   ```

   

2.  循环

   ```perl
   while (con) {
       ....
   }
   ```

   

3.  符号

   <STDIN> : 	读取一行值直到遇到\n为止

   chomp:   去除输入的一个换行符, `chomp($text = <STDIN>)`

   defined:  可判断$input是undef还是空字符, `defined($input)`

   

#### 三. 语言特性

* 没有布尔数据类型;
* 字符串'0'是表示假;
* 



