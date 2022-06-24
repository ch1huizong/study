#include <stdio.h>
// T: 字符读入

int main(int argc, char *argv[]) {
    char c;
    int i;

    // scanf("%d %c\n", &i, &c); // 空格好像是忽略的意思
    scanf("%d%c\n", &i, &c); //紧接着
    printf("i = %d, c = %d, c=%c\n", i, c, c);

    return 0;
}
