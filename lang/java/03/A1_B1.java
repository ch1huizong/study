// T: 子类对超类属性的覆盖_02

class A1 {
  int x = 2;

  public void setx(int i) {
    x = i;
  }

  public void printa() {
    System.out.println(x);
  }
}

class B1 extends A1 {
  int x = 100;

  public void printb() {
    super.x = super.x + 10;
    System.out.println("super.x = " + super.x + " x = " + x);
  }
}

public class A1_B1 {

  public static void main(String[] args) {
    A1 a1 = new A1();
    a1.setx(4);
    a1.printa();

    B1 b1 = new B1();
    b1.printb();
    b1.printa(); // 注意观察这里
    System.out.println();

    b1.setx(6);
    b1.printb();
    b1.printa();
    a1.printa();
  }
}
