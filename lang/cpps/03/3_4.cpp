#include <iostream>
// T: 函数调用-3 - 在11~999范围内寻找m, 使m、m2、m3都为回文数字

// 判断回文的函数
bool symm(unsigned n) { // 结果值
    unsigned i = n;     // 当下值
    unsigned m = 0;     // 前一次累计值

    while (i > 0) {
        m = m * 10 + i % 10; // 这里有点技巧!
        i /= 10;
    }

    return m == n;
}

int main(int argc, char *argv[]) {
    for (unsigned int i = 11; i < 1000; ++i) {
        if (symm(i) && symm(i * i) && symm(i * i * i)) {
            std::cout << "i = " << i << ", ";
            std::cout << " i * i = " << i * i << ", ";
            std::cout << " i * i * i = " << i * i * i << std::endl;
        }
    }

    return 0;
}
