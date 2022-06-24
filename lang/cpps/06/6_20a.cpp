#include <iostream>
#include <vector>
// T: vector数组的使用case2

int main(int argc, char *argv[]) {
    std::vector<int> v = {1, 2, 3, 5, 4, 3};

    for (auto i = v.begin(); i != v.end(); ++i) { // 遍历方式1
        std::cout << *i << std::endl;
    }

    std::cout << std::endl;

    for (auto i : v) { // 遍历方式2
        std::cout << i << std::endl;
    }

    return 0;
}
