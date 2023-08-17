#include "client.h"

#include <iostream>

void Client::ChangeServerName(char name) {
    Client::ServerName = name;
    Client::ClientNum++;
}

int Client::GetClientNum() { return Client::ClientNum; }
