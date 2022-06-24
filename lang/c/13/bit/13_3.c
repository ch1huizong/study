#include <stdio.h>
// T: 输出数字的二进制形式

int main(int argc, char *argv[]) {
    int number;
    scanf("%d", &number);
    printf("8:number = %o\n", number);
    printf("16:number = %x\n", number);

    printf("2:");
    unsigned mask = 1u << 31;
    for (; mask; mask >>= 1) {
        printf("%d", number & mask ? 1 : 0);
    }
    printf("\n");
    return 0;
}
