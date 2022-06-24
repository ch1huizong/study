// T: 构造函数 + 多态会引起的问题

public class RoundGlyph extends Glyph {
  int radius = 1;

  RoundGlyph(int r) {
    // super.Glyph();  默认会调用超类的默认构造方法
    radius = r;
    System.out.println("RoundGlyph.RoundGlyph(), radius = " + radius);
  }

  void draw() {
    System.out.println("RoundGlyph.draw(), radius = " + radius);
  }

  public static void main(String[] args) {
    new RoundGlyph(15);
  }

}
