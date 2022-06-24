#include <stdio.h>

int add(int a, int b) { return a + b; }

int main(int argc, char *argv[]) {
    int c;
    int (*p)(int, int);

    // p = &add;
    p = add;

    // c = (*p)(2, 3);
    c = p(2, 3);

    printf("sum = %d\n", c);

    return 0;
}
