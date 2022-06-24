// T: 构造方法在继承中的调用_02

class Person {
  protected String name;
  protected String phoneNumber;
  protected String address;

  public Person() {
    this("", "", "");
  }

  public Person(String name, String phoneNumber, String address) {
    this.name = name;
    this.phoneNumber = phoneNumber;
    this.address = address;
  }
}

class Employee extends Person {
  protected int employeeNumber;
  protected String workPhoneNumber;

  public Employee() {
    // 此处隐含调用构造方法Person()
    this(0, "");
  }

  public Employee(int employeeNumber, String workPhoneNumber) {
    // 此处隐含调用构造方法Person()
    this.employeeNumber = employeeNumber;
    this.workPhoneNumber = workPhoneNumber;
  }
}

public class Professor extends Employee {
  protected String research;

  public Professor() {
    super();
    research = "";
  }

  public Professor(int number, String phoneNumber, String research) {
    super(number, phoneNumber);
    this.research = research;
  }

  public static void main(String[] args) {
    Professor p1 = new Professor();
    Professor p2 = new Professor(123456, "5135728", "network security");
    System.out.println("p1 = " + p1);
    System.out.println("p2 = " + p2);
  }
}
