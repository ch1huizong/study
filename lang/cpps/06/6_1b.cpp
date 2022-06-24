#include <iostream>
// T: 一维数组应用, 答题

int main(int argc, char *argv[]) {
    const char key[] = {'a', 'c', 'b', 'a', 'd'};
    const int NUM_QUES = 5;
    char c;
    int ques = 0, numCorrect = 0;

    std::cout << "Enter the " << NUM_QUES << "question tests:" << std::endl;

    while (std::cin.get(c)) {
        if (c != '\n') { // 当前人没有答完题
            if (c == key[ques]) {
                numCorrect++;
                std::cout << " ";
            } else {
                std::cout << "*";
            }
            ques++;
        } else { // 当前人答完题了，计算结果
            std::cout << " Score "
                      << static_cast<float>(numCorrect) / NUM_QUES * 100 << "%"
                      << std::endl;
            ques = 0;
            numCorrect = 0;
        }
    }
    // 所有人的答题结束

    return 0;
}
