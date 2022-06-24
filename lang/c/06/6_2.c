#include <stdio.h>
// T: 探测int和unsinged int的最大值

int main(int argc, char *argv[]) {
    int a = 0;
    unsigned int b = 0;
    unsigned int t = b + 1;

    while (++a > 0)
        ;
    printf("int max(a) = %d\n", a - 1);

    while (t > 0) {
        b++;
        t++;
    }
    printf("int max(b) = %u\n", b);

    return 0;
}
