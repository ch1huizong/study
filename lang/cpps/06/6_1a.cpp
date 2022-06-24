#include <iostream>
// T: 输出fib序列前20项

int main(int argc, char *argv[]) {
    int f[20] = {1, 1};
    for (int i = 2; i < 20; ++i) {
        f[i] = f[i - 1] + f[i - 2];
    }

    for (int i = 0; i < 20; ++i) {
        if (i % 5 == 0)
            std::cout << std::endl;

        std::cout.width(12);
        std::cout << f[i];
    }
    std::cout << std::endl;

    return 0;
}
