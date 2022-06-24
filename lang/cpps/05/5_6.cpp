#include <cmath>
#include <iostream>
// T: 友元函数 - dist

class Point {
  public:
    Point(int x = 0, int y = 0) : x(x), y(y){};

    int getX() { return x; };
    int getY() { return y; };

    friend float dist(Point &a,
                      Point &b); // 声明友元函数, 可以访问对象a的a.x, a.y

  private:
    int x, y;
};

// 友元函数, 不属于类
float dist(Point &a, Point &b) {
    double x = a.x - b.x;
    double y = a.y - b.y;
    return static_cast<float>(sqrt(x * x + y * y));
}

int main(int argc, char *argv[]) {
    Point p1(1, 1), p2(4, 5);
    // std::cout << p1.x << std::endl; //私有成员不能访问
    std::cout << "The distance is " << dist(p1, p2) << std::endl;

    return 0;
}
