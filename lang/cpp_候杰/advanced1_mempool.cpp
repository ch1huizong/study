#include <iostream>

class Screen
{
public:
    Screen (int x): i(x) {};
    int get() { return i; }

    void* operator new(size_t);
    void operator delete(void*, size_t);

private:
    Screen* next;
    static Screen* freeStore; // next
    static const int screenChunk; // elements, 总共多少块


private:
    int i;
};

Screen* Screen::freeStore = 0;
const int Screen::screenChunk = 24;

void* Screen::operator new(size_t size) {
    Screen* p;
    if (!freeStore) {
        size_t chunk = size * screenChunk; // 分配一大块内存
        freeStore = p = reinterpret_cast<Screen*>(new char[chunk]);

        for (; p!= &freeStore[screenChunk - 1]; ++p) {
            p->next = p + 1;
        }
        p->next = 0; // 最后一个节点的next属性指向空
    }

    p = freeStore;
    freeStore = freeStore->next;
    return p;
}

void Screen::operator delete(void* p, size_t) {
   (static_cast<Screen*>(p))->next = freeStore; // 释放的节点，指向下一个空白
   freeStore = static_cast<Screen*>(p); // 空白转向
}

int main(int argc, char *argv[])
{
    std::cout << sizeof(Screen) << std::endl;

    size_t const N = 100;
    Screen* p[100];
    for (int i = 0; i < N; ++i) {
        p[i] = new Screen(i);
    }

    for (int i = 0; i < 10; ++i) { // 确认每一块内存间，没有cookie
        std::cout << p[i] << std::endl;
    }

    for (int i = 0; i < N; ++i) {
        delete p[i];
    }
    
    return 0;
}
    
