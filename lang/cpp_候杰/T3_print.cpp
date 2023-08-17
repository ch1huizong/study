
// 可变模板参数 - 函数模板
//
// 递归调用处理的是"参数" - 使用函数模板
// 递归继承处理的是"类型" - 使用类模板
// 函数头部/构造函数，处理参数拆分
//
// 注意区分: 模板的声明、使用和定义
//      1. 声明时, 需要指明T具体的类型 -> 产生具体的类
//      2. 使用时, C p(...) -> 类实例p
//      3. 定义时, T只不过是一个类型符号(占位)

#include <bitset>
#include <complex>
#include <initializer_list>
#include <iostream>
#include <ostream>
#include <stdexcept>
#include <tuple>

// 例子1
void print() {}

template <typename T, typename... Types>               // 1
void print(const T& firstArg, const Types&... args) {  // 2
    std::cout << firstArg << ":" << sizeof...(args) << std::endl;  // 剩余参数个数
    print(args...);          // 3
}
/*
template <typename... Types>
void print(const Types&... args){ // 比较泛化，共存永远不会调用
}

*/

// 例子2, 模拟实现print函数
void printfx(const char* s) {
    while (*s) {
        if (*s == '%' && *(++s) != '%') {
            std::runtime_error("invalid format string");
        }
        std::cout << *s++;
    }
}

// 递归分解的规则可以自己定制, 模式匹配
template <typename T, typename... Args>
void printfx(const char* s, T value, Args... args) {  // 注意拆分规则
    while (*s) {
        if (*s == '%' && *(++s) != '%') {
            std::cout << value;     // todo: %d等控制字符没有用到
            printfx(++s, args...);  // 注意这里！
            return;
        }
        std::cout << *s++;  // 原样打印其他字符
    }
}

// 例子三, 使用初始列表实现max - 参数类型相同
struct lesser {  // 把比较操作函数包装成对象了
    template <typename It1, typename It2>
    bool operator()(It1 it1, It2 it2) const {
        return *it1 < *it2;
    }
};

template <typename It, typename Compare>
inline It max_element(It first, It last, Compare comp) {
    if (first == last) {
        return first;
    }
    It result = first;

    while (++first != last) {
        if (comp(result, first)) {
            result = first;
        }
    }
    return result;
}

template <typename It>
inline It max_element(It first, It last) {
    return max_element(first, last, lesser());
}

template <typename T>
inline T max(std::initializer_list<T> l) {
    return *max_element(l.begin(), l.end());
}

// 例子四
int max1(int n) { return n; }

template <typename... Types>
int max1(int n, Types... args) {
    return std::max(n, max1(args...));
}

// 例子五，首-remaining元素的处理逻辑不同, 递归创建
template <int IDX, int MAX, typename... Args>
struct PRINT_TUPLE {
    static void print(std::ostream& os, const std::tuple<Args...>& t) {
        os << std::get<IDX>(t) << (IDX + 1 == MAX ? "" : ",");  // 拿当下元素
        PRINT_TUPLE<IDX + 1, MAX, Args...>::print(os, t);
    }
};

template <int MAX, typename... Args>
struct PRINT_TUPLE<MAX, MAX, Args...> {  // 模板特化, 注意排列顺序
    static void print(std::ostream& os, const std::tuple<Args...>& t){};
};

template <typename... Args>
std::ostream& operator<<(std::ostream& os, const std::tuple<Args...>& t) {
    os << "[";
    PRINT_TUPLE<0, sizeof...(Args), Args...>::print(os, t);
    return os << "]" << std::endl;
}

// 例子六， 递归继承
template <typename... Values> class Tup1;
template <> class Tup1<> {};

template <typename Head, typename... Tail>
class Tup1<Head, Tail...> : private Tup1<Tail...> { // 特化，拆分
    typedef Tup1<Tail...> inherited;

   public:
    Tup1() {}
    Tup1(Head v, Tail... vtail) : m_head(v), inherited(vtail...) {}

    Head head() { return m_head; }
    inherited& tail() { return *this; }

   protected:
    Head m_head;
};

// 例子七， 递归复合
template <typename... Values> class Tup2;
template <> class Tup2<> {};

template <typename Head, typename... Tail>
class Tup2<Head, Tail...> {
    typedef Tup2<Tail...> composited;

   public:
    Tup2() {}
    Tup2(Head v, Tail... vtail) : m_head(v), m_tail(vtail...) {}

    Head head() { return m_head; }
    composited& tail() { return m_tail; }

   protected:
    Head m_head;
    composited m_tail;
};

int main(int argc, char* argv[]) {
    std::cout << "---------- 函数模板 ----------" << std::endl;
    // 1
    print(7.5, "hello", std::bitset<16>(377), 42);

    // 2
    int* pi = new int;
    printfx("%d %s %p %f\n", 15, "This is Ace", pi, 3.141596);

    // 3, 4
    std::cout << max({57, 48, 60, 100, 20, 18}) << std::endl;
    std::cout << max1(57, 48, 60, 100, 20, 18) << std::endl;
    std::cout << std::endl;

    std::cout << "---------- 类模板 ----------" << std::endl;

    // 5 - 递归创建
    std::cout << "递归创建 ---> ";
    std::cout << std::make_tuple(7.5, std::string("hello"),
                                 std::bitset<16>(377), 42);

    // 6 - 递归继承
    std::cout << "递归继承 ---> ";
    Tup1<int, float, std::string> t(41, 6.3, "nico");
    std::cout << t.head() << "," << t.tail().head() << std::endl;

    // 7 - 递归复合
    std::cout << "递归复合 ---> ";
    Tup2<int, float, std::string> it1(41, 6.3, "nico");
    std::cout << sizeof(it1) << std::endl;
    std::cout << it1.head() << std::endl;
    std::cout << it1.tail().head() << std::endl;
    std::cout << it1.tail().tail().head() << std::endl;

    Tup2<std::string, std::complex<int>, std::bitset<16>, double> it2(
        "Ace", std::complex<int>(3, 8), std::bitset<16>(377), 3.1415926);
    std::cout << sizeof(it2) << std::endl;
    std::cout << it2.head() << std::endl;
    std::cout << it2.tail().head() << std::endl;
    std::cout << it2.tail().tail().head() << std::endl;
    std::cout << it2.tail().tail().tail().head() << std::endl;

    return 0;
}
