// T: 多态举例
/*
 *  多态(基础)
 *
 *  1. 向上转型
 *  2. 动态绑定
 *
 */

public class BindingTester {

  public static void main(String[] args) {
    Shape[] s = new Shape[9];
    int n;

    for (int i = 0; i < s.length; i++) {
      n = (int) (Math.random() * 3);
      switch (n) {
        case 0:
          s[i] = new Circle();
          break;
        case 1:
          s[i] = new Square();
          break;
        case 2:
          s[i] = new Triangle();
          break;
      }
    }

    for (int i = 0; i < s.length; i++) {
      s[i].draw(); // 统一的接口访问
    }
  }
}
