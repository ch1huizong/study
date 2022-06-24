#include <stdio.h>
// T: 整数逆序

int main(int argc, char *argv[]) {
    int x;
    scanf("%d", &x);
    int digit;
    int ret = 0;

    while (x > 0) {
        digit = x % 10;
        ret = ret * 10 + digit;
        x /= 10;
    }

    printf("ret = %d\n", ret);

    return 0;
}
