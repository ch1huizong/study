// T: 类的综合应用 - 银行帐号

public class BankAccount {
  private static int LAST_ACCOUNT_NUMBER = 0;

  private String ownerName;
  private int accountNumber;
  private float balance;

  // this重载构造方法
  public BankAccount() {
    this("", 0.0f);
  }

  public BankAccount(String initName) {
    this(initName, 0.0f);
  }

  public BankAccount(String initName, float initBalance) {
    ownerName = initName;
    accountNumber = ++LAST_ACCOUNT_NUMBER;
    balance = initBalance;
  }

  public String toString() {
    return ("Account #"
        + new java.text.DecimalFormat("000000").format(accountNumber)
        + " with balance "
        + new java.text.DecimalFormat("$0.00").format(balance));
  }

  public String getOwnerName() {
    return ownerName;
  }

  public int getAccountNumber() {
    return accountNumber;
  }

  public float getBalance() {
    return balance;
  }

  public void setOwnerName(String newName) {
    ownerName = newName;
  }

  /*
  public void setAccountNumber(int newNum) {
    accountNumber = newNum;
  }

  public void setBalance(float newBalance) {
    balance = newBalance;
  }
  */

  public float deposit(float anAmount) {
    balance += anAmount;
    return balance;
  }

  public float withdraw(float anAmount) {
    if (anAmount <= balance) {
      balance -= anAmount;
    }

    return balance;
  }

  public static BankAccount sample1() {
    BankAccount ac = new BankAccount();
    ac.setOwnerName("che");
    ac.deposit(1000);

    return ac;
  }

  public static BankAccount sample2() {
    BankAccount ac = new BankAccount();
    ac.setOwnerName("yu");
    ac.deposit(1000);
    ac.deposit(2000);

    return ac;
  }

  public static BankAccount sample3() {
    BankAccount ac = new BankAccount();
    ac.setOwnerName("wang");

    return ac;
  }

  public boolean equals(Object x) {
    if (this.getClass() != x.getClass()) {
      return false;
    }

    BankAccount b = (BankAccount) x;
    return ((this.getOwnerName().equals(b.getOwnerName()))
        && (this.getAccountNumber() == b.getAccountNumber())
        && (this.getBalance() == b.getBalance()));
  }

  public int hashCode() {
    return super.hashCode();
  }

  public static void main(String[] args) {
    BankAccount bob, mary, biff;

    bob = BankAccount.sample1();
    mary = BankAccount.sample1();
    biff = BankAccount.sample2();

    mary.setOwnerName("Mary");
    mary.deposit(250);

    System.out.println(bob);
    System.out.println(mary);
    System.out.println(biff);
  }
}
