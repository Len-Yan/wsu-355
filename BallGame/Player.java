public class Player{
  private int hits;
  private int score;
  private int[] typehit = {0,0,0,0};
  private int[] ballscore = {25,20,15,10};
  private String[] balltype = {"basic","shrink","bounce","split"};
  
//cons
  public Player(){
    hits = 0;
    score = 0;
  }
  
  public int getscore(){
    return score;
  }
  public int gethits(){
    return hits;
  }
  
  //pass the type index, update base on type index
  public void hitball(int x){
    score += ballscore[x];
    hits++;
    typehit[x]++;
  }
  
  //return most hit ball type
  public String mosthit(){
    int most = 0;          //track type index
    int temp = typehit[0];
    for(int i = 0; i < typehit.length; i++ ){
      if(typehit[i] > temp){
        temp = typehit[i];
        most = i;      // update to mosthit type index
      }
    }
    return balltype[most];

  }
  
}