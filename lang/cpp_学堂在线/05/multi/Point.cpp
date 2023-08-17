#include "Point.h"

#include <iostream>
// T: Point类实现文件

int Point::count = 0;

Point::Point(const Point &p) : x(p.x), y(p.y) { count++; };

void Point::showCount() {
    std::cout << "Object count = " << count << std::endl;
}
