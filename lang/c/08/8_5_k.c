#include <stdio.h>

// T: 构造n以内(不包括n)的素数表
// 每个索引下的0和1标记是否是素数

int main(int argc, char *argv[]) {
    const int maxNumber = 125;
    int isPrime[maxNumber];
    int x;

    for (int i = 0; i < maxNumber; ++i) {
        isPrime[i] = 1;  // 假设maxNumber以内的所有的数都是素数
    }

    // 慢慢的修正素数表
    for (int i = 2; i < maxNumber; ++i) {  // 当前数值
        if (isPrime[i]) {
            for (int j = 2; j * i < maxNumber; ++j) {  // 通过倍数标记非素数
                isPrime[i * j] = 0;
            }
        }
    }

    for (int i = 2; i < maxNumber; ++i) {
        if (isPrime[i]) {  // 输出素数
            printf("%d\t", i);
        }
    }
    printf("\n");

    return 0;
}
