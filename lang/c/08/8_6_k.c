#include <stdio.h>
// T: 构造n个素数

int isPrime(int x, int knownPrimes[], int length);

int main(int argc, char *argv[]) {
    const int number = 100; // 素数表容量
    int prime[number];
    int count = 1;
    int i = 3; // 起始值，可以自定义

    prime[0] = 2;
    while (count < number) {
        if (isPrime(i, prime, count)) { // 以已知的来做判断
            prime[count++] = i;         // 更新prime
        }
        i++;
    }

    for (int i = 0; i < number; ++i) {
        printf("%d", prime[i]);
        if ((i + 1) % 5) {
            printf("\t");
        } else {
            printf("\n");
        }
    }

    return 0;
}

int isPrime(int x, int knownPrimes[], int length) {
    int ret = 1;
    for (int i = 0; i < length; ++i) {
        if (x % knownPrimes[i] == 0) {
            ret = 0;
            break;
        }
    }
    return ret;
}
