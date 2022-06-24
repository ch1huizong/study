#include <stdio.h>
// T: 判断x是否是素数

int main(int argc, char *argv[]) {
    int x;
    scanf("%d", &x);
    int isPrime = 1; // 假设x是素数

    for (int i = 2; i < x; ++i) {
        if (x % i == 0) {
            isPrime = 0;
            break;
        }
    }
    if (isPrime) {
        printf("%d是素数\n", x);
    } else {
        printf("%d不是素数\n", x);
    }

    return 0;
}
