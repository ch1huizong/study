// 标准头文件结构, 保证头文件在一个编译单元中只能被引用一次
// 根源上是解决结构重复定义的问题
#ifndef _MAX_H 
#define _MAX_H

extern int gAll; // 全局变量声明, 声明不产生代码
double max(double a, double b);

struct Node {
    int value;
    char *name;
};

#endif 
