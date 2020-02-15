/*
This section contains the relevent code neccesary for the running of the background 

Names:  Adeepa Rajamanthri, Anton R
Date of final change:  29/09/19
*/


PWindow win;
PApplet qw;
  

/*********************************************************************************************************************
Setup
**********************************************************************************************************************/
void setup()
{
   setup_robot();
/*
Contains the code to setup the scroll down box
*/
  noStroke();
  PFont fontddl1 = createFont("arial",25);
  Scroll = new ControlP5(this);
  NOP = Scroll.addScrollableList("Number of Players",10,((height-200)/2)-300/2,300,400);
  List Nom_o_p = Arrays.asList("2 Players", "3 Players", "4 Players");
  customizeddl(NOP,Nom_o_p,fontddl1,50,70);
  
  Scroll = new ControlP5(this);
  List power_list = Arrays.asList("Health Boost", "Rapid Fire", "Boost");
  create_powerup(p1l1,"P1L1",power_list,fontddl1,50,int(((height+200)/2+200)-310/2+180));
  create_powerup(p1l1,"P1L2",power_list,fontddl1,520,int(((height+200)/2+200)-310/2+180));
  create_powerup(p1l1,"P1L3",power_list,fontddl1,1000,int(((height+200)/2+200)-310/2+180));
  create_powerup(p1l1,"P1L4",power_list,fontddl1,1490,int(((height+200)/2+200)-310/2+180));
  /*
contains the code to setup the sliders
*/
  slider = new ControlP5(this);
  create_slider(time1,"P1S1",fontddl1, 50+250,int(((height+200)/2+200)-310/2+180)+10);
  create_slider(time1,"P1S2",fontddl1, 520+250,int(((height+200)/2+200)-310/2+180)+10);
  create_slider(time1,"P1S3",fontddl1, 1000+250,int(((height+200)/2+200)-310/2+180)+10);
  create_slider(time1,"P1S4",fontddl1, 1490+250,int(((height+200)/2+200)-310/2+180)+10);
/*
contains the code to setup the text boxes
*/
  PFont fonttt1 = createFont("arial",20);
  textin = new ControlP5(this);
  player1 = textin.addTextfield("Player 1",  320+10, 200+10,400-50,20);
  customizetx(player1,fonttt1,"Player 1") ;
  player2  =  textin.addTextfield("Player 2", 720+10, 200+10, 400-10,20);
  customizetx(player2,fonttt1,"Player 2") ;
  player3  =  textin.addTextfield("Player 3", 1120+10, 200+10, 400-10,20);
  customizetx(player3,fonttt1,"Player 3") ;
  player4  =  textin.addTextfield("Player 4", 1520+10, 200+10, 400-10,20);
  customizetx(player4,fonttt1,"Player 4") ;
  
  setup_text();
  Croc_logo = loadImage("croc1.png");
  
 

}


void printa (float r)
{
  if(name.equals("Number of Players"))
  {
    println("Number of Players  "+r);
  }
   if(name.equals("number of powerups"))
  {
    println("number of powerups  "+r);
  }
}
/*********************************************************************************************************************
Final Background
**********************************************************************************************************************/

void background()
{    //player_1.draw(this);

  CP5 = new ControlP5(this);
  choice_background();

    //printa(it);
  if(next2_button == 1)
  {
    input =NOP.getId() ;
    NOP.show();
    choice_freeforall();
  }
  if(next1_button == 1)
  {
    game_background();
    back_tff.draw();
  }  
    if(back_tff.released())
  {
      next2_button = 1;
      next1_button = 0;
      player_1.hide();
      player_2.hide();
      player_3.hide();
      player_4.hide();
  }  
  pop_up++;
}

