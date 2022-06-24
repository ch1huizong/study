#include <stdio.h>
// T: 求和

void sum(int, int); // 函数原型声明

int main(int argc, char *argv[]) {
    sum(1, 10);
    sum(20, 30);
    sum(35, 45);

    return 0;
}

void sum(int begin, int end) {
    int sum = 0;
    for (int i = begin; i <= end; ++i) {
        sum += i;
    }
    printf("%d到%d的和是%d\n", begin, end, sum);
}
