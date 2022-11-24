#include <stdio.h>
#include <stdlib.h>

int *init(int a[], int length);
int *print(int a[], int length);

int main(int argc, char *argv[]) {
    const int MAX_SIZE = 1000;
    int size;

    do {
        printf("输入数量(0, 1000): ");
        scanf("%d", &size);
    } while (size < 0 || size > MAX_SIZE);

    int *a = (int *)malloc(size * sizeof(int));  // 主函数里面分配的地址
    print(init(a, size), size);
    free(a);

    return 0;
}

int *init(int a[], int length) {
    for (int i = 0; i < length; ++i) {
        a[i] = i;
    }
    return a;
}

int *print(int a[], int length) {
    for (int i = 0; i < length; ++i) {
        printf("%d\t", a[i]);
    }
    printf("\n");
    return a;
}
