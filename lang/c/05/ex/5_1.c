#include <stdio.h>
// T: 输出不相同并且有序的三位数

int main(int argc, char *argv[]) {
    int a;
    scanf("%d", &a);
    int cnt = 0;

    for (int i = a; i <= a + 3; ++i) {
        for (int j = a; j <= a + 3; j++) {
            for (int k = a; k <= a + 3; k++) {
                if (i != j && i != k && j != k) {
                    printf("%d%d%d", i, j, k);
                    cnt++;

                    if (cnt % 6 == 0) {
                        printf("\n");
                    } else {
                        printf(" ");
                    }
                }
            }
        }
    }
    printf("\n");

    return 0;
}
