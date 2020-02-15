/*
Name: Textfield.h
author: Adeepa Rajamanthri
Date of last change: 9/09/19
Description
The code nessasary to custamise the textfield
*/

void customizetx(Textfield tf,PFont font,String name)
{

  tf.setColorBackground(color(60));
  tf.setColorActive(color(255,128));
  tf.setFont(font);
  tf.setSize(380,40);
  tf.setAutoClear(false);
  tf.hide();
  textin.getController(name).getCaptionLabel().align(ControlP5.CENTER, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0);
}

void setup_text()
{
  textshow = new ControlP5(this);
  player_1 =textshow.addTextlabel("p1");
  player_2 =textshow.addTextlabel("p2");
  player_3 =textshow.addTextlabel("p3");
  player_4 =textshow.addTextlabel("p4");

}

void customizetext(Textlabel tb ,String in, PFont fonttl, int CV, int xpos, int ypos)
{
  tb.setColorBackground(color(60));
  tb.setText(in);
  tb.setColorValue(CV);
  tb.setFont(fonttl);
  tb.setPosition(xpos,ypos);
  tb.show();
}

void setup_robot()
{
   try { 
    robot = new Robot();
  } catch (AWTException e) {
    e.printStackTrace();
    exit();
  } 
}

void Keyboard(int ent)
{
   robot.keyPress(ent);
  //If we want a delay here, that gets a little bit more complicated...
  robot.keyRelease(ent);
}
