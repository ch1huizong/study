#include <iostream>
// T: 动态分配内存空间

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

int main(int argc, char *argv[]) {
    std::cout << "Step one:" << std::endl;
    Point *ptr1 = new Point;
    delete ptr1; // 释放指向的地址的内存空间

    std::cout << std::endl;

    std::cout << "Step two:" << std::endl;
    ptr1 = new Point(1, 2);
    delete ptr1; // 再次释放

    return 0;
}
