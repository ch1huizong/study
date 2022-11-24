#ifndef _NODE_LIST_
#define _NODE_LIST_

typedef struct _node {
    int value;
    struct _node* next;  // 不能替换成Node, 因为此时Node未定义
} Node;

typedef struct _list {
    Node* head;
} List;

void add(List* pList, int number);

void print(List* pList);

void find(List* pList, int target);

void remove1(List* pList, int target);

void clear(List* pList);

#endif /* ifndef _NODE_LIST_ */
