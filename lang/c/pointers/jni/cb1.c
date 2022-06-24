#include <stdio.h>
#include <stdlib.h>

// 自定义比较规则或排名机制
int compare(int a, int b) {
    if (a > b) { // a的得分就高了
        return 1;
    }
    return -1;
}

int abs_compare(int a, int b) { return abs(a) - abs(b); }

void BubbleSort(int A[], int n, int (*compare)(int, int)) {
    int i, j, tmp;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n - 1; ++j) {
            if (compare(A[j], A[j + 1]) > 0) {
                tmp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = tmp;
            }
        }
    }
}

int main(int argc, char *argv[]) {
    int i, A[] = {2, 4, 3, -7, 5, 6};

    // BubbleSort(A, 6, compare);
    BubbleSort(A, 6, abs_compare);

    for (int i = 0; i < 6; ++i) {
        printf("%d ", A[i]);
    }
    printf("\n");

    return 0;
}
