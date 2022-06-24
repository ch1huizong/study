#include <stdio.h>

int main(int argc, char *argv[]) {
    int B[2][3] = {{2, 3, 6}, {4, 5, 8}};

    int(*p)[3] = B;

    printf("B => %p, &B[0] = %p, *B = %p, B[0] = %p\n", B, &B[0], *B, B[0]);
    printf("B+1 = %p, &B[1] = %p, *(B+1) = %p, B[1] = %p\n", B + 1, &B[1],
           *(B + 1), B[1]);

    return 0;
}
