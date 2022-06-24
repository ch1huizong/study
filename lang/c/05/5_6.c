#include <stdio.h>
// T: 逆序输出整数数字

int main(int argc, char *argv[]) {
    int d;
    int x;
    scanf("%d", &x);

    do {
        d = x % 10;
        printf("%d", d);
        if (x > 9) {
            printf("\t");
        }
        x /= 10;
    } while (x > 0);
    printf("\n");

    return 0;
}
