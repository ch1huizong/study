// T: 多态的二次分发

public class DriverTest {

  public static void main(String[] args) {
    Driver a = new FemaleDriver();
    Driver b = new MaleDriver();
    Vehicle x = new Car();
    Vehicle y = new Bus();

    a.drives(x); // 司机类型, 交通工具
    b.drives(y);
  }
}
