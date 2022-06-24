#include <stdio.h>
// T: 整数分解

int main(int argc, char *argv[]) {
    int x;
    scanf("%d", &x);

    int mask = 1;
    int t = x;
    while (t > 9) {
        t /= 10;
        mask *= 10;
    }
    printf("x = %d, mask = %d\n", x, mask);

    do {
        int d = x / mask;
        printf("%d", d);
        if (mask > 9) {
            printf(" ");
        }

        x %= mask;
        mask /= 10;
        // printf("d = %d, x = %d, mask = %d\n", d, x, mask);

    } while (mask > 0);
    printf("\n");

    return 0;
}
