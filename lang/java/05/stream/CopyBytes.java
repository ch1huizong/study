// T: 二进制文件- DataInputStream/DataOutputStream -通过字节复制，完成文件复制

import java.io.*;

public class CopyBytes {

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Please enter the file names");
            return;
        }

        File src = new File(args[0]); // 测试文件
        File dst = new File(args[1]);
        if (dst.exists()) {
            System.out.println(args[1] + " already exists.");
            return;
        }
        if (!src.exists()) {
            System.out.println(args[0] + " does not exist.");
            return;
        }

        try {
            DataInputStream in =
                    new DataInputStream(new BufferedInputStream(new FileInputStream(src)));
            DataOutputStream out =
                    new DataOutputStream(new BufferedOutputStream(new FileOutputStream(dst)));

            try {
                int data;
                while (true) {
                    data = in.readUnsignedByte(); // 读字节
                    out.writeByte(data); // 写字节
                }
            } catch (EOFException eof) {
                in.close();
                out.close();
                return;
            }

        } catch (FileNotFoundException e) {
            System.out.println("Problem opening files");
        } catch (IOException e) {
            System.out.println("IO Problems");
        }
    }
}
