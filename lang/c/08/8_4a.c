#include <math.h>
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

// 过滤出偶数，再判断奇数
int isPrime(int x) {
    int ret = 1;
    if (x == 1 || (x % 2 == 0 && x != 2)) {
        ret = 0;
    }

    for (int i = 3; i < sqrt(x); i += 2) {  // 再从奇数中判断, 不正确？
        if (x % i == 0) {
            ret = 0;
            break;
        }
    }
    return ret;
}
