// T: 类的继承举例_01

class Person {
  public String name;

  public String getName() {
    return name;
  }
}

class Employee extends Person {
  public int employeeNumber;

  public int getEmployeeNumber() {
    return employeeNumber;
  }
}

public class Manager extends Employee {
  public String responsibilities;

  public String getResponsibilities() {
    return responsibilities;
  }

  public static void main(String[] args) {
    Employee e = new Employee();
    e.name = "che";
    e.employeeNumber = 666666;
    System.out.println(e.getName());
    System.out.println(e.getEmployeeNumber());
    System.out.println();

    Manager m = new Manager();
    m.name = "wang";
    m.employeeNumber = 888888;
    m.responsibilities = "Internet project";
    System.out.println(m.getName());
    System.out.println(m.getEmployeeNumber());
    System.out.println(m.getResponsibilities());
  }
}
