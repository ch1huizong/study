// T: 引用类型转换后的"实例方法"和"类方法"的查找

public class MethodFind {
  public static void main(String[] args) {
    Manager man = new Manager();
    Employee emp1 = new Employee();
    Employee emp2 = (Employee)man;

    // 实例方法的查找
    emp1.computePay();
    man.computePay();
    emp2.computePay();

    System.out.println("\n");

    // 类方法的查找
    man.expenseAllowance();
    emp1.expenseAllowance();
    emp2.expenseAllowance();
  }
}
