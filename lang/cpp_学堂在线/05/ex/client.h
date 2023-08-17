#ifndef CLIENT_H
#define CLIENT_H

class Client {
private:
  static char ServerName;
  static int ClientNum;

public:
  static void ChangeServerName(char name);
  static int GetClientNum();
};

#endif /* CLIENT_H */
