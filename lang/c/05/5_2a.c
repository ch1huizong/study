#include <stdio.h>
// T: 输出前N个素数

int main(int argc, char *argv[]) {
    const int N = 50;
    int count = 0;
    int x = 2;
    int isPrime;

    while (count < N) {
        isPrime = 1;

        for (int i = 2; i < x; ++i) { // 判断x是否是素数
            if (x % i == 0) {
                isPrime = 0;
                break;
            }
        }
        if (isPrime) {
            count++;
            printf("%d\t", x);

            if (count % 5 == 0) {
                printf("\n");
            }
        }
        x++; // 下一个数
    }

    return 0;
}
