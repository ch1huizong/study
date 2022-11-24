#include <stdio.h>

int g_var1 = 1024;
int g_var2;

void f(int x);

int main(int argc, char *argv[]) {
    int i = 17;
    static int var3 = 10;
    static int var4;

    f(i);

    return 0;
}

void f(int x) { printf("x = %d\n", x); }
