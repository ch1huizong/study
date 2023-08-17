#include <iostream>
// T: 自定义数据类型 - struct的使用

struct MytimeStruct {
    unsigned int year;
    unsigned int month;
    unsigned int day;
    unsigned int hour;
    unsigned int min;
    unsigned int sec;
};

int main(int argc, char *argv[]) {
    MytimeStruct mytime = {2021, 6, 3, 22, 6, 15};

    std::cout << "please input year: ";
    std::cin >> mytime.year;

    std::cout << "please input month: ";
    std::cin >> mytime.month;

    std::cout << "please input day: ";
    std::cin >> mytime.day;

    std::cout << "please input hour: ";
    std::cin >> mytime.hour;

    std::cout << "please input min: ";
    std::cin >> mytime.min;

    std::cout << "please input second: ";
    std::cin >> mytime.sec;

    std::cout << "The time is set: " << mytime.year << "/" << mytime.month
              << "/" << mytime.day << " " << mytime.hour << ":" << mytime.min
              << ":" << mytime.sec << std::endl;

    return 0;
}
