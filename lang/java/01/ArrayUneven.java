// T: 二维数组

public class ArrayUneven {

  public static void main(String[] args) {
    int[][] uneven = {
      {1, 9, 4},
      {0, 2},
      {0, 1, 2, 3, 4},
    };

    System.out.println("Length of array is:" + uneven.length); // 行数
    System.out.println("Length of row[0] is:" + uneven[0].length);
    System.out.println("Length of row[1] is:" + uneven[1].length);
    System.out.println("Length of row[2] is:" + uneven[2].length);
  }
}
