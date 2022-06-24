#include <iostream>

#include "client.h"

int Client::ClientNum = 0;
char Client::ServerName = 'a';

int main(int argc, char *argv[]) {
    Client c1;
    c1.ChangeServerName('a');
    std::cout << c1.GetClientNum() << std::endl;
    Client c2;
    c2.ChangeServerName('b');
    std::cout << c2.GetClientNum() << std::endl;

    return 0;
}
