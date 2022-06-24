#include <stdio.h>

int main(int argc, char *argv[]) {
    int ch;

    while ((ch = getchar()) != EOF) {
        putchar(ch);
    }
    printf("EOF\n");

    return 0;
}
