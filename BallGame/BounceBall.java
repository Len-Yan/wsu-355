import java.awt.*;

public class BounceBall extends BasicBall{ 
  private int bounce;
  
  public BounceBall(double r, Color c) {
    super(r,c);
    type = 2;
    bounce = 3;
  }
  
  // move the ball with bounce
  public void move() {
    rx = rx + vx;
    ry = ry + vy;
    //System.out.println(bounce);
    if (bounce >= 0){
      if (Math.abs(ry) >= 1.0){vy = vy*-1; bounce--;}
      if (Math.abs(rx) >= 1.0){vx = vx*-1; bounce--;}
    }
    else {
      if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) {isOut = true;}
    }
  }
  
  // add bounce var
  public void draw() { 
    if (bounce >= 0 || ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0))) {
      StdDraw.setPenColor(color);
      StdDraw.filledCircle(rx, ry, radius);
    } else   isOut = true;
  }
  
  //add reset bounce # after hit
  public int reset() {
    bounce = 3;
    rx = 0.0;
    ry = 0.0;   
    // TO DO: assign a random speed 
    vx = StdRandom.uniform(-(speed), speed);
    vy = StdRandom.uniform(-(speed), speed);
    
    return 1;
  }
  
  public int getScore() {
    return 15;
  }
}