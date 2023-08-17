
// 数据转换 vs explicit构造函数
// using、noexcept、overwrite、final、decltype

#include <iostream>

class Fraction {
	public:
		explicit Fraction(int num, int den = 1) : m_num(num), m_den(den) {}

		// 转换函数 - 定制数据转换规则
		// operator double() const { return (double)(m_num / (m_den + 0.0)); }

		Fraction operator+ (const Fraction &f) {
			return *this;  // 空实现
		}

	public:
		int m_num;	// 分子
		int m_den;	// 分母
};

int main(int argc, char *argv[]) {
	Fraction f(3, 5);
	// double d = 4 + f;
	// std::cout << d << std::endl;

	Fraction d1 = f + 4;  // 会有隐含转换, 但是加了explicit会有转换失败

	return 0;
}
