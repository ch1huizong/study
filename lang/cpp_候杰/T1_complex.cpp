// 类模板 - 使用时, 主要处理类型T

#ifndef __complex__
#define __complex__

#include <iostream>

template <typename T>
class complex {
	public:
		complex(T r = 0, T i = 0) : re(r), im(i) {}

		T real() const { return re; }
		T imag() const { return im; }

	private:
		T re, im;
};

int main(int argc, char *argv[]) {
	complex<int> c1(4, 7);
	complex<double> c2(4.0, 7.0);

	std::cout << c1.real() << std::endl;
	std::cout << c2.real() << std::endl;

	return 0;
}

#endif /* ifndef __COMPLEX1__ */
