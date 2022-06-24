#include <stdio.h>
// T: 统计数字0~9出现次数

const int number = 10;

int main(int argc, char *argv[]) {
    int x;
    int count[number];
    for (int i = 0; i < number; ++i) {
        count[i] = 0;
    }

    scanf("%d", &x);
    while (x != -1) {
        if (x >= 0 && x <= 9) {
            count[x]++;
        }
        scanf("%d", &x);
    }

    for (int i = 0; i < number; ++i) {
        printf("%d: %d\n", i, count[i]);
    }

    return 0;
}
