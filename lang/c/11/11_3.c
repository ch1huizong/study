// T: 指向结构体的指针
#include <stdio.h>

struct point {
    int x;
    int y;
};

struct point *getStruct(struct point *);
void output(struct point);
void print(const struct point *);

int main(int argc, char *argv[]) {
    struct point y = {0, 0};

    // getStruct(&y); // 1
    // output(y);
    // output(*getStruct(&y)); // 2
    print(getStruct(&y));  // 3

    return 0;
}

struct point *getStruct(struct point *p) {  // 会改变内容
    scanf("%d", &p->x);                     // 暗示了优先级(->, &)
    scanf("%d", &p->y);
    printf("getStruct: %d %d\n", p->x, p->y);

    return p;
}

void output(struct point p) { printf("output: %d %d\n", p.x, p.y); }

void print(const struct point *p) { printf("print: %d %d\n", p->x, p->y); }

