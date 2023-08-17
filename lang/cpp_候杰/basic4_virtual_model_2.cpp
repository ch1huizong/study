// 虚函数的又一应用场景

#include <iostream>

class Framework {
	public:
		void OnFileOpen();
		virtual void Serialize(){};	 // 必须这样写吗? 是的!

	private:
		int data1;
};

void Framework::OnFileOpen() {
	std::cout << "Before Serialize" << std::endl;
	Serialize();
	std::cout << "After Serialize" << std::endl;
}

class MyDoc : public Framework {
	public:
		virtual void Serialize() {
			std::cout << "I am in MyDoc, Serialize!" << std::endl;
		}

	private:
		int data2;
};

int main(int argc, char *argv[]) {
	MyDoc my;

    // 间接满足条件, 会隐式调用虚机制
	my.OnFileOpen(); // 你自己回答，为何会调用子类的Serialize方法?

	return 0;
}
