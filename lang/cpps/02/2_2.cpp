#include <iostream>
// T: leapYear

int main(int argc, char *argv[]) {
    int year;
    bool isLeapYear;

    std::cout << "Enter the year:";
    std::cin >> year;

    isLeapYear = ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
    if (isLeapYear) {
        std::cout << year << " is a leap year" << std::endl;
    } else {
        std::cout << year << " is not a leap year" << std::endl;
    }

    return 0;
}
