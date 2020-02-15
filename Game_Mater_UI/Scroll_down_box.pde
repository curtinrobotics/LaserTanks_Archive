/*
This section contains the relevent code neccesary for Drop Down Boxes and all control events from CP5

Names:  Adeepa Rajamanthri
Date of final change:  29/09/19
*/

void customizeddl(ScrollableList ddl, List l, PFont font,int barheight, int itemheight) 
{
  ddl.setItemHeight(itemheight);
  ddl.setBarHeight(barheight);
  ddl.addItems(l);
  ddl.setColorBackground(color(60));
  ddl.setColorActive(color(255,128));
  ddl.setFont(font);
  ddl.close();
  ddl.hide();
}

void create_powerup(ScrollableList ddl,String setname, List l,PFont font,int xpos,int ypos)
{ 
  for (int i=0;i<4;i++) 
  {
    ddl = Scroll.addScrollableList(setname+i,xpos,ypos-i*65,220,250);
    customizeddl(ddl,l,font,50,40);
    ddl.setId(i);
    ddl.setCaptionLabel("Rank"+(4-i));
    //ddl.setValue(0);
  }
    
}

void controlddl(ControlP5 ws,String setname, int items,boolean rt)
{
  
  for(int i=0;i<items;i++)
  {
    if(rt == true)
    {
      ws.get(ScrollableList.class, setname+i).hide();
    }
    if(rt == false)
    {
      ws.get(ScrollableList.class, setname+i).show();
    }
  }
  
}

void printddl(ControlP5 scrolldown,ControlP5 slider,String setnameddl,String setnameslider, int items)
{
  //print(ws);
  MasterArduino.write("255"); 
  int t = items;
  for(int i=items-1;i>-1;i--)
  {
    MasterArduino.write("  "); 
    print("  ");
    print(int(scrolldown.get(ScrollableList.class, setnameddl+i).getValue()+1));
    MasterArduino.write(int(scrolldown.get(ScrollableList.class, setnameddl+i).getValue()+1)); 
    MasterArduino.write(" "); 
    print(" ");
    print(int(slider.get(Slider.class, setnameslider+i).getValue()));
    MasterArduino.write(int(slider.get(Slider.class, setnameslider+i).getValue())); 
  }
  //println();
}



void keyPressed() {
  switch(key) {
    //case('1'):
    
    //break;
    //case('2'):
    
    //break;
    //case('3'):
    
    //break;
    //case('4'):
    
    //break;
    //case('5'):
    
    //break;
  }
}

void controlEvent(ControlEvent theEvent) 
{
  if (theEvent.isGroup()) 
  {
    // check if the Event was triggered from a ControlGroup
    println("event from group : "+theEvent.getGroup().getValue()+" from "+theEvent.getGroup());
  } 
   if (theEvent.isController()) 
  {
    println("event from controller : "+theEvent.getController().getValue()+" from "+theEvent.getController());
    name = theEvent.getController().getName();
    if(name.equals("Number of Players"))
    {
      it = theEvent.getController().getValue(); //<>//
      people = int(it);
    }  
  }
  if(theEvent.isAssignableFrom(Textfield.class)) 
  {
    if (theEvent.getName().equals("Player 1"))
    {
      player_name1 = theEvent.getStringValue();
    }
        if (theEvent.getName().equals("Player 2"))
    {
      player_name2 = theEvent.getStringValue();
    }
        if (theEvent.getName().equals("Player 3"))
    {
      player_name3 = theEvent.getStringValue();
    }
        if (theEvent.getName().equals("Player 4"))
    {
      player_name4 = theEvent.getStringValue();
    }
  }
}
