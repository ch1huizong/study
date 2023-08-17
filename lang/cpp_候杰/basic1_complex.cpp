// 无指针的类

#ifndef __COMPLEX__
#define __COMPLEX__

#include <cmath>
#include <iostream>

class complex {

	public:
		complex(double r = 0, double i = 0) : re(r), im(i) {}

		complex& operator+=(const complex&);

		double real() const { return re; }
		double imag() const { return im; }

		int func(const complex& param) {
			return param.re + param.im;	 // 直接访问re,im
		}

	private:
		double re, im;

		friend complex& __doapl(complex*, const complex&);  // 友元函数, 不是它的成员函数
};

// 返回原来的对象，引用
inline complex& __doapl(complex* ths, const complex& r) {
	ths->re += r.re;
	ths->im += r.im;

	return *ths;
}

// 设计为成员函数
inline complex& complex::operator+=(const complex& r) {
	return __doapl(this, r);
}

inline double real(const complex& x) { return x.real(); }
inline double imag(const complex& x) { return x.imag(); }

////////////////////////////////////////////////////////////
///
/// 接下来为运算符重载
///

// 设计为全局函数
inline complex operator+ (const complex& x, const complex& y) {
    // 这里返回临时对象, 返回值
	return complex(real(x) + real(y), imag(x) + imag(y));
}

inline complex operator+ (const complex& x, double y) {
	return complex(real(x) + y, imag(x));
}

inline complex operator+ (double x, const complex& y) {
	return complex(x + real(y), imag(y));
}

inline complex operator+ (const complex& x) { return x; }

inline complex operator- (const complex& x) { return complex(-real(x), -imag(x)); }

inline bool operator== (const complex& x, const complex& y) {
	return real(x) == real(y) && imag(x) == imag(y);
}

inline bool operator== (const complex& x, double y) {
	return real(x) == y && imag(x) == 0;
}
inline bool operator== (double x, const complex& y) {
	return x == real(y) && imag(y) == 0;
}

inline bool operator!= (const complex& x, const complex& y) {
	return real(x) != real(y) || imag(x) != imag(y);
}

inline bool operator!= (const complex& x, double y) {
	return real(x) != y || imag(x) != 0;
}
inline bool operator!= (double x, const complex& y) {
	return x != real(y) && imag(y) != 0;
}

inline complex conj(const complex& x) { return complex(real(x), -imag(x)); }

////////////////////////////////////////////////////////////

// 若返回值返回void,就不能连用了
inline std::ostream& operator<< (std::ostream& os, const complex& x) {
	// os前面不能加const
	return os << '(' << real(x) << ',' << imag(x) << ')';
}

int main(int argc, char* argv[]) {
	complex c1(2, 1);
	complex c2(100, 100);

	std::cout << "real=" << c1.real() << ',' << "image=" << c1.imag()
			  << std::endl;
	std::cout << c1 << '~' << conj(c1) << std::endl;

	c1 += c2;
	std::cout << c1 << std::endl;

	return 0;
}

#endif /* ifndef __COMPLEX__ */
