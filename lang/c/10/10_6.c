#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char s[] = "hello";
    char *p = strchr(s, 'l');
    p = strchr(p + 1, 'l');  // 寻找第二个'l'字符
    printf("%s\n", p);

    char s1[] = "hello";  // 寻找第一个'l'前面的字符串
    char *p1 = strchr(s1, 'l');
    char c = *p1;
    *p1 = '\0';
    char *t = (char *)malloc(strlen(s1) + 1);
    strcpy(t, s1);

    printf("%s\n", t);

    *p1 = c;
    free(t);

    return 0;
}
