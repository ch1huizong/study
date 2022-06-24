// T: 压缩和解压缩 - zip格式 - 命令行读入一系列文本文件

import java.io.*;
import java.util.zip.*;

public class ZipOutputStreamTester {

    public static void main(String[] args) throws IOException {
        ZipOutputStream out =
                new ZipOutputStream(new BufferedOutputStream(new FileOutputStream("test.zip")));

        // 压缩
        for (int i = 0; i < args.length; i++) {
            System.out.println("Writing file " + args[i]);
            BufferedInputStream in = new BufferedInputStream(new FileInputStream(args[i]));

            out.putNextEntry(new ZipEntry(args[i])); // 注意添加文件头条目

            int c;
            while ((c = in.read()) != -1) {
                out.write(c);
            }
            in.close();
        }
        out.close();

        // 解压缩到屏幕
        System.out.println("Reading file");
        ZipInputStream in1 =
                new ZipInputStream(new BufferedInputStream(new FileInputStream("test.zip")));
        ZipEntry e;

        while ((e = in1.getNextEntry()) != null) {
            System.out.println("Reading file " + e.getName());

            int x;
            while ((x = in1.read()) != -1) {
                System.out.write(x);
            }

            System.out.println();
        }

        in1.close();
    }
}
