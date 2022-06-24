#include <stdio.h>
// T: x几次幂

int main(int argc, char *argv[]) {
    int x;
    int ret = 0;
    scanf("%d", &x);

    int t = x;
    while (x > 1) {
        x /= 2;
        ret++;
    }
    printf("log2 of %d is %d\n", t, ret);

    return 0;
}
