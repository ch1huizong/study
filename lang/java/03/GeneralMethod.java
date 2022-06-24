// T: 泛形方法_04

public class GeneralMethod {
  <Type> void printClassName(Type object) { // 定义泛型方法
    System.out.println(object.getClass().getName());
  }

  public static void main(String[] args) {
    GeneralMethod gm = new GeneralMethod();
    gm.printClassName("hello");
    gm.printClassName(3);
    gm.printClassName(3.0f);
    gm.printClassName(3.0);
  }
}
