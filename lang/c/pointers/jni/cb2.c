#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int A = *((int *)a);
    int B = *((int *)b);

    return abs(A) - abs(B);
}

int main(int argc, char *argv[]) {
    int i, A[] = {-31, 22, -1, 50, -6, 4};
    qsort(A, 6, sizeof(int), compare);

    for (int i = 0; i < 6; ++i) {
        printf("%d ", A[i]);
    }

    printf("\n");

    return 0;
}
