#include <iostream>
// 递归函数-3
// 汉诺塔问题, 关键是理解递归思想
// Value

int counter = 0;

//将src针的最上面一个盘子移动到dest针上
void move(char src, char dest) {
    std::cout << src << " --> " << dest << std::endl;
    counter += 1;
}

//将n个盘子从src针移动到dest针，以medium针作为中转
void hanoi(int n, char src, char medium, char dest) {
    if (n == 1) {
        move(src, dest);
    } else {
        hanoi(n - 1, src, dest, medium);
        move(src, dest);
        hanoi(n - 1, medium, src, dest);
    }
}

int main(int argc, char *argv[]) {
    int m;
    std::cout << "Enter the number of disks: ";
    std::cin >> m;
    std::cout << "the steps to moving " << m << "disks:" << std::endl;
    hanoi(m, 'A', 'B', 'C');
    std::cout << "hanoi be called: " << counter << std::endl;

    return 0;
}
