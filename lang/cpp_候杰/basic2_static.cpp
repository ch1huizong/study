#include <iostream>

// 使用
class Account {
	public:
		static double m_rate;
		static void set_rate(const double& x) { m_rate = x; }
};

double Account::m_rate = 8.0;  // 一定要在外部定义

int main(int argc, char *argv[]) {
	Account::set_rate(9.0);	 // 1. 通过类调用
	std::cout << Account::m_rate << std::endl;

	Account a;
	a.set_rate(11.0);  // 2. 通过对象调用
	std::cout << a.m_rate << std::endl;

	return 0;
}
