#include <iostream>
// T: 枚举类型

enum GameResult {WIN, LOSE, TIE, CANCEL}; // 符号常量， 有值

int main(int argc, char *argv[]) {
    GameResult result;
    enum GameResult omit = CANCEL;

    for (int i = WIN; i <= CANCEL; ++i) {
        //result = i; // 与C语言不同，需要强制转化
        result = GameResult(i); // int -> enum, 类型转换

        if (result == omit) {
            std::cout << "The game was cancelled" << std::endl;
        } else {
            std::cout << "The game was played";
            if (result == WIN) {
                std::cout << " and we won!";
            }
            if (result == LOSE) {
                std::cout << " and we lost.";
            }

            std::cout << std::endl;
        }
    }

    return 0;
}
