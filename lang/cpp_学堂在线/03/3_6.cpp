#include <cstdlib>
#include <iostream>
// T: 函数调用-6 - 投骰子

enum GameStatus { WIN, LOSE, PLAYING };

int main(int argc, char *argv[]) {
    int sum, myPoints; // myPoints游戏玩家的点数
    GameStatus status;
    unsigned int seed;
    int rollDice(void);

    std::cout << "Please enter an unsigned integer: ";
    std::cin >> seed; // 随机种子
    srand(seed);

    sum = rollDice(); // 第一轮投递并计算和数
    switch (sum) {
    case 7:
    case 11:
        status = WIN;
        break;

    case 2:
    case 3:
    case 12:
        status = LOSE;
        break;

    default:
        status = PLAYING;
        myPoints = sum;
        std::cout << "point is " << myPoints << std::endl;
    }

    // 接下来第二轮、第三轮...
    while (status == PLAYING) { // 只要状态为PLAYING,继续
        sum = rollDice();
        if (sum == myPoints) {
            status = WIN;
        } else if (sum == 7) {
            status = LOSE;
        }
    }

    // 终于得到正负结果了
    if (status == WIN) {
        std::cout << "player wins" << std::endl;
    } else {
        std::cout << "player loses" << std::endl;
    }

    return 0;
}

int rollDice() {
    int die1 = 1 + rand() % 6;
    int die2 = 1 + rand() % 6;
    int sum = die1 + die2;
    std::cout << "player rolled " << die1 << " + " << die2 << " = " << sum
              << std::endl;

    return sum;
}
