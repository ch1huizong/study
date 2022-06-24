#include <stdio.h>
// T: 计算月份,字符串数组应用

int main(int argc, char *argv[]) {
    int month;
    char *a[] = {
        "",        "January",  "February", "March",  "April",
        "May",     "June",     "July",     "August", "September",
        "October", "November", "December",
    };

    printf("请输入月份(1-12): ");
    scanf("%d", &month);
    printf("月: %s\n", a[month]);

    return 0;
}
