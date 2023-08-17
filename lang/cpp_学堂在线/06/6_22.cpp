#include <cassert>
#include <iostream>
// T: 深层复制

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
    ArrayofPoints(const ArrayofPoints &v);

    // 特别注意以下返回值
    Point &element(int index) {
        assert(index >= 0 && index < size);
        return points[index];
    }

  private:
    Point *points;
    int size;
};

// 深层复制代码部分
ArrayofPoints::ArrayofPoints(const ArrayofPoints &v) {
    size = v.size;
    points = new Point[size];
    for (int i = 0; i < size; ++i) {
        points[i] = v.points[i];
    }
}

int main(int argc, char *argv[]) {
    int count;
    std::cout << "Please enter the count of points: ";
    std::cin >> count;
    ArrayofPoints points1(count);
    points1.element(0).move(5, 10);
    points1.element(1).move(15, 20);

    ArrayofPoints points2(points1);
    std::cout << "Copy of points1:" << std::endl;
    std::cout << "Point_0 of points2:" << points2.element(0).getX() << ","
              << points2.element(0).getY() << std::endl;
    std::cout << "Point_1 of points2:" << points2.element(1).getX() << ","
              << points2.element(1).getY() << std::endl;

    points1.element(0).move(25, 30);
    points1.element(1).move(35, 40);
    std::cout << "After the moving of points1" << std::endl;
    std::cout << "Point_0 of points2:" << points2.element(0).getX() << ","
              << points2.element(0).getY() << std::endl;
    std::cout << "Point_1 of points2:" << points2.element(1).getX() << ","
              << points2.element(1).getY() << std::endl;

    std::cout << "Complete." << std::endl;
}
