#include <stdio.h>

// T: 求a和b的最大公约数，辗转相除法

int main(int argc, char *argv[]) {
    int a, b;
    int t;

    scanf("%d %d", &a, &b);
    int ai = a;
    int bi = b;

    while (b != 0) {
        t = a % b;
        a = b;
        b = t;
    }

    printf("%d和%d的最大公约数是%d\n", ai, bi, a);

    return 0;
}
