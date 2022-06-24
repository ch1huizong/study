#include <stdio.h>

int main(int argc, char *argv[]) {
    int hour1, minute1;
    int hour2, minute2;

    scanf("%d %d", &hour1, &minute1);
    scanf("%d %d", &hour2, &minute2);

    int h = hour2 - hour1;
    int t = minute2 - minute1;
    if (t < 0) {
        t = 60 + t;
        h--;
    }

    printf("时间差是%d小时%d分钟\n", h, t);

    return 0;
}
