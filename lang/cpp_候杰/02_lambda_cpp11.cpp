// 匿名函数

#include <iostream>
#include <set>
#include <string>

auto I = [] { std::cout << "hello lambda!" << std::endl; };

void I2() {
	int id = 0;
	auto f = [id]() mutable {  // 捕获外部的符号, 注意mutable
		std::cout << "id: " << id << std::endl;
		++id;
	};

	id = 42;
	f(); // 连续调用间，函数维护了id的值? 类似闭包!
	f();
	f();
	std::cout << "id: " << id << std::endl;
}

void I3() {
	int id = 0;
	auto f = [&id](int param) {	 // 捕获外部的符号
		std::cout << "id: " << id << std::endl;
		std::cout << "param: " << param << std::endl;
		++id;
		++param;
	};

	id = 42;
	f(7);
	f(7);
	f(7);
	std::cout << id << std::endl;
}

class Person {
	public:
		Person(const char* first, const char* last) : firstname(first), lastname(last){};

		std::string firstname, lastname;
};

void I4() {
	auto cmp = [](const Person& p1, const Person& p2) {
		return (p1.lastname < p2.lastname) ||
			   (p1.lastname == p2.lastname && p1.firstname < p2.firstname);
	};

	// 此时cmp是函数实例， decltype(cmp)代表函数类
	std::set<Person, decltype(cmp)> coll(cmp);
}

int main(int argc, char* argv[]) {
	I();
	// I2();
	I3();
	//I4();

	return 0;
}
