// T: 异常 - 生成并抛出异常, 可以自定义预判

public class ThrowTest {
    public static void main(String[] args) {
        try {
            throw new ArithmeticException();
        } catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();
        }

        try {
            throw new ArrayIndexOutOfBoundsException();
        } catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();
        }

        try {
            throw new StringIndexOutOfBoundsException();
        } catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();
        }
    }
}
