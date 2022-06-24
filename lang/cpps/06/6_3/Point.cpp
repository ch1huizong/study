#include "Point.h"

#include <iostream>

Point::Point() : x(0), y(0) {
    std::cout << "Default constructor called." << std::endl;
};

Point::Point(int x, int y) : x(x), y(y) {
    std::cout << "Constructor called." << std::endl;
};

Point::~Point() { std::cout << "Deconstructor called." << std::endl; };

void Point::move(int newX, int newY) {
    std::cout << "Moving to the point to (" << newX << "," << newY << ")"
              << std::endl;
    x = newX;
    y = newY;
}
