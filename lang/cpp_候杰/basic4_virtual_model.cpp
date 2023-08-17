/* 虚机制的内存模型

虚机制(虚指针, 虚表) 
    - 多态 -> 同一个指针入口，具体指向不同的对象

    - VS 运行时决议 RTTI) VS 模板, 编译时决议

调用函数的方式不同，决定动态绑定和静态绑定, 决定会不会走虚路径

虚路径的触发方式:

    1. 显式, 如下
        动态绑定满足三个条件:(分清 => 不要和动态分配内存搞混)
            1. 指针
            2. 虚函数
            3. 向上转型(宽指针)

    2. 隐式
*/

#include <iostream>

class A {
	public:
		virtual void vf1() { std::cout << "IN A vf1" << std::endl; }
		virtual void vf2() { std::cout << "A base vf2" << std::endl; }

		void f1();
		void f2();

	private:
		int d1, d2;
};

class B : public A {
	public:
		virtual void vf1() { std::cout << "IN B vf1" << std::endl; }
		void f2();

	private:
		int d3;
};

class C : public B {
	public:
		virtual void vf1() { std::cout << "IN C vf1" << std::endl; }
		void f2();

	private:
		int d1, d4;
};

int main(int argc, char *argv[]) {
    // 静态绑定
	B b;
    A a = (A)b;
    a.vf1();

    // 动态绑定, 直接满足条件

    A* pa = new B; // case1 会触发, 有点类似范型编程
    pa->vf1();

    pa = &b; // case2
    pa->vf1();

    std::cout << "------------- 一般调用 --------------" << std::endl;

    // 一般调用
    // 走的是静态绑定，即直接函数调用，没走虚路径
	b.vf1();
	b.vf2();

	C c;
	c.vf1();

	C *p = new C;
	p->vf1();
	p->vf2();
    
	return 0;
}
