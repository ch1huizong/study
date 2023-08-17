#include <iostream>
#include <string>
// T: string类的应用

inline void test(const char *title, bool value) {
    std::cout << title << " returns " << (value ? "true" : "false")
              << std::endl;
}

int main(int argc, char *argv[]) {
    std::string s1 = "DEF";
    std::cout << "s1 is " << s1 << std::endl;

    std::string s2;
    std::cout << "Please enter s2: ";
    std::cin >> s2;
    std::cout << "length of s2: " << s2.length() << std::endl;

    test("s1 <= ABC", s1 <= "ABC");
    test("DEF <= s1", "DEF" <= s1);

    s2 += s1; // 连接操作
    std::cout << "s2 = s2 + s1: " << s2 << std::endl;
    std::cout << "length of s2: " << s2.length() << std::endl;

    return 0;
}
