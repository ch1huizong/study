// T: 一维数组

public class ArrayDemo {

  public static void main(String[] args) {
    int[] a1 = {1, 2, 3, 4, 5};
    int[] a2;
    a2 = a1; // 数组名是一个引用

    for (int i = 0; i < a2.length; i++) {
      a2[i]++;
    }
    for (int i = 0; i < a1.length; i++) {
      System.out.println("a1[" + i + "] = " + a1[i]);
    }

    // 字符串数组
    String[] anArray = {"String One", "String Two", "String Three"};
    for (int i = 0; i < anArray.length; i++) {
      System.out.println(anArray[i].toLowerCase());
    }

    // 数组复制
    char[] copyFrom = {'d', 'e', 'c', 'a', 'f', 'f', 'e', 'i', 'n', 'a', 't', 'e', 'd'};
    char[] copyTo = new char[7];
    System.arraycopy(copyFrom, 2, copyTo, 0, 7);
    System.out.println(new String(copyTo));
  }
}
