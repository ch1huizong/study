#include <iostream>

int main()
{
    int a;
    int *p;

    p = new int; // 简便了,返回指定类型指针
    *p = 10;
    printf("*p = %d\n", *p);
    delete p;

    p = new int[20];
    p[0] = 1024;
    printf("*p = %d\n", *p);
    delete[] p;

    return 0;
}
