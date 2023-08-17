#include <iostream>
// T: 动态创建数组

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
    Point *ptr = new Point[2]; // Point(1, 1)不行啊!
    ptr[0].move(5, 10);
    ptr[1].move(15, 20);

    std::cout << "Deleting..." << std::endl;
    delete[] ptr; // 注意后面的[]

    return 0;
}
