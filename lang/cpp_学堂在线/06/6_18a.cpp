#include <cassert>
#include <iostream>
// T: 创建动态数组的封装

class Point {
  public:
    Point() : x(0), y(0) {
        std::cout << "Default Constructor called." << std::endl;
    };
    Point(int x, int y) : x(x), y(y) {
        std::cout << "Constructor called." << std::endl;
    }

    ~Point() { std::cout << "Destructor called." << std::endl; };

    int getX() const { return x; };
    int getY() const { return y; };

    void move(int newX, int newY) {
        x = newX;
        y = newY;
    }

  private:
    int x, y;
};

class ArrayofPoints {
  public:
    ArrayofPoints(int size) : size(size) { points = new Point[size]; }
    ~ArrayofPoints() {
        std::cout << "Deleting..." << std::endl;
        delete[] points;
    };

    //***** 特别注意以下返回值,  返回数组元素的引用 *****
    Point &element(int index) { // 注意&符号
        assert(index >= 0 && index < size);
        return points[index];
    }

  private:
    Point *points;
    int size;
};

int main(int argc, char *argv[]) {
    int count;
    std::cout << "Please enter the count of points: ";
    std::cin >> count;
    ArrayofPoints points(count); // 看如何实例化
    points.element(0).move(5, 0);
    points.element(1).move(15, 20);

    std::cout << "Complete." << std::endl;
}
