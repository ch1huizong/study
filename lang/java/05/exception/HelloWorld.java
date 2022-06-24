// T: 异常 - 非检查型异常(数组越界)

public class HelloWorld {

    public static void main(String[] args) {
        int i = 0;
        String greetings[] = {"Hello world!", "No, I mean it!", "HELLO WORLD!!"};

        while (i < 4) {
            System.out.println(greetings[i]);
            i++;
        }
    }
}
