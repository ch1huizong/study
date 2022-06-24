#include <stdio.h>

int pown(int x, int n);

int main(int argc, char *argv[]) {
    int n;
    scanf("%d", &n);

    int first = 1; // 寻找起点
    for (int i = 1; i < n; ++i) {
        first *= 10;
    }

    for (int i = first; i < first * 10; ++i) { // n位数范围
        int t = i;
        int sum = 0;
        while (t > 0) { // 分解整数
            int d = t % 10;
            sum += pown(d, n);
            t /= 10;
            // printf("digit = %d, sum = %d, t = %d\n", d, sum, t);
        }

        // printf("i=%d, sum=%d\n", i, sum);
        if (i == sum) {
            printf("%d\n", i);
        }
    }

    return 0;
}

int pown(int x, int n) { // x ** n
    int p = 1;
    for (int i = 0; i < n; ++i) {
        p *= x;
    }
    return p;
}
