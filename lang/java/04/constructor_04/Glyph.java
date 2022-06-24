public abstract class Glyph {

  abstract void draw();

  public Glyph() { 
    System.out.println("Glyph() before draw()");
    draw(); // 构造函数 + 调用了抽象方法
    System.out.println("Glyph() after draw()");
  }
}
