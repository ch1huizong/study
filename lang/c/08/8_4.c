#include <stdio.h>
// T: 判断素数

int isPrime(int x);

int main(int argc, char *argv[]) {
    int x;
    scanf("%d", &x);
    if (isPrime(x)) {
        printf("%d是素数\n", x);
    } else {
        printf("%d不是素数\n", x);
    }

    return 0;
}

// 从2~x-1遍历
int isPrime(int x) {
    int ret = 1;
    if (x == 1) {
        ret = 0;
    }
    for (int i = 2; i < x; ++i) {
        if (x % i == 0) {
            ret = 0;
            break;
        }
    }
    return ret;
}
