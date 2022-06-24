#include <stdio.h>
// T: 计数

int main(int argc, char *argv[]) {
    int count = 100;

    while (count >= 0) {
        count--;
        printf("%d\n", count);
    }
    printf("发射!\n");

    return 0;
}
