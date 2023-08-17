#include <iostream>
// T: 指针和函数
// 读入三个浮点数，将整数部分和小数部分分别输出

void splitFloat(float x, int *intPart, float *fracPart) {
    *intPart = static_cast<int>(x);
    *fracPart = x - *intPart;
}

int main(int argc, char *argv[]) {
    for (int i = 0; i < 3; ++i) {
        float x, f;
        int n;
        std::cin >> x;

        splitFloat(x, &n, &f);
        std::cout << "Interger Part = " << n << ", Fraction Part = " << f
                  << std::endl;
    }

    return 0;
}
