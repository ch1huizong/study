#include <iostream>
// T: 流程控制-switch

int main(int argc, char *argv[]) {
    int day;
    std::cin >> day;

    switch (day) {
    case 0:
        std::cout << "Sunday" << std::endl;
        break;
    case 1:
        std::cout << "Monday" << std::endl;
        break;
    case 2:
        std::cout << "Tuesday" << std::endl;
        break;
    case 3:
        std::cout << "Wednesday" << std::endl;
        break;
    case 4:
        std::cout << "Thursday" << std::endl;
        break;
    case 5:
        std::cout << "Friday" << std::endl;
        break;
    case 6:
        std::cout << "Saturday" << std::endl;
        break;
    default:
        std::cout << "Day out of range Sunday .. Saturday" << std::endl;
        break;
    }

    return 0;
}
