#include <iostream>
// T: 常量指针和指针常量(关键是const在*前还是后)

int main(int argc, char *argv[]) {
    int a = 798;
    const int *p1 = &a; // 不能通过p1修改指向目标的值
    //*p1 = 1;            // 编译会出错
    int b;
    p1 = &b; // 但可以修改p1的指向

    int *const p2 = &a;
    *p2 = 666;
    printf("a = %d\n", a);
    // p2 = &b; //指针p2不能转向

    return 0;
}
