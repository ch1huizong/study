// T: 遍历 - 03 - Lambda

import java.util.ArrayList;

public class LambdaTester {

  public static void main(String[] args) {
    ArrayList<String> al = new ArrayList<String>();
    al.add("Che");
    al.add("Zhang");
    al.add("Wang");

    al.stream().forEach(e -> System.out.println(e));
  }
}
