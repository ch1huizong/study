#include <iostream>
// T: 流程控制- do-while

int main(int argc, char *argv[]) {
    int i, sum = 0;
    std::cin >> i;

    do { // 至少执行一次语句
        sum += i;
        i++;
    } while (i <= 10);
    std::cout << "sum = " << sum << std::endl;

    return 0;
}
