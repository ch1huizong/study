// 有指针成员的类, big-three
#ifndef __MYSTRING__
#define __MYSTRING__

#include <cstring>
#include <iostream>
#include <ostream>

class String {
   public:
    String(const char* cstr = 0);  // 声明中指定参数默认值

    // big three
    String(const String& str);      // 拷贝构造
    String(String&& str) noexcept;  // 移动构造
    String& operator=(const String& str);  // 拷贝赋值
    String& operator=(String&& str) noexcept; // 移动赋值
    ~String();  // 析构函数

    bool operator<(const String& rhs) const;
    bool operator==(const String& rhs) const;

    char* get_c_str() const { return m_data; }

   private:
    char* m_data;
};

// 构造函数
inline String::String(const char* cstr) {
    if (cstr) {
        m_data = new char[strlen(cstr) + 1];
        strcpy(m_data, cstr);
    } else {
        m_data = new char[1];
        *m_data = '\0';
    }
}

// 拷贝构造 => 新建对象
inline String::String(const String& str) {
    m_data = new char[strlen(str.m_data) + 1];  // 注意这里可str.m_data访问私有成员
    strcpy(m_data, str.m_data);
}

// 移动构造 => 浅拷贝
inline String::String(String&& str) noexcept : m_data(str.m_data) {
    str.m_data = NULL;
}

// 拷贝赋值 => 修改已有对象
inline String& String::operator=(const String& str) {
    if (this == &str) {  // 必须自我赋值检测, 效率和正确性
        return *this;
    }

    delete[] m_data;                            // 1
    m_data = new char[strlen(str.m_data) + 1];  // 2
    strcpy(m_data, str.m_data);                 // 3

    return *this;  // 最好返回，链式调用
}

// 移动赋值
inline String& String::operator=(String&& str) noexcept {
    if (this == &str) {  // 必须自我赋值检测, 效率和正确性
        return *this;
    }

    delete[] m_data;
    m_data = str.m_data;
    str.m_data = NULL;

    return *this;
}

inline String::~String() {
    if (m_data) {
        delete[] m_data;
    }
}

bool String::operator<(const String& rhs) const {
    return std::string(this->m_data) < std::string(rhs.m_data);
}

bool String::operator==(const String& rhs) const {
    return std::string(this->m_data) < std::string(rhs.m_data);
}

std::ostream& operator<<(std::ostream& os, const String& str) {
    os << str.get_c_str();
    return os;
}

int main(void) {
    String s1;
    String s2("hello");

    String s3(s1);
    std::cout << s3 << std::endl;

    s3 = s2;
    std::cout << s3 << std::endl;

    String* p = new String("hello");  // 动态分配的方式
    delete p;

    return 0;
}

#endif /* ifndef __MYSTRING__ */
