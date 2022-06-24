// T: 接口实现类 - Rectangle

public class Rectangle implements Shape2D {

	private int w;
	private int h;

  public Rectangle(int w, int h) {
		this.w = w;
		this.h = h;
  }

  public double area() {
    return (w * h);
  }
}
