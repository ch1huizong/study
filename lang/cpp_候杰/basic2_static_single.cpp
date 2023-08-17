// 单例模式

#include <iostream>

class A {
	public:
		static A& getInstance();
		void setup() { std::cout << "建立一个A单例" << std::endl; }

	private:
		A(int a = 18, int s = 1024) : age(a), salary(s) {
			std::cout << "单例的默认构造函数" << std::endl;
		};
		A(const A& rhs){};

		int age, salary;

		// static A a;  // 可以没构造？
};

A& A::getInstance() {
	static A a;	 // 若无调用函数者，就会没构造？
	return a;
}

int main(int argc, char* argv[]) {
	// A::getInstance().setup();
	std::cout << "main" << std::endl;

	return 0;
}
