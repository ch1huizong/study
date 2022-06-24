// T: 接口实现类 - Circle

public class Circle implements Shape2D, Color { // 多继承

	private double r;
  private String color;

  public Circle(double r) {
		this.r = r;
  }

  public double area() {
    return (pi * r * r);
  }

  public void setColor(String str) {
    this.color = str;
    System.out.println("color = " + this.color);
  }

}
