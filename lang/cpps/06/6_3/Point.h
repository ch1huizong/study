#ifndef POINT_H
#define POINT_H

class Point {
private:
  int x, y;

public:
  Point();
  Point(int x, int y);
  ~Point();

  void move(int newX, int newY);
  int getX() const { return x; };
  int getY() const { return y; };
  static void showCount();
};

#endif /* POINT_H */
