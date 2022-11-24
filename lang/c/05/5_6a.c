#include <stdio.h>
// T: 逆序输出整数数字, 700不能正确输出

int main(int argc, char *argv[]) {
    int d, x, t = 0;
    scanf("%d", &x);

    // 构建逆序整数
    do {
        d = x % 10;
        t = t * 10 + d;
        x /= 10;
    } while (x > 0);
    x = t;

    do {  // 逆序输出整数数字
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
