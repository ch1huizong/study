#include <iostream>
// T: 字符串连接，使用C语言的方法(method1)

char *link(char *a, char *b) {
    int m = 0, n = 0;

    // 统计字符个数
    while (a[m] != '\0')
        m++;

    while (b[n] != '\0')
        n++;

    // 创建动态字符数组
    char *c = new char[m + n + 1];

    // cp操作
    for (int i = 0; i < m; i++)
        c[i] = a[i];
    for (int i = m; i < m + n; i++)
        c[i] = b[i - m];
    c[m + n] = '\0';

    return c;
}

int main() {
    char a[] = "abc";
    char b[] = "def";
    std::cout << link(a, b) << std::endl;

    return 0;
}
