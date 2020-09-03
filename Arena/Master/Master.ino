
/*Adeepa Rajamanthri
 * Title: Master
 * Purpose: This program will collect all the data from slave arduinos and process them through 12c communication protocols
 * Date: 11/10/2018
 */
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#define T1   
#define T2
#define T3 

bool check =false;
bool in = false;
int i = 1;
const int ledPin =53;
const int interruptPin = 3;
uint8_t tankID[7];
//
LiquidCrystal_I2C lcd(0x27,16,2);  
void setup() 
{
  Wire.begin();
  Wire.onReceive(receiveEvent); // from GUI to master
  lcd.backlight();
  lcd.init();  
  Serial.begin(115200);//set baud rate
  Serial.println("Serial Start");
  pinMode(ledPin, OUTPUT);
  pinMode(13, OUTPUT);
  
 pinMode(interruptPin, INPUT_PULLUP);// for TESTING PURPOSE
 //attachInterrupt(digitalPinToInterrupt(interruptPin),testSlave,FALLING);

//  testSlave();
}

void loop() 
{
   if(!digitalRead(interruptPin))
   {
    Serial.println("Yeh");
   int a[] = {1,5};
   transmissionEvent(a); // For Slave 1, set duration to be 5 seconds for speed powerup
   }
   
  // for(i=1;i<3;i++)
  if(0)
  {
    in = Wire.requestFrom(i,sizeof(tankID));
    if(in)
    {
      Serial.print("From Powerup number:  ");
      Serial.println(i);
      receiving();
      // insert code for transmit data to IDE
    }
  }
  //printloop(); not sure what this does so ill leave it in

  
}

void printHex(unsigned int numberToPrint)
{
  if (numberToPrint >= 16)
    printHex(numberToPrint / 16);
  Serial.println("0123456789ABCDEF"[numberToPrint % 16]);
  //return 
  
}

/*Adeepa Rajamanthri
 * Name: receiving
 * Purpose: Sets the data to zero and read in the 8 bits from the respective wire
 */
void receiving()
{ 
  String str = "";
  delay(5);
  
  while (Wire.available()>5)
  {
    // loop through all but the last
    for (int ii=0; ii < sizeof(tankID); ii++)
    {
      tankID[ii] = Wire.read(); // receive byte as a character
      str += tankID[ii]; // store ID as a string
    }
    
    if(str != "0255255255255255255") // if ID not invalid 
    {
      Serial.println(str);
    }
  }
 }
  
  void receiveEvent()
  {
    int powerup_info[2]; // Name,Duration
    while (0 < Wire.available())
     {
          powerup_info[0]=Wire.read();// Slave Number
          powerup_info[1]=Wire.read();// Duration for power up
          transmissionEvent(powerup_info); //
     }
  }
  void transmissionEvent(int trans[0 ])
  {
      Wire.beginTransmission(1); // powerup number
      Wire.write(trans[1]); // the duration
      Wire.endTransmission(1);
      Serial.println("Sent val");
  }

 /* void testSlave()
  {
   //if(digitalRead(9)); // TESTING PURPOSE
   //{
   Serial.println("Yeh");
   int a[] = {1,5};
   transmissionEvent(a); // For Slave 1, set duration to be 5 seconds for speed powerup
  
  }*/
