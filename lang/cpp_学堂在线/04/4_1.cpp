#include <iostream>
// T: 类的定义 - Clock类

class Clock {
  public:
    Clock(int newH, int newM, int newS); // 构造函数

    Clock(); // 自定义默认构造函数
    // Clock(int newH=0, int newM=0, int newS=0); //
    // 提供默认参数值，自定义默认构造函数

    // Clock() = default; // 指示编译器生成默认构造函数

    void setTime(int newH = 0, int newM = 0, int newS = 0);
    void showTime();

  private:
    int hour, minute, second;
};

Clock::Clock(int newH, int newM, int newS)
    : hour(newH), minute(newM), second(newS){}; // 初始化参数列表
Clock::Clock() : hour(0), minute(0), second(0){};

// 委托构造函数, 借助已定义的构造函数，避免代码重复
// Clock::Clock() : Clock(0, 0, 0){};

void Clock::setTime(int newH, int newM, int newS) {
    hour = newH;
    minute = newM;
    second = newS;
}

void Clock::showTime() {
    std::cout << hour << ":" << minute << ":" << second << std::endl;
}

int main(int argc, char *argv[]) {
    Clock c1(9, 9, 9);
    Clock c2;

    c1.showTime();
    c2.showTime();

    return 0;
}
