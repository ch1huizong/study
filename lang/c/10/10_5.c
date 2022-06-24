#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// T: 复制

// 数组版本
char *mycpy1(char *dst, const char *src) {
    int idx = 0;
    while (src[idx]) {
        dst[idx] = src[idx];
        idx++;
    }
    dst[idx] = '\0';
    return dst;
}

// 指针版本
char *mycpy2(char *dst, const char *src) {
    char *ret = dst;
    while ((*dst++ = *src++)) {
    };
    *dst = '\0';
    return ret;
}

int main(int argc, char *argv[]) {
    char s1[] = "hello world";
    char s2[strlen(s1) + 1]; // 这里提前计算空间了
    // mycpy1(s2, s1);
    mycpy2(s2, s1);

    printf("%s\n", s2);

    return 0;
}
