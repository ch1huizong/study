// 函数模板 - 使用时不需要处理类型T, 根据实参推导T类型

#include <iostream>

class stone {
	public:
		stone(int w = 0, int h = 0, int we = 0) : _w(w), _h(h), _weight(we) {}

		bool operator< (const stone& rhs) const { return _w < rhs._w; }

	private:
		int _w, _h, _weight;
};

template <class T>
inline const T& min(const T& a, const T& b) {
	return a < b ? a : b;
}

int main(int argc, char* argv[]) {
	stone r1(2, 3), r2(3, 3), r3;
	r3 = min(r1, r2);

	return 0;
}
