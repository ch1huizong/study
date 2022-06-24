// T: 遍历- 01 - Iterator

import java.util.Arrays;
import java.util.Iterator;
import java.util.Vector;

public class IteratorTester {

    public static void main(String[] args) {
        String[] num = {
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"
        };
        Vector<String> v = new Vector<String>(Arrays.asList(num));
        System.out.println("Before Vector: " + v);

        Iterator<String> i = v.iterator(); // 获得迭代器
        while (i.hasNext()) {
            String s = i.next();
            System.out.println(s);
            if (s.length() > 4) {
                i.remove(); // 会改变Vector集合元素
            }
        }
        System.out.println("After Vector: " + v);
    }
}
