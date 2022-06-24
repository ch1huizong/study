#include <iostream>

class B; //前向引用声明

class A {
  public:
    void f(B b);
};

class B {
  public:
    void g(A a);
};

class Fred; //前向引用声明

class Barney {
    Fred x; //错误：类Fred的声明尚不完善
            // Fred* x;
};

class Fred {
    Barney y;
};
