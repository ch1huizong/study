#include <stdio.h>
// T: 直接使用枚举量

enum COLOR { RED, YELLOW, GREEN };

int main(int argc, char *argv[]) {
    int color = -1;
    char *colorName = NULL;

    printf("请输入你喜欢的颜色的代码: ");
    scanf("%d", &color);

    switch (color) {
    case RED:
        colorName = "red";
        break;
    case YELLOW:
        colorName = "yellow";
        break;
    case GREEN:
        colorName = "green";
        break;
    default:
        colorName = "unknown";
        break;
    }
    printf("你喜欢的颜色: %s\n", colorName);

    return 0;
}
