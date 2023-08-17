#ifndef POINT_H
#define POINT_H 

// 类声明文件
class Point {
private:
  int x, y;
  static int count;

public:
  Point(int x = 0, int y = 0) : x(x), y(y){};
  Point(const Point &p);
  ~Point() { count--; };

  int getX() const { return x; };
  int getY() const { return y; };

  static void showCount();
};

#endif /* POINT_H */
