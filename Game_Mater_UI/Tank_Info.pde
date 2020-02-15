/*
This section contains the relevent code neccesary for the running of the background 

Names:  Adeepa Rajamanthri, Anton R
Date of final change:  29/09/19
*/

class Tank {
  int health, score;
}

void arduino_serial_setup()
{
    MasterArduino = new Serial(this, "COM6", 115000); //the serial will connect to com port connected to the master  
    println(MasterArduino);
}

void Read_arduino_serial()
{
    if(MasterArduino.available() > 0 && start_mode == true)
  {
    in_tank = (MasterArduino.readStringUntil(space));
    in_powerup =(MasterArduino.readStringUntil(nl));
    println(in_tank,in_powerup);
  }
}
