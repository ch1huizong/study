// T: 标准输入输出重定向-文件复制

import java.io.*;

public class Redirecting {

    public static void main(String[] args) throws IOException {
        BufferedInputStream in =
                new BufferedInputStream(new FileInputStream("Redirecting.java")); // 输入流
        PrintStream out =
                new PrintStream(new BufferedOutputStream(new FileOutputStream("test.out"))); // 输出流

        // 重定向标准输入输出
        System.setIn(in);
        System.setOut(out);
        System.setErr(out);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s;

        while ((s = br.readLine()) != null) {
            System.out.println(s);
        }
        in.close();
        out.close();
    }
}
