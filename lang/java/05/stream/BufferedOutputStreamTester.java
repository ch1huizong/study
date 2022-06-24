// T: 二进制文件 - 写 - 多种数据类型写入二进制文件

import java.io.*;

public class BufferedOutputStreamTester {
    public static void main(String[] args) {
        String name = "mixed.dat";

        try {
            DataOutputStream out =
                    new DataOutputStream(new BufferedOutputStream(new FileOutputStream(name)));
            out.writeInt(0);
            System.out.println(out.size() + " bytes has been written.");
            out.writeDouble(31.2);
            System.out.println(out.size() + " bytes has been written.");
            out.writeBytes("JAVA");
            System.out.println(out.size() + " bytes has been written.");

            out.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
