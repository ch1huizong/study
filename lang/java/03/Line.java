// T: 类的组合_05

class Point {
  private int x;
  private int y;

  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }

  public int getX() {
    return x;
  }

  public int getY() {
    return y;
  }
}

public class Line {
  private Point p1;
  private Point p2;

  public Line(Point a, Point b) {
    this.p1 = new Point(a.getX(), a.getY()); // 注意这里的构造
    this.p2 = new Point(b.getX(), b.getY());
  }

  public double Length() {
    return Math.sqrt(Math.pow(p2.getX() - p1.getX(), 2) + Math.pow(p2.getY() - p1.getY(), 2));
  }

  public static void main(String[] args) {}
}
