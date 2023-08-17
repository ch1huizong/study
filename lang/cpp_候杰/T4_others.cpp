#include <iostream>
#include <set>

class Person {
   public:
    char* firstname;
    char* lastname;
};

template <typename T1, typename T2>
auto add(T1 x, T2 y) -> decltype(x + y) {  // 1. decltype动态计算类型
    return x + y;
}

// 2. decltype计算lambda表达式返回对象的类型
auto cmp = [](const Person& p1, const Person& p2) {
    return p1.lastname < p2.lastname ||
           (p1.lastname == p2.lastname && p1.firstname < p2.firstname);
};

int main(int argc, char* argv[]) {
    std::cout << "add(int, float) = " << add(5, 15.12) << std::endl;

    std::set<Person, decltype(cmp)> coll(cmp);  // 使用了lambda对象的类型

    return 0;
}
