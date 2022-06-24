#include <stdio.h>

void swap(int a, int b);

int main(void) {
    // int main(int argc, char *argv[]) {
    int a = 5, b = 6;
    swap(a, b);
    printf("a = %d, b = %d\n", a, b);

    return 0;
}

void swap(int a, int b) {
    int t = a;
    a = b;
    b = t;
}
