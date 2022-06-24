#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int a;
    int *p;

    p = (int *)malloc(sizeof(int));
    *p = 10;
    free(p);

    p = (int *)malloc(20 * sizeof(int));

    for (int i = 0; i < 20; ++i) {
        p[i] = i;
    }

    for (int i = 0; i < 20; ++i) {
        printf("p[i] = %d\n", p[i]);
    }

    free(p);

    return 0;
}
