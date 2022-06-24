#include <iostream>
// T: 分情况计算图形的面积

const float PI = 3.1416;

int main(int argc, char *argv[]) {
    int iType;
    float radius, a, b, area;

    std::cout << "图形的类型为?(1-圆形 2-长方形 3-正方形): ";
    std::cin >> iType;

    switch (iType) {
    case 1:
        std::cout << "圆形的半径为: ";
        std::cin >> radius;
        area = PI * radius * radius;
        std::cout << "面积为: " << area << std::endl;
        break;

    case 2:
        std::cout << "矩形的长为: ";
        std::cin >> a;
        std::cout << "矩形的宽为: ";
        std::cin >> b;
        area = a * b;
        std::cout << "面积为: " << area << std::endl;
        break;

    case 3:
        std::cout << "正方形的边为: ";
        std::cin >> a;
        area = a * a;
        std::cout << "面积为: " << area << std::endl;
        break;

    default:
        std::cout << "不是合法的输入值!" << std::endl;
    }

    return 0;
}
