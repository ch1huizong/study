// T: 对象序列化 - ObjectOutputStream/ObjectInputStream

import java.io.*;

class Book implements Serializable {

    int id;
    String name;
    String author;
    float price;

    public Book(int id, String name, String author, float price) {
        this.id = id;
        this.name = name;
        this.author = author;
        this.price = price;
    }
}

public class SerializableTester {

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Book book = new Book(100032, "Java Programming", "che", 30);

        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("book.dat"));
        out.writeObject(book); // 一个对象占多少字节?
        out.close();

        book = null;
        ObjectInputStream in = new ObjectInputStream(new FileInputStream("book.dat"));
        book = (Book) in.readObject();
        in.close();

        System.out.println("ID is: " + book.id);
        System.out.println("name is: " + book.name);
        System.out.println("author is: " + book.author);
        System.out.println("price is: " + book.price);
    }
}
