#include <stdio.h>

int total;

int square(int x) { return x * x; }

int squareOfSum(int x, int y) {
    int z = square(x + y);

    return z;
}

int main(int argc, char *argv[]) {
    int a = 1, b = 3;

    total = squareOfSum(a, b);

    printf("output = %d\n", total);

    return 0;
}
