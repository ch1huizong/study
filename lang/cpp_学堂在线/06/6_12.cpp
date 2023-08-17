#include <iostream>
// T: 对象指针

class Point {
  public:
    Point(int x = 0, int y = 0) : x(x), y(y){};

    virtual ~Point(){};

    int getX() const { return x; };
    int getY() const { return y; };

  private:
    int x, y;
};

int main(int argc, char *argv[]) {
    Point a(4, 5);
    Point *p = &a;

    std::cout << p->getX() << std::endl; // 注意->语法
    std::cout << a.getX() << std::endl;

    return 0;
}
