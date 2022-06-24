// T: 文件压缩解压缩 - gzip格式

import java.io.*;
import java.util.zip.*;

public class GZIPTester {

    public static void main(String[] args) throws IOException {
        FileInputStream in = new FileInputStream("Hello.txt");
        GZIPOutputStream out = new GZIPOutputStream(new FileOutputStream("test.gz"));
        System.out.println("Writing compressing file from Hello.txt to test.gz");

        int c;
        while ((c = in.read()) != -1) {
            out.write(c); // 写
        }
        in.close();
        out.close();

        // 解压缩并打印
        System.out.println("Reading file from test.gz to monitor");
        BufferedReader in1 =
                new BufferedReader(
                        new InputStreamReader(new GZIPInputStream(new FileInputStream("test.gz"))));

        String s;
        while ((s = in1.readLine()) != null) {
            System.out.println(s);
        }
        in1.close();

        // 另存
        System.out.println("Writing decompression to newHello.txt");
        GZIPInputStream in2 = new GZIPInputStream(new FileInputStream("test.gz"));
        FileOutputStream out2 = new FileOutputStream("newHello.txt");
        while ((c = in2.read()) != -1) {
            out2.write(c);
        }
        in2.close();
        out2.close();
    }
}
