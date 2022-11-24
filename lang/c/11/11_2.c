// T: 结构的构造和初始化
#include <stdio.h>

struct date {
    int year;
    int month;
    int day;
};  // 分号必须有

int main(int argc, char *argv[]) {
    // 初始化两种方式
    struct date today = {2022, 11, 22};
    struct date thismonth = {.month = 11, .year = 2022};

    struct date t1;
    struct date t2;
    t1 = (struct date){2022, 11, 22};  // 字面量整体赋值
    t2 = t1;
    t2.year = 2023;  // 单体赋值

    printf("Today's date is %i-%i-%i.\n", today.year, today.month, today.day);
    printf("This month's date is %i-%i-%i.\n", thismonth.year, thismonth.month,
           thismonth.day);

    printf("t1 is %i-%i-%i.\n", t1.year, t1.month, t1.day);
    printf("t2 is %i-%i-%i.\n", t2.year, t2.month, t2.day);

    struct date *pDate = &today;
    printf("Ptoday's date is %i-%i-%i.\n", (*pDate).year, (*pDate).month,
           (*pDate).day);

    return 0;
}
