#include <stdio.h>
// T: 求m~n间所有素数的和

int isPrime(int num) {
    int ret = 1;
    for (int i = 2; i < num; ++i) {
        if (num % i == 0) {
            ret = 0;
            break;
        }
    }
    return ret;
}

int main(int argc, char *argv[]) {
    int m, n;
    int sum = 0;
    int cnt = 0;
    scanf("%d %d", &m, &n);

    if (m == 1) {
        m = 2;
    }

    for (int i = m; i <= n; ++i) {
        if (isPrime(i)) {
            sum += i;
            cnt++;
        }
    }
    printf("Sum: %d, Count: %d\n", sum, cnt);

    return 0;
}
