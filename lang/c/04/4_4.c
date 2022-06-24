#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// T: 猜数字

int main(int argc, char *argv[]) {
    srand(time(0));
    int number = rand() % 100 + 1;

    int a = 0;
    int count = 0;
    printf("我已经想好了一个1-100之间的数。\n");
    do {
        printf("猜猜这个1-100之间的数: ");
        scanf("%d", &a);
        count++;
        if (a > number) {
            printf("你猜的数大了\n");
        } else if (a < number) {
            printf("你猜的数小了\n");
        }

    } while (a != number);

    return 0;
}
