// T: 修改Object的equals方法

public class Apple {
  private String color;
  private boolean ripe;

  public Apple(String aColor, boolean isRipe) {
    color = aColor;
    ripe = isRipe;
  }

  public void setColor(String aColor) {
    color = aColor;
  }

  public void setRipe(boolean isRipe) {
    ripe = isRipe;
  }

  public String getColor() {
    return color;
  }

  public boolean getRipe() {
    return ripe;
  }

  public String toString() {
    if (ripe) {
      return ("A ripe " + color + " apple");
    } else {
      return ("A not so ripe " + color + " apple");
    }
  }

  // Object的equals主要判断是否是同一个目标!
  public boolean equals(Object obj) {
    if (obj instanceof Apple) {
      Apple a = (Apple) obj;
      return (color.equals(a.getColor()) && (ripe == a.getRipe()));
    }
    return false;
  }

  public static void main(String[] args) {
    Apple a = new Apple("red", true);
    Apple b = new Apple("red", true);

    if (a.equals(b)) {
      System.out.println("Apple:a equals Apple:b");
    } else {
      System.out.println("Apple:a != Apple:b");
    }
  }
}
