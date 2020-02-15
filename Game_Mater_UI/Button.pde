/*
This section contains the relevent code neccesary for Button

Names:   Anton R
Date of final change:  29/08/18
*/
class Button {
  int xpos, ypos, bWidth, bHeight;
  color bCol;
  float size;
  String bTitle;
  boolean wasPressed = false;
  Button(int x, int y, int w, int h, color c, String t,float s) {
    xpos = x;
    ypos = y;
    bWidth = w;
    bHeight = h;
    bCol = c;
    bTitle = t;
    size=s;
  }
  
  // checks if button is being pressed
  boolean pressed() {
    if (mousePressed && mouseButton == LEFT &&
    mouseX >= xpos && mouseX <= xpos + bWidth &&
    mouseY >= ypos && mouseY <= ypos + bHeight) {
      wasPressed = true;
      return true;
    }
    return false;
  }
  
  // checks if button has been released
  boolean released() {
    if (!mousePressed && wasPressed) {
      wasPressed = false;
      return true;
    }
    return false;
  }
  
  // draw the button
  void draw() {
    fill(bCol);
    stroke(0);
    rect(xpos, ypos, bWidth, bHeight);
    
    textSize(size);    
    fill(#000000);
    
    text(bTitle, xpos + (bWidth - textWidth(bTitle)) / 2,
    ypos + (bHeight + textAscent() - textDescent()) / 2,200);
    // indicate button press by making it darker
    if (pressed()) {
      fill(0, 100);
      rect(xpos, ypos, bWidth, bHeight);
    }
 }
}

void playerenter()
{
  if(p1enter.released())
  {
    //Keyboard((KeyEvent.VK_ENTER));
    player_name1= textin.get(Textfield.class,"Player 1").getText();
    nameof_player = player_name1.length();
    if(nameof_player >12)
    {
       win = new PWindow();
    }
    else
    {
      customizetext(player_1 ,player_name1, createFont("Georgia",60),0x000000,350,350);
    }
  }
  if(p2enter.released())
  {
    //Keyboard((KeyEvent.VK_ENTER));
    player_name2 = textin.get(Textfield.class,"Player 2").getText();
    customizetext(player_2 ,player_name2, createFont("Georgia",60),0x000000,750,350);
  }
  if(p3enter.released())
  {
    //Keyboard((KeyEvent.VK_ENTER));
    player_name3 = textin.get(Textfield.class,"Player 3").getText();
    customizetext(player_3 ,player_name3, createFont("Georgia",60),0x000000,1150,350);
  }
  if(p4enter.released())
  {
    //Keyboard((KeyEvent.VK_ENTER));
    player_name4 = textin.get(Textfield.class,"Player 4").getText();
    customizetext(player_4 ,player_name4, createFont("Georgia",60),0x000000,1550,350);
  }
}
//void keyPressed() {
//  //Detect space key presses (to show that it works)
//  if(key == ENTER) {
//    println("Space!");

//  }
//}
