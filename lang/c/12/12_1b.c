#include <stdio.h>
// T: 返回函数本地变量的地址危险!

int *f(void);

void g(void);

int main(int argc, char *argv[]) {
    int *p = f();
    printf("*p = %d\n", *p);
    g();
    printf("*p = %d\n", *p);

    return 0;
}

int *f(void) {
    int i = 12;
    return &i;  // i消失， i占用的内存空间不受控制了
}

void g(void) {
    int k = 1024;
    printf("k = %d\n", k);
}
