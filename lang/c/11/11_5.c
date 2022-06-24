#include <stdio.h>
// T: union的应用

typedef union {
    int i;
    char ch[sizeof(int)];
} CHI;

int main(int argc, char *argv[]) {
    CHI chi;
    chi.i = 1234; // 这里小端存储

    for (int i = 0; i < sizeof(int); ++i) {
        printf("%02hhX", chi.ch[i]);
    }
    printf("\n");

    return 0;
}
