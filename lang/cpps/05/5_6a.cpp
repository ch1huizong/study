#include <iostream>
// T: 友元类 - B

class A {
    friend class B; // 声明友元类B

  public:
    A(int x = 0) : x(x){};
    void display() { std::cout << x << std::endl; }

  private:
    int x;
};

class B {
  public:
    B(A a) : a(a){};

    void set(int i);
    void display();

  private:
    A a;
};

void B::set(int i) { a.x = i; } // 可以访问a的private x了

void B::display() { a.display(); }

int main(int argc, char *argv[]) {
    A a;
    B b(a);
    b.set(777);
    b.display();

    return 0;
}
