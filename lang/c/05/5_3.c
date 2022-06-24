#include <stdio.h>
// T: 凑硬币，1、2、5凑x元

int main(int argc, char *argv[]) {
    int x;
    scanf("%d", &x);

    for (int i = 1; i < x * 10; ++i) {
        for (int j = 1; j < x * 10 / 2; ++j) {
            for (int k = 1; k < x * 10 / 5; ++k) {
                if (i + 2 * j + 5 * k == x * 10) {
                    printf("你可以用%d个1角加%d个2角加%d个5角得到%d元\n", i, j,
                           k, x);
                    goto out;
                }
            }
        }
    }

out:
    return 0;
}
