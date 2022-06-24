#include <stdio.h>
// T: 1 - 1/2 + 1/3 - 1/4 ...

int main(int argc, char *argv[]) {
    int n = 0;
    double ret = 0.0;
    int sign = 1;

    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
        ret += sign * 1.0 / i;
        sign = -sign;
    }

    printf("ret = %f\n", ret);

    return 0;
}
