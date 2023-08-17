#include <cmath>
#include <iostream>
// T: 类的组合

// Point类
class Point {
  public:
    Point(int xx = 0, int yy = 0) {
        x = xx;
        y = yy;
    };

    Point(const Point &p);

    int getX() { return x; };
    int getY() { return y; };

  private:
    int x, y;
};

Point::Point(const Point &p) {
    x = p.x;
    y = p.y;
    std::cout << "Calling the copy constructor of <Point>" << std::endl;
};

// Line类
class Line {
  public:
    Line(Point xp1, Point xp2);
    Line(const Line &l);
    double getLen() { return len; }

  private:
    Point p1, p2; // 决定了参数初始化参数列表的构造顺序
    int len;
};

Line::Line(Point xp1, Point xp2) : p1(xp1), p2(xp2) {
    std::cout << "Calling constructor of <Line>" << std::endl;
    double x = static_cast<double>(p1.getX() - p2.getX());
    double y = static_cast<double>(p1.getY() - p2.getY());
    len = sqrt(x * x + y * y);
}

Line::Line(const Line &l) : p1(l.p1), p2(l.p2) {
    std::cout << "Calling the copy constructor of <Line>" << std::endl;
    len = l.len;
}

int main(int argc, char *argv[]) {
    Point p1(1, 1), p2(4, 5);
    Line l1(p1, p2);
    Line l2(l1); //复制构造

    std::cout << "The length of the l1 is " << l1.getLen() << std::endl;
    std::cout << "The length of the l2 is " << l2.getLen() << std::endl;

    return 0;
}
