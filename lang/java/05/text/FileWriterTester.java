// T: 文本文件- 写 - FileWriter

import java.io.*;

public class FileWriterTester {
    public static void main(String[] args) {
        String name = "Hello.txt";

        try {
            FileWriter w = new FileWriter(name, true); // 追加

            w.write("Hello!\n");
            w.write("This is my first text file, \n");
            w.write("You can see how this is done.\n");
            w.write("输入一行中文也可以\n");

            w.close();
        } catch (IOException e) {
            System.out.println("Problem writing " + name);
        }
    }
}
