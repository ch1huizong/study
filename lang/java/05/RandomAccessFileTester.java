// T: 随机文件读写 - RandomAccessFile(自定义存储协议)

import java.io.*;

class Employee {
    char name[] = {'\u0000', '\u0000', '\u0000', '\u0000', '\u0000', '\u0000', '\u0000', '\u0000'};
    int age;

    public Employee(String name, int age) {
        if (name.toCharArray().length > 8) {
            System.arraycopy(name.toCharArray(), 0, this.name, 0, 8);
        } else {
            System.arraycopy(name.toCharArray(), 0, this.name, 0, name.toCharArray().length);
        }

        this.age = age;
    }
}

public class RandomAccessFileTester {
    private String Filename;

    public RandomAccessFileTester(String Filename) {
        this.Filename = Filename;
    }

    // 插入第几条记录
    public void writeEmployee(Employee e, int n) throws Exception {
        RandomAccessFile f = new RandomAccessFile(this.Filename, "rw");
        f.seek(n * 20);
        for (int i = 0; i < 8; i++) {
            f.writeChar(e.name[i]);
        }
        f.writeInt(e.age);
        f.close();
    }

    // 读取第几条记录
    public void readEmployee(int n) throws Exception {
        char t[] = new char[8];
        RandomAccessFile f = new RandomAccessFile(this.Filename, "r");
        f.seek(n * 20);
        for (int i = 0; i < 8; i++) {
            t[i] = f.readChar();
        }
        System.out.print("name: ");
        System.out.println(t);
        System.out.println("age: " + f.readInt());
        f.close();
    }

    public static void main(String[] args) throws Exception {
        RandomAccessFileTester t = new RandomAccessFileTester("/tmp/students.data");
        Employee e1 = new Employee("ZhangSanttt", 23);
        Employee e2 = new Employee("李晓珊", 33);
        Employee e3 = new Employee("王华", 19);

        t.writeEmployee(e1, 0);
        t.writeEmployee(e3, 2);
        System.out.println("第一个雇员信息:");
        t.readEmployee(0);
        System.out.println("第三个雇员信息:");
        t.readEmployee(2);
        t.writeEmployee(e2, 1);
        System.out.println("第二个雇员信息:");
        t.readEmployee(1);
    }
}
