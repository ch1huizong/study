#include <stdio.h>
// T: 结构的输入

struct date {
    int month;
    int day;
    int year;
};

int isLeap(struct date d);
int numberOfDays(struct date d);

int main(int argc, char *argv[]) {
    struct date today, tomorrow;

    printf("Enter today's date (mm dd yyyy): ");
    scanf("%i %i %i", &today.month, &today.day, &today.year);

    if (today.day != numberOfDays(today)) { // 是否是一个月最后一天
        tomorrow.day = today.day + 1;
        tomorrow.month = today.month;
        tomorrow.year = today.year;
    } else if (today.month == 12) {
        tomorrow.day = 1;
        tomorrow.month = 1;
        tomorrow.year = today.year + 1;
    } else {
        tomorrow.day = 1;
        tomorrow.month = today.month + 1;
        tomorrow.year = today.year;
    }

    printf("Tomorrow's date is %i-%i-%i.\n", tomorrow.year, tomorrow.month, tomorrow.day);

    return 0;
}

int isLeap(struct date d) {
    int leap = 0;
    if ((d.year % 4 == 0 && d.year % 100 != 0) || d.year % 400 == 0) {
        leap = 1;
    }

    return leap;
}

int numberOfDays(struct date d) {
    int days;
    const int daysPerMonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (d.month == 2 && isLeap(d)) {
        days = 29;
    } else {
        days = daysPerMonth[d.month - 1];
    }

    return days;
}
