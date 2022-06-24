#include <stdio.h>
// T: 浮点运算不精确

int main(int argc, char *argv[]) {
    float a, b, c;
    a = 1.345f;
    b = 1.123f;
    c = a + b;

    if (c == 2.468) {
        printf("相等\n");
    } else {
        printf("不相等! c = %.10f, 或%f\n", c, c);
    }

    return 0;
}
