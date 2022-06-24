#include <stdio.h>
// T: 判断输入的数字的位数

int main(int argc, char *argv[]) {
    int x;
    scanf("%d", &x);

    int n = 0;

    do {
        x /= 10;
        n++;
    } while (x > 0);

    printf("位数:%d\n", n);

    return 0;
}
