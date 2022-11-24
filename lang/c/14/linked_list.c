#include <stdio.h>
#include <stdlib.h>

#include "linked_list.h"

int main(int argc, char* argv[]) {
    List list;
    list.head = NULL;
    int number = 0;

    do {
        scanf("%d", &number);
        if (number != -1) {
            add(&list, number);
        }
    } while (number != -1);

    print(&list);
    find(&list, 10);
    remove1(&list, 10);
    print(&list);
    
    clear(&list);

    return 0;
}

void add(List* pList, int number) {
    Node* p = (Node*)malloc(sizeof(Node));
    p->value = number;
    p->next = NULL;

    // 寻找最后一个节点，从头开始找
    Node* last = pList->head;
    if (last) {  // 若已创建link表
        while (last->next) {
            last = last->next;
        }
        last->next = p;  // 找到最后一个节点
    } else {
        pList->head = p;  // 初始化头指针
    }
}

void print(List* pList) {
    Node* p;
    for (p = pList->head; p; p = p->next) {
        printf("%d\n", p->value);
    }
}

void find(List* pList, int target) {
    Node* p;
    for (p = pList->head; p; p = p->next) {
        if (p->value == target) {
            printf("Found target = %d\n", target);
            break;
        }
    }
}

void remove1(List* pList, int target) {
    Node* pre;
    Node* p;

    for (pre = NULL, p = pList->head; p; pre = p, p = p->next) {
        if (p->value == target) {
            if (pre) {
                pre->next = p->next;  // 前提pre不为空
            } else {
                pList->head = p->next;
            }
            free(p);  // 释放当下的p指向节点
            break;
        }
    }
}

void clear(List* pList) {
    Node* p;
    Node* post;

    for (p = pList->head; p; p = post) {
        post = p->next;
        free(p);
    }
}
