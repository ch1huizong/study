#include <iostream>
// T: 流程控制-while

int main(int argc, char *argv[]) {
    int i = 1, sum = 0;

    while (i <= 10) {
        sum += i;
        i++;
    }
    std::cout << "sum = " << sum << std::endl;

    return 0;
}
