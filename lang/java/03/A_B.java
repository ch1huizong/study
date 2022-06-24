// T: private属性的在继承中的访问控制_02

class B {
  public int a = 10;
  private int b = 20; // 不能被子类访问
  protected int c = 30;

  public int getB() {
    return b;
  }
}

class A extends B {
  public int d;

  public void tryVariables() {
    System.out.println(a);
    System.out.println(b); // 不允许访问
    System.out.println(getB());
    System.out.println(c);
  }
}

public class A_B {
  public static void main(String[] args) {
    A a = new A();
    a.tryVariables();
  }
}
