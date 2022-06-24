#include <stdio.h>
// T: 阶乘

int main(int argc, char *argv[]) {
    int n;
    scanf("%d", &n);
    int fact = 1;

    for (int i = n; i > 1; i--) {
        fact *= i;
    }
    printf("%d! = %d\n", n, fact);

    return 0;
}
