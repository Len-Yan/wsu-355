import java.awt.Color;

public class ShrinkBall extends BasicBall{ 
  private double rawradius;
  
  public ShrinkBall(double r, Color c) {
    super(r,c);
    radius = r;
    rawradius = r;
    type =1;
  }
     public int getScore() {
       return 20;
     }
     
     public int reset() {
       rx = 0.0;
       ry = 0.0;   
       radius = radius * 0.67;
       // TO DO: assign a random speed 
       vx = StdRandom.uniform(-0.02, 0.02);
       vy = StdRandom.uniform(-0.02, 0.02);
       if(radius <= rawradius * 0.25){
         radius = rawradius;
       }
       return 1;
     }
}