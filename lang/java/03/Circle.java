// T: 抽象类举例_03

abstract class GraphicObject {
  int x, y;

  void moveTo(int newX, int newY) {}
  ;

  abstract void draw();
}

public class Circle extends GraphicObject {
  void draw() {}
}
