#include <iostream>
#include <string>
#include <array>
#include <ctime>
#include <cstdlib>

using std::string;
using std::array;

#define ASIZE 500000

long get_a_target_long() {
    long target = 0;
    std::cout << "target (0~" << RAND_MAX << "): ";
    std::cin >> target;
    return target;
}

string get_a_target_string() {
    long target = 0;
    char buf[10];

    std::cout << "target (0~" << RAND_MAX << "): ";
    std::cin >> target;
    snprintf(buf, 10, "%d", target);

    return string(buf);
}

int compareLongs(const void* a, const void* b) {
    return (*(long*)a - *(long*)b);
}

int compareStrings(const void* a, const void* b) {
    if (*(string*) a > *(string*) b) {
       return 1; 
    } else if  (*(string*) a < *(string*) b) {
       return -1;
    } else {
        return 0;
    }
}

void test_array() {
    std::cout << "\ntest_array()......... \n" << std::endl;
    array<long, ASIZE> c;

    clock_t start = clock();
    for (long i = 0; i < ASIZE; ++i) {
        c[i] = rand();
    }
    clock_t end = clock();
    std::cout << "milli-seconds : " << (end - start) << std::endl;
    std::cout << "array.size() = " << c.size() << std::endl;
    std::cout << "array.front() = " << c.front() << std::endl;
    std::cout << "array.back() = " << c.back() << std::endl;
    std::cout << "array.data() = " << c.data() << std::endl;

    long target = get_a_target_long();
    start = clock();
    qsort(c.data(), ASIZE, sizeof(long), compareLongs);
    long* item = (long*)bsearch(&target, (c.data()), ASIZE, sizeof(long), compareLongs);
    end = clock();
    std::cout << "qsort() + bsearch(), milli-seconds : " << end - start << std::endl;

    if (item != NULL) {
        std::cout << "found, " << *item << std::endl;
    }else{
        std::cout << "not found! " << std::endl;
    }
}


int main(int argc, char *argv[])
{
    test_array();
    
    return 0;
}
