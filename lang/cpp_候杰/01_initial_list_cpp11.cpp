// 初始化列表

#include <algorithm>
#include <initializer_list>
#include <iostream>
#include <vector>


// 匿名函数
auto I = [](int x) -> bool { return false; };

// 参数定义为初始化列表
void print(std::initializer_list<int> vals) {
	for (auto p = vals.begin(); p != vals.end(); ++p) {
		std::cout << *p << std::endl;
	}
};

template <typename T>
void print1(const T& coll) {	  // 如何构造一个T类型的coll?
	for (const auto& e : coll) { 
		std::cout << e << std::endl;
	}
}

// explicit类型转换
class P {
	public:
		P(int a, int b) {
			std::cout << "P(int, int), a=" << a << ", b=" << b << std::endl;
		};

		P(std::initializer_list<int> initlist) {  // 直接使用
			std::cout << "P(initializer_list<int>), values=";
			for (auto i : initlist) {
				std::cout << i << " ";
			}
			std::cout << std::endl;
		};

		// 明确调用，不允许隐式转换发生
		explicit P(int a, int b, int c) {
			std::cout << "explicit P(int a, int b, int c)" << std::endl;
		}
};

int main(int argc, char* argv[]) {

    // for-loop循环
	std::cout << "------- for:loop --------" << std::endl;
	std::vector<int> v {1, 2, 3, 4, 5};  // 一致化设初值
	for (auto& i : v) {
		i *= 2;
	}
	/*
	// 上面转化为下面这种形式了!
	for (auto i = v.begin(); i != v.end(); ++i) {
		std::cout << *i << std::endl;
	}
	*/
	for (auto i : {1, 3, 5, 7, 9}) {
		std::cout << i << " ";
	}
	std::cout << std::endl;

	print({7, 9, 2, 3, 5, 6, 1});

	P r{77, 5, 42};
	P s{77, 5};
	P error = {99, 88, 77};	 // 应该出错，怎么没出错?

	std::cout << "max:" << std::max({54, 16, 48, 5}) << std::endl;
	std::cout << "min:" <<std::min({54, 16, 48, 5}) << std::endl;

	return 0;
}
