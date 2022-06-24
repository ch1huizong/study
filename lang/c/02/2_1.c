#include <stdio.h>
// T: 价钱计算

int main(int argc, char *argv[]) {
    int price = 0;
    const int AMOUNT = 100;

    printf("请输入金额(元) : ");
    scanf("%d", &price);

    int change = AMOUNT - price;
    printf("找您%d元。\n", change);

    return 0;
}
