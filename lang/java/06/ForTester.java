// T: 遍历 - 02 - 增强For循环遍历

import java.util.Vector;

public class ForTester {
    public static void main(String[] args) {
        Vector<String> v = new Vector<String>();
        v.add("Sunday");
        v.add("Monday");
        v.add("Tuesday");
        v.add("Wednesday");
        v.add("Thursday");
        v.add("Friday");
        v.add("Saturday");

        for (String day : v) {
            System.out.println(day);
        }
    }
}
