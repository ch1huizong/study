#include <stdio.h>
#include <stdlib.h>

#include "array.h"

const int BLOCK_SIZE = 3;

Array array_create(int init_size) {
    Array a;
    a.size = init_size;
    a.array = (int*)malloc(sizeof(int) * a.size);
    return a;
}

void array_free(Array* a) {
    free(a->array);
    a->array = NULL;
    a->size = 0;
}

// 封装, c++可以实现相应机制
int array_size(Array* a) { 
    return a->size; 
}

int* array_at(Array* a, int index) {
    if (index >= a->size) {
        // array_inflate(a, (index / BLOCK_SIZE + 1) * BLOCK_SIZE - a->size) ;  // 是不是讲错了?
        array_inflate(a, BLOCK_SIZE);
    }
    return &(a->array[index]);
}

int array_get(const Array* a, int index) { 
    return a->array[index]; 
}

void array_set(Array* a, int index, int value) { 
    a->array[index] = value;
}

void array_inflate(Array* a, int more_size) {
    int* p = (int*)malloc(sizeof(int) * (a->size + more_size)); // realloc ?
    printf("Alloc memory, total size: %d\n", a->size + more_size);

    for (int i = 0; i < a->size; ++i) {  // memcpy ?
        p[i] = a->array[i];
    }

    free(a->array);
    a->array = p;
    a->size += more_size;
}

int main(int argc, char* argv[]) {
    Array a = array_create(2);
    printf("array size = %d\n", array_size(&a));

    *array_at(&a, 0) = 10;
    printf("%d\n", *array_at(&a, 0));

    int number = 0;
    int cnt = 0;
    while (number != -1) {
        scanf("%d", &number);
        if (number != -1) {
            *array_at(&a, cnt++) = number;
        }
        //scanf("%d", array_at(&a, cnt++));
    }
    array_free(&a);

    return 0;
}
