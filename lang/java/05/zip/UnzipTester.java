// T: 压缩解压缩 - zip - 恢复文件路径
// 有点bug

import java.io.*;
import java.util.zip.*;

class Unzip {

    private String zipName;
    private String unzipPath;
    private byte b[] = null;

    public Unzip(String zipName, String unzipPath) {
        this.zipName = zipName;
        this.unzipPath = unzipPath;
        this.setUnzipPath(this.unzipPath);
    }

    public Unzip(String zipName) {
        this.zipName = zipName;
        this.unzipPath = null;
        this.setUnzipPath(this.unzipPath);
    }

    private void setUnzipPath(String unzipPath) {
        if (unzipPath.endsWith("/")) {
            this.unzipPath = new String(unzipPath);
        } else {
            this.unzipPath = new String(unzipPath + '/');
        }
    }

    public void doUnzip() {
        try {
            ZipInputStream zips = new ZipInputStream(new FileInputStream(this.zipName));
            ZipEntry e = null;

            while ((e = zips.getNextEntry()) != null) {
                System.out.println("ZipEntry : " + e.getName());

                if (e.isDirectory()) {
                    checkFilePath(this.unzipPath + e.getName());
                } else {
                    //
                    // todo: 需要额外的文件处理操作
                    //
                    //
                    String f = new String(unzipPath + e.getName());
                    try {
                        FileOutputStream out = new FileOutputStream(f);

                        this.b = new byte[512];
                        int n;
                        while ((n = zips.read(this.b, 0, 512)) != -1) {
                            out.write(this.b, 0, n);
                        }

                        out.close();

                        out = null;
                        this.b = null;
                    } catch (IOException io) {
                        System.out.println(io.getMessage());
                    }
                }
            }

            zips.close();
        } catch (IOException e) {
            System.out.println("ioe");
        }
    }

    private void checkFilePath(String dirName) throws IOException {
        File dir = new File(dirName);
        if (!dir.exists()) {
            dir.mkdirs();
        }
    }
}

public class UnzipTester {
    public static void main(String[] args) {
        String zipName = args[0];
        String unzipPath = args[1] + '/';
        Unzip myzip = new Unzip(zipName, unzipPath);
        myzip.doUnzip(); // 解压并恢复路径
    }
}
