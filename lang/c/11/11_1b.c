#include <stdio.h>
// T: 自动计数的枚举

enum COLOR { RED, YELLOW, GREEN, NumCOLORS };

int main(int argc, char *argv[]) {
    int color = -1;
    char *ColorNames[NumCOLORS] = {
        "red",
        "yellow",
        "green",
    };
    char *colorName = NULL;

    printf("请输入你喜欢的颜色的代码: ");
    scanf("%d", &color);
    if (color >= 0 && color < NumCOLORS) {
        colorName = ColorNames[color];
    } else {
        colorName = "unknown";
    }

    printf("你喜欢的颜色: %s\n", colorName);

    return 0;
}