/*********************************************************************************************************************
mode selction page
**********************************************************************************************************************/
void choice_background()
{
  background(#B6B7A6);
  fill(0x0);
  fill(238,130,88);
  rect(0,0,width,200);
  tofreeforall.draw();
  if (tofreeforall.released())
  {
      next2_button = 1;
      next1_button = 0;
     
  }
  image(Croc_logo, width/2-1091/2, (141/4));
  
  controlddl(Scroll,"P1L1",4,true);
  controlddl(Scroll,"P1L2",4,true);
  controlddl(Scroll,"P1L3",4,true);
  controlddl(Scroll,"P1L4",4,true);
  controlslider(slider,"P1S1", 4,true);
  controlslider(slider,"P1S2", 4,true);
  controlslider(slider,"P1S3", 4,true);
  controlslider(slider,"P1S4", 4,true);
}
/*********************************************************************************************************************
Free for all selction page
**********************************************************************************************************************/

 void choice_freeforall()
{
  NOP.show();  
  background(#B6B7A6);
  fill(#B6B7A6 );

    
  fill(238,130,88);
  rect(0,0,width,200);
  fill(#B6B7A6 );
  rect(0,200,width,(height-200)/2);
  rect(0,200,320,(height-200)/2);
  player_select(it, 320, 200,(width-320), ((height-200)/2));
  power_select(0, height/2+100, width, (height-200)/2);
  
  togame.draw();
  if (togame.released())
  {
    next1_button = 1;
    next2_button = 0;
    print("120");
    MasterArduino.write("120");
    MasterArduino.write("1");
    //printddl(Scroll,slider,"P1L1","P1S1", 4);
    //printddl(Scroll,slider,"P1L2","P1S2", 4);
    //printddl(Scroll,slider,"P1L3","P1S3", 4);
    //printddl(Scroll,slider,"P1L4","P1S4", 4);
    //print("  ");
    //println("119");
    MasterArduino.write("119");
  }
  
  
  controlddl(Scroll,"P1L1", 4,false);
  controlddl(Scroll,"P1L2", 4,false);
  controlddl(Scroll,"P1L3", 4,false);
  controlddl(Scroll,"P1L4", 4,false);
  controlslider(slider,"P1S1", 4,false);
  controlslider(slider,"P1S2", 4,false);
  controlslider(slider,"P1S3", 4,false);
  controlslider(slider,"P1S4", 4,false);
  image(Croc_logo, width/2-1091/2, (141/4));
  drop = true;
  //print(1);
  
  
  //println();
}

/*********************************************************************************************************************
Game Background
**********************************************************************************************************************/
void game_background()
{ player1.hide();player2.hide();player3.hide();player4.hide();
  NOP.hide();
  background(0x0 );
  fill(#B6B7A6 );
  textSize(32);
  text(title, (width - textWidth(title)) / 2, 35);
  textSize(36);
  if (!timing) text("Timer:", (width - textWidth(timeStr)) / 2 - textWidth("Timer:") - 15, 90);
  text(timeStr, (width - textWidth(timeStr)) / 2, 90);
  //text(millis(), 20, 50);
  textSize(10);
  //text(mouseX + "," + mouseY, 10,10);
  noStroke();
  fill(128);
  rect(0,200,width,height);
  fill(200,50,50);
  rect(10,210,width/2 - 20, (height - 200) / 2 - 20);
  fill(50,200,50);
  rect(width/2+10, 210, width/2-20, (height-200)/2 - 20);
  fill(50,50,200);
  rect(10,(height-200)/2+210, width/2-20,(height-200)/2 - 20);
  fill(200,200,50);
  rect(width/2+10, (height-200)/2+210, width/2-20,(height-200)/2-20);
  //base plate for player one health
  fill(128,128,128);
  rect(50, 450, 500, 100);
  //base plate for player 2 health bar
  fill(128,128,128);
  rect(50, 890, 500,100);
  //base plate for player 3 health bar
  button_draw();
  customizetext(player_1 ,player_name1, createFont("Georgia",60),0x000000,50,250);
  customizetext(player_2 ,player_name2, createFont("Georgia",60),0x000000,1000,250);
  customizetext(player_3 ,player_name3, createFont("Georgia",60),0x000000,50,700);
  customizetext(player_4 ,player_name4, createFont("Georgia",60),0x000000,1000,700);
  controlddl(Scroll,"P1L1", 4,true);
  controlddl(Scroll,"P1L2", 4,true);
  controlddl(Scroll,"P1L3", 4,true);
  controlddl(Scroll,"P1L4", 4,true);
  controlslider(slider,"P1S1", 4,true);
  controlslider(slider,"P1S2", 4,true);
  controlslider(slider,"P1S3", 4,true);
  controlslider(slider,"P1S4", 4,true);
}

void button_draw()
{
  exit.draw();
  if (exit.released())
  {
     MasterArduino.write('0');         //send a 1
     exit(); 
     start_mode = false;
  }
  if (!timing) 
  {
    plusButt.draw();
    minusButt.draw();
    startButt.draw();
  } 
  else 
  {
    timer = millis() - startTime;
    if (timer >= counter) 
    {
      timing = false;
      timer = 0;
    }
  }
  
  
  if (plusButt.released()) counter += 30000;
  if (minusButt.released()) counter -= 30000;
  if (startButt.released()) 
  {
    timing = true;
    startTime = millis();
    MasterArduino.write("255");         //send a 1
    MasterArduino.write("  "); 
    println("255");   
    start_mode = true;
  }

  
  if (counter < 0) counter = 0;
  tSecs = (counter - timer)/1000;
  timeStr = int(tSecs/60) + ":" + int(((tSecs) % 60) / 10) + "" + (tSecs) % 10;
}  


void player_select(float in, float xpos, float ypos, float lnth, float heght)
{
  in +=2;
  float hold;
  hold = lnth/4;

  int col[]={#C83232,#32C832,#3232C8,#C8C832};
  for(int i=0;i<in;i++)
  {
    fill(col[i] );
    rect(xpos+i*hold,ypos,hold,heght);
  }
  if(in==2)
  {
    player1.show();player2.show();player3.hide();player4.hide();
    p1enter.draw();p2enter.draw();
    player_3.hide();player_4.hide();
  }
  if(in==3)
  {
    player1.show();player2.show();player3.show();player4.hide();
    p1enter.draw();p2enter.draw();p3enter.draw();
    player_4.hide();
  }
  else if(in==4)
  {
    player1.show();player2.show();player3.show();player4.show();
    p1enter.draw();p2enter.draw();p3enter.draw();p4enter.draw();
  }
  playerenter();
}

void power_select(float xpos, float ypos, float lnth, float heght)
{
  float hold;
  hold = lnth/4;
  for(int i=0;i<4;i++)
  {
  fill(#B6B7A6);
  rect(xpos+i*hold,ypos,hold,heght);

  }
  
}

class PWindow extends PApplet {
  PWindow() {
    super();
    PApplet.runSketch(new String[] {this.getClass().getSimpleName()}, this);
  }
 
   void settings() {
    size(500, 500);
  }
 
  void setup() {
    background(150);
  }
 
  void draw() 
  {
    text("pls enter a name with less than 12 characters", 10,10);
  }
 
  void mousePressed() {
    println("mousePressed in secondary window");
  }
  

}
