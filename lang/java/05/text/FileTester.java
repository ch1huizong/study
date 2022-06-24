// T: 文件操作API - File

import java.io.*;

public class FileTester {
    public static void main(String[] args) {
        File f = new File("Hello.txt");

        if (f.exists()) {
            f.delete();
        } else {
            try {
                f.createNewFile();
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
