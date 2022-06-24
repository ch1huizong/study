#include <stdio.h>
// T: 计算平均值并打印大于平均值的数字

const int NUM = 3;

int main(int argc, char *argv[]) {
    int x;
    double sum = 0;
    int cnt = 0;
    int number[NUM];

    scanf("%d", &x);
    while (x != -1) {
        if (cnt == NUM) {
            printf("Array full\n");
            break;
        }
        number[cnt] = x;
        sum += x;
        cnt++;

        scanf("%d", &x);
    }
    if (cnt > 0) {
        printf("Average: %f\n", sum / cnt);

        for (int i = 0; i < cnt; ++i) {
            if (number[i] > sum / cnt) {
                printf("%d\n", number[i]);
            }
        }
    }

    return 0;
}
