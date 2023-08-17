#include <iostream>
// T: 指针和函数
// 只读(常量)指针的应用,避免函数修改原对象数据

const int N = 6;
void print(const int *p, int n);

int main(int argc, char *argv[]) {
    int array[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> array[i];
    }

    print(array, N);

    return 0;
}

void print(const int *p, int n) {
    std::cout << "{" << *p;
    for (int i = 1; i < n; ++i) {
        std::cout << "," << *(p + i);
    }
    std::cout << "}" << std::endl;
}
