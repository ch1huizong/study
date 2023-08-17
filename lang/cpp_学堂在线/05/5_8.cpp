#include <iostream>
// T: 常数据成员 - 类数据和实例数据

class A {
  public:
    A(int i);
    void print();

  private:
    const int a;
    static const int b;
};

const int A::b = 10; // 常类成员初始化
A::A(int i) : a(i){};
void A::print() { std::cout << a << ":" << b << std::endl; }

int main(int argc, char *argv[]) {
    A a1(100), a2(0); // 常实例成员的初始化
    a1.print();
    a2.print();

    return 0;
}
