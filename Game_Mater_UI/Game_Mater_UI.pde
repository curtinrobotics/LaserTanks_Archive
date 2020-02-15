/*
 * 29/08/18
 * Anton R
 * Laser Tanks rough UI mockup

 *13/09/19
 *Adeepa Rajamanthri
 *Laser Tanks Addition into main hub
 *Revision 2
 */






public void settings() 
{
  fullScreen();
  //size(900,900);
  //MasterArduino = new Serial(this, "COM15", 115000);
  arduino_serial_setup();
  
}
 

void draw() 
{
  MasterArduino.write("1");
  Read_arduino_serial();
  background();
}
