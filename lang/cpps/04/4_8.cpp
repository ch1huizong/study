#include <iostream>
#include <string>
// T: 联合体使用 - 共用存储空间

class ExamInfo {
  private:
    std::string name; // 课程名字

    enum { GRADE, PASS, PERCENTAGE } mode;

    union {          // 无名联合体
        char grade;  // 等级制
        bool pass;   // 通过与否
        int percent; // 百分制
    };               // 共享内存

  public:
    ExamInfo(std::string name, char grade)
        : name(name), grade(grade), mode(GRADE) {} 
    ExamInfo(std::string name, bool pass)
        : name(name), pass(pass), mode(PASS) {}
    ExamInfo(std::string name, int percent)
        : name(name), percent(percent), mode(PERCENTAGE) {}

    void show();
};

void ExamInfo::show() {
    std::cout << name << " : ";

    switch (mode) {
    case GRADE:
        std::cout << grade << std::endl;
        break;
    case PASS:
        std::cout << (pass ? "PASS" : "FAIL") << std::endl;
        break;
    case PERCENTAGE:
        std::cout << percent << std::endl;
        break;
    default:
        std::cout << "Exit" << std::endl;
    }
}

int main(int argc, char *argv[]) {
    ExamInfo c1("English", 'B');
    ExamInfo c2("Calculus", true);
    ExamInfo c3("C++ Programming", 85);

    c1.show();
    c2.show();
    c3.show();

    return 0;
}
