// T: 二进制文件- 读写 - 将255/0/-1二进制写入data1文件并读取计算

import java.io.*;

public class DataInputStreamTester {
    public static void main(String[] args) {
        String name = "data1.dat";
        String name1 = "trytry.dat";

        int value0 = 255, value1 = 0, value2 = -1;
        long sum = 0;

        // 写入二进制文件data1.dat
        try {
            DataOutputStream out =
                    new DataOutputStream(new BufferedOutputStream(new FileOutputStream(name)));
            out.writeInt(value0);
            out.writeInt(value1);
            out.writeInt(value2);
            out.close();
        } catch (Exception e) {
            System.out.println("Problem writing " + name);
        }

        // 读二进制文件data1.dat的整数并计算
        try {
            DataInputStream in =
                    new DataInputStream(new BufferedInputStream(new FileInputStream(name)));
            try {
                while (true) {
                    sum += in.readInt(); // 读取Int数据
                }
            } catch (EOFException eof) { // 通过捕获异常判断结束
                System.out.println("The sum is: " + sum);
                in.close();
            }
        } catch (IOException e) {
            System.out.println("IO Problems with " + name);
        }
        System.out.println("\n");

        // 写入并读取单字节到trytry.dat
        try {
            DataOutputStream out1 = new DataOutputStream(new FileOutputStream(name1));
            out1.writeByte(-1);
            out1.close();

            DataInputStream in1 = new DataInputStream(new FileInputStream(name1));
            int a = in1.readByte(); // 有符号读
            System.out.println(Integer.toHexString(a));
            System.out.println(a);

            in1.skip(-1);
            a = in1.readUnsignedByte(); // 无符号读
            System.out.println(Integer.toHexString(a));
            System.out.println(a);
            in1.close();
        } catch (IOException e) {
            System.out.println("IO Problems with " + name1);
        }
    }
}
