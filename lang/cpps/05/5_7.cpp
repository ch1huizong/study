#include <iostream>
// T: 常成员函数, const会参与函数重载判断

class R {
  public:
    R(int r1, int r2) : r1(r1), r2(r2){};
    // void print();
    void print() const; // 常函数, 一种承诺, 编译器会审查函数是否改变了对象状态

  private:
    int r1, r2;
};

// void R::print() { std::cout << r1 << ":" << r2 << std::endl; }

void R::print() const { std::cout << r1 << ":" << r2 << std::endl; }

int main(int argc, char *argv[]) {
    R a(5, 4);
    a.print();

    const R b(21, 40); // 定义b是常对象了
    b.print();         // 调用void print() const

    return 0;
}
