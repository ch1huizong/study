#ifndef EMPLOYEE_H_
#define EMPLOYEE_H_

#include <iostream>

class Employee {
  std::string name;
  std::string address;
  std::string city;
  std::string code;

public:
  Employee(std::string n = "", std::string add = "", std::string ct = "", std::string cd = ""): name(n), address(add), city(ct), code(cd){};

  void display() {
    std::cout << "name: " << name << std::endl;
    std::cout << "address: " << address << std::endl;
    std::cout << "city: " << city << std::endl;
    std::cout << "code: " << code << std::endl;
    std::cout << std::endl;
  }

  void change_name(std::string nm) { name = nm; }

};

#endif
