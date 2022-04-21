import java.awt.Color;

public class SplitBall extends BasicBall{ 
  
  public SplitBall(double r, Color c) {
    super(r,c);
    type = 3;
  }
     
     public int getScore() {
       return 10;
    }
}