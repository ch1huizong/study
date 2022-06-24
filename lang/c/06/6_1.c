#include <stdio.h>

int main(int argc, char *argv[]) {
    int a;
    a = 6;
    printf("sizeof(a) = %ld\n", sizeof(a));
    printf("sizeof(char) = %ld\n", sizeof(char));
    printf("sizeof(short) = %ld\n", sizeof(short));
    printf("sizeof(int) = %ld\n", sizeof(int));
    printf("sizeof(long) = %ld\n", sizeof(long));
    printf("sizeof(long long) = %ld\n", sizeof(long long));

    printf("sizeof(float) = %ld\n", sizeof(float));
    printf("sizeof(double) = %ld\n", sizeof(double));
    printf("sizeof(long double) = %ld\n", sizeof(long double));

    printf("sizeof(a++) = %ld\n", sizeof(a++)); // sizeof静态编译
    printf("a = %d\n", a);

    return 0;
}
