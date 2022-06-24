// T: 图形类 - class基础知识

class Circle {
  static double PI = 3.14159265; // 类变量
  int radius; // private 私有成员

  public Circle(int radius) {
    this.radius = radius;
  }

  public Circle() {
    this.radius = 0;
  }

  public double circumference() {
    return 2 * PI * radius;
  }

  public void enlarge(int factor) {
    radius = radius * factor;
  }

  public boolean fitsInside(Rectangle r) {
    return (2 * radius < r.width) && (2 * radius < r.height);
  }

  public int getRadius() {
    return this.radius;
  }

  public void setRadius(int radius) {
    this.radius = radius;
  }
}

class Rectangle {

  double width = 10.128;
  double height = 5.734;
}

public class Shape {

  static double maxArea(Circle c, Rectangle... varRec) { // 可变长参数函数定义
    double max = 0;
    Rectangle[] rec = varRec;
    for (Rectangle r : rec) {
      System.out.println(r);
    }
    return max;
  }

  public static void main(String[] args) {
    // 声明
    Circle x;
    Rectangle y;

    // 初始化
    System.out.println("初始化...");
    x = new Circle();
    y = new Rectangle();
    System.out.println(x);
    System.out.println("radius = " + x.radius);

    System.out.println(x + " " + y);
    System.out.println("\n");

    // 测试类变量
    System.out.println("测试类变量...");
    System.out.println(x.PI);
    System.out.println(Circle.PI);
    x.PI = 3.14;
    System.out.println(x.PI);
    System.out.println(Circle.PI);
    System.out.println("\n");

    // 测试实例方法
    System.out.println("测试实例方法...");
    Circle c1 = new Circle();
    c1.radius = 8;
    Circle c2 = new Circle();
    c2.radius = 15;
    Rectangle r = new Rectangle();
    r.width = 20;
    r.height = 30;

    System.out.println("Circle 1 fits inside Rectangle:" + c1.fitsInside(r));
    System.out.println("Circle 2 fits inside Rectangle:" + c2.fitsInside(r));
    System.out.println("\n");

    // 测试可变长参数
    System.out.println("测试变成参数函数定义...");
    Circle c = new Circle();
    Rectangle r1 = new Rectangle();
    Rectangle r2 = new Rectangle();
    System.out.println("max area of c, r1 and r2 is " + maxArea(c, r1, r2));
    System.out.println("max area of c, r1 is " + maxArea(c, r1));
    System.out.println("max area of c, r2 is " + maxArea(c, r2));
    System.out.println("max area of only c is " + maxArea(c));
  }
}
