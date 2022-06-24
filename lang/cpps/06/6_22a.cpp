#include <iostream>
// T: 第一种方法，复制构造

class IntNum {
  public:
    IntNum(int x = 0) : xptr(new int(x)) {
        std::cout << "Calling constructor..." << std::endl;
    }
    IntNum(const IntNum &n) : xptr(new int(*n.xptr)) {
        std::cout << "Calling copy constructor..." << std::endl;
    }
    ~IntNum() {
        delete xptr;
        std::cout << "Destructing..." << std::endl;
    }
    int getInt() { return *xptr; }

  private:
    int *xptr;
};

IntNum getNum() {
    IntNum a;
    return a; // 有变化
}

int main(int argc, char *argv[]) {
    std::cout << getNum().getInt() << std::endl;
    return 0;
}
