#include <stdio.h>

// T: 求a和b的最大公约数，枚举法

int main(int argc, char *argv[]) {
    int a, b;
    int min;
    int ret = 0;

    scanf("%d %d", &a, &b);
    min = (a < b) ? a : b;

    for (int i = 1; i <= min; ++i) {
        if (a % i == 0) {
            if (b % i == 0) {
                ret = i;
            }
        }
    }

    printf("%d和%d的最大共约数是%d\n", a, b, ret);

    return 0;
}
