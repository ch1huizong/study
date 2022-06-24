#include <iostream>
// T: 复制构造函数发生的三种情况

class Point {
  public:
    Point(int xx = 0, int yy = 0);
    Point(const Point &p); // = delete; // 不被复制
    ~Point(){};
    int getX();
    int getY();

  private:
    int x, y;
};

Point::Point(int xx, int yy) : x(xx), y(yy){};
Point::Point(const Point &p) { // 复制构造函数
    x = p.x;
    y = p.y;
    std::cout << "Calling the copy constructor." << std::endl;
}

int Point::getX() { return x; };
int Point::getY() { return y; };

// 实参传入时，会发生复制构造
void fun1(Point p) { std::cout << p.getX() << std::endl; }

Point fun2() {
    Point a;
    return a;
}

int main(int argc, char *argv[]) {
    Point a;
    Point b(a); // 1. 初始化,复制发生
    std::cout << b.getX() << std::endl;

    fun1(b);    // 2. 作为函数参数
    b = fun2(); // 3. 作为函数返回值, 有问题？
    std::cout << b.getX() << std::endl;

    return 0;
}
