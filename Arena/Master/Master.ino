
/*Adeepa Rajamanthri
 * Title: Master
 * Purpose: This program will collect all the data from slave arduinos and process them through 12c communication protocols
 * Date: 11/10/2018
 */
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#define T1 12345678   
#define T2 12345678
#define T3 12345678
#define POWERUP_NUM 3

 
bool check =false;
bool in = false;
int powerupType[POWERUP_NUM]; // [p0,p1...pn]
const int ledPin =53;
const int interruptPin = 3;
uint8_t collisionBuffer[POWERUP_NUM][2]; //[tank ID, powerup type] 
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
}

void loop() 
{
   if(!digitalRead(interruptPin)) // testing
   {
    ii =1;
    cycle[ii]++;
    cycle[ii] = cycle[ii]%6; 
    Serial.println("Testing Transmission:");
   int a[] = {1,15,cycle[ii]};
   transmissionEvent(a); // For Slave 1, set duration to be 5 seconds for speed powerup
   }
   
  for(int jj=1;jj<3;jj++)
  //if(0)
  {
      Wire.requestFrom(jj,7);
      receiving();
      // insert code for transmit data to IDE
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

 }

 void tankIdentify(String str)
 {
    int tankId = 0;
    if str== T1;
    {
       tankId = 1;
    }
    if str== T2;
    {
       tankId = 2;
    }
    if str== T3;
    {
       tankId = 3;
    }
 }
  
  void receiveEvent()
  {
    int powerup_info[2]; // Name,Duration
    while (0 < Wire.available())
     {
          ii = Wire.read();// Slave Number
          powerup_info[1]=Wire.read();// Duration for power up
          transmissionEvent(powerup_info); //
     }
  }
  void transmissionEvent(int trans[0])
  {
      Wire.beginTransmission(trans[0]); // powerup number
      Wire.write(trans[1]); // the duration
      Wire.write(trans[2]); // powerupType
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
