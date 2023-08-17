#include <iostream>
#include <string>
// T: string类应用，getline读取行字符串(里面可以包含空格)

int main(int argc, char *argv[]) {
    for (int i = 0; i < 2; ++i) {
        std::string city, state;

        getline(std::cin, city, ','); // 指定分割符
        getline(std::cin, state);

        std::cout << "City:" << city << " State:" << state << std::endl;
    }

    return 0;
}
