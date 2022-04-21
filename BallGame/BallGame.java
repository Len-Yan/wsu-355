/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.*; 

public class BallGame { 

    public static void main(String[] args) {
  
     // number of bouncing balls
     int numBalls = Integer.parseInt(args[0]);
     //ball types
     String ballTypes[] = new String[numBalls];
     //sizes of balls
     double ballSizes[] = new double[numBalls];
     
     //retrieve ball types
     int index =1;
     for (int i=0; i<numBalls; i++) {
      ballTypes[i] = args[index];
      index = index+2;
     }
     //retrieve ball sizes
     index = 2;
     for (int i=0; i<numBalls; i++) {
      ballSizes[i] = Double.parseDouble(args[index]);
      index = index+2;
     }
     
     //TO DO: create a Player object and initialize the player game stats.  
     Player p = new Player();
     
     
     //number of active balls
     int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        //
        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" 
        //with sizes given in "ballSizes") and store them in an Arraylist
        
        ArrayList<BasicBall> balls = new ArrayList<BasicBall>();
        //BasicBall ball = new BasicBall(ballSizes[0],Color.RED);;
        for(int i = 0; i<numBalls; i++){ // make x ball
          numBallsinGame++;
          BasicBall ball;
          if(ballTypes[i].equals("basic")){
            ball = new BasicBall(ballSizes[i],Color.RED);
            balls.add(ball);
          }
          else if(ballTypes[i].equals("shrink")){
            ball = new ShrinkBall(ballSizes[i],Color.cyan);
            balls.add(ball);
          }
          else if(ballTypes[i].equals("bounce")){
            ball = new BounceBall(ballSizes[i],Color.yellow);
            balls.add(ball);
          }
          else if (ballTypes[i].equals("split")){
            ball = new SplitBall(ballSizes[i],Color.orange);
            balls.add(ball);
          }
          else{System.out.println("ball type error");numBallsinGame--;}
        }
         
     //TO DO: initialize the numBallsinGame 
     //numBallsinGame++;
        Iterator<BasicBall> it = balls.iterator();
        //BasicBall ball;
          
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        BasicBall ball;
        //numBallsinGame++;
        
        
        Boolean splitfalg = false;
        double tempr = 0;
        while (numBallsinGame > 0) {

         // TODO: move all balls
          //balls.forEach((b) -> b.move());
          for(int i = 0; i< balls.size(); i++){
           balls.get(i).move(); 
          }
            //ball.move();

            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.  
                
                it = balls.iterator();
                while(it.hasNext()){
                  ball = it.next();
                  
                  if (ball.isHit(x,y)) {
                    ball.reset();
                    //TO DO: Update player statistics
                    int t = ball.gettype();
                    //System.out.println(t);
                    if(t == 3){
                      //make another SPball
                      splitfalg = true;
                      tempr = ball.getRadius();
                    }
                    p.hitball(t);
                    
                  }
                }
            }
            
            if(splitfalg == true){
              splitfalg = false;
              BasicBall a = new SplitBall(tempr,Color.orange);
              balls.add(a);numBallsinGame++;
            }
            
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game.  
           
            it = balls.iterator();
            while(it.hasNext()){
              ball = it.next();
                if (ball.isOut == false) { 
                ball.draw();
                numBallsinGame++;
              }
            }
            
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            //TO DO: print the rest of the player statistics
            StdDraw.text(-0.65, 0.84, "Player Score: " + String.valueOf(p.getscore()));
            StdDraw.text(-0.65, 0.78, "Player hits: " + String.valueOf(p.gethits()));
            StdDraw.text(-0.65, 0.72, "Most hits ball: " + String.valueOf(p.mosthit()));
            
            StdDraw.show();
            StdDraw.pause(20);
        }//while loop end
        
        
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            
            
            StdDraw.show();
            StdDraw.pause(10);           
        }
         
        
    }
}
