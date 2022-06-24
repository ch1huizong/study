// T: 文本文件- 读 - BufferedReader

import java.io.*;

public class BufferedReaderTester {
    public static void main(String[] args) {
        String name = "Hello.txt", line;

        try {
            BufferedReader in = new BufferedReader(new FileReader(name));
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }

            in.close();
        } catch (IOException e) {
            System.out.println("Problem reading " + name);
        }
    }
}
