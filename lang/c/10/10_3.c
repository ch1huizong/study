#include <stdio.h>
#include <string.h>

int mylen(const char *s) {
    int cnt = 0;
    while (*s++ != '\0') {
        cnt++;
    }
    return cnt;
}

int main(int argc, char *argv[]) {
    char s[] = "Hello";
    printf("Length: %lu\n", strlen(s));
    printf("Size: %lu\n", sizeof(s));
    printf("mylen: %d\n", mylen(s));

    return 0;
}
