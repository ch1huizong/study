#include <stdio.h>
// T: 成绩

int main(int argc, char *argv[]) {
    int grade;

    printf("输入成绩(0-100): ");
    scanf("%d", &grade);

    char *level = NULL;

    switch (grade / 10) {
    case 10:
    case 9:
        level = "A";
        break;
    case 8:
        level = "B";
        break;
    case 7:
        level = "C";
        break;
    case 6:
        level = "D";
        break;
    default:
        level = "F";
        break;
    }

    printf("level = %s\n", level);

    return 0;
}
