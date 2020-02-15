


void custamizes(Slider s,String name,float xpos, float ypos,int lent,int heit)
{
  s.setPosition(xpos,ypos);
  s.setWidth(lent);
  s.setHeight(heit);
  s.setRange(0,30); // values can range from big to small as well
  s.setValue(15);
  s.setNumberOfTickMarks(15);
  s.setSliderMode(Slider.LINE);
  s.setBroadcast(true);
  s.setHandleSize(20);
  s.setDecimalPrecision(0);
  slider.getController(name).getCaptionLabel().hide();//align(ControlP5.RIGHT, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0);
}

void create_slider(Slider s,String setname,PFont font,int xpos,int ypos)
{
  
    for (int i=0;i<4;i++) 
  {
    s = slider.addSlider(setname+i);
    //addScrollableList(setname+i,xpos,ypos-i*60,220,250);
    custamizes(s,setname+i,xpos,ypos-i*60,175,30);
    s.setId(i);
    s.setFont(createFont("arial",25));
    slider.getController(name).getCaptionLabel().hide();
    //s.setCaptionLabel("Rank"+(4-i));
  }
}
void controlslider(ControlP5 ws,String setname, int items,boolean rt)
{
  for(int i=0;i<items;i++)
  {
    if(rt == true)
    {
      ws.get(Slider.class, setname+i).hide();
    }
    if(rt == false)
    {
      ws.get(Slider.class, setname+i).show();
    }
  }
  
}
