/*Adeepa rajamanthri
   Title = Slave2
   Purpose: to read a card using RFID technology by utalising a PN532 board. It will send the data to a master for calculation
            of the boosts a certain tank receives by going over the board. This code will also contain the neccesery steps for
            the lighting of an Adafruit light cicuit which will indicate when a tank drives on top of the board.
  Date last chnaged: 11/10/18
*/


/*When the number after #if set as 1, it will be switch to SPI Mode
  The following code is for the declaration of the PN532 board
*/
#define SLAVE_NUM 1

#if 1
#include <SPI.h>
#include <PN532_SPI.h>
#include "PN532.h"

PN532_SPI pn532spi(SPI, 10);
PN532 nfc(pn532spi);

/* When the number after #elif set as 1, it will be switch to HSU Mode*/
#elif 0
#include <PN532_HSU.h>
#include <PN532.h>

PN532_HSU pn532hsu(Serial1);
PN532 nfc(pn532hsu);

/* When the number after #if & #elif set as 0, it will be switch to I2C Mode*/
#else
#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_I2C pn532i2c(Wire);
PN532 nfc(pn532i2c);
#endif

/*The following code is for the light ring*/
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
#include <Wire.h>
#define LED_PIN 6 /*the light ring signal cable is at pin 6*/
#define powerUpCol strip.Color(100, 0, 0) /* this sets the resting colour of the lights*/
Adafruit_NeoPixel strip = Adafruit_NeoPixel(16, LED_PIN, NEO_GRB);



int start_time;
int duration;
uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 }, uidLength, i; // Buffer to store the returned UID of the card
int toggle = 5; //The toggeling pin from the master to indicate when card is found*****************************
int rst = 2; //Forcefully reset the Powerup Arduino
boolean activated = false;
// global Variables

void setup() {
  pinMode(toggle, OUTPUT);//setting the bit for toggleing as output
  pinMode(rst, OUTPUT);
  Serial.begin(115200);//sets the baud rate

  nfc.begin();
  uint32_t versiondata = nfc.getFirmwareVersion();//storing board details
  if (! versiondata) //checking if a board is found
  {
    Serial.print("Didn't find PN53x board");
    while (1); // halt
  }
  // Got ok data, print it out!
  Serial.print("Found chip PN5"); Serial.println((versiondata >> 24) & 0xFF, HEX);
  Serial.print("Firmware ver. "); Serial.print((versiondata >> 16) & 0xFF, DEC);
  Serial.print('.'); Serial.println((versiondata >> 8) & 0xFF, DEC);
  // Set the max number of retry attempts to read from a card
  // This prevents us from waiting forever for a card, which is
  // the default behaviour of the PN532.
  nfc.setPassiveActivationRetries(0xFF); \
  // configure board to read RFID tags
  nfc.SAMConfig();
  Serial.println("Waiting for an ISO14443A card");

  //The 2 following codes are for the intializing of the light strip
  strip.begin(); // this innitilises the light for the powerUp
  pinMode(2, INPUT_PULLUP);

  Wire.begin(SLAVE_NUM);//Wire Identifier for transfering of data*****************************************
  //register event
  Wire.onRequest(requestEvent);//Send buffered data if any
  Wire.onReceive(receiveEvent);// Master sending Powerup information

  start_time = millis(); // Marks the current time in seconds
  duration = 5000; // get the duration in Seconds

}

void loop()
{
  if(  millis() - start_time < duration) // Hence the Powerup is ON
 
  {
    LED_ON(); // Standard for without activation

     boolean success = false;
  // Wait for an ISO14443A type cards (Mifare, etc.).  When one is found
  // 'uid' will be populated with the UID, and uidLength will indicate
  // if the uid is 4 bytes (Mifare Classic) or 7 bytes (Mifare Ultralight)
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, &uid[0], &uidLength);
  
  Serial.println(success);
    if (success)
    {
      digitalWrite(rst, HIGH);
      activated = true;

      printBuffer(); // Function call for printing buffer value
      LED_ACTIVATED(); // Function call for set LEDs to activated protocol
    }
    else
    {
      //Serial.println("Timed out waiting for a card");
      //digitalWrite(toggle, LOW);
    }

  }
  else
  {
    LED_OFF();
  }

}


/*Name: CHaitany Goyal
  Purpose: This function set the colour of the set ring to "ON"
  Inputs: nil
   Outputs: nil */
void LED_ON()
{
  setRing(powerUpCol); // send it to the function setring
}

/*Name: Chaitany Goyal
  Purpose: This function set the colour of the set ring to "Activated"
  Inputs: nil
   Outputs: nil */
void LED_ACTIVATED()
{
  //light ring Code for on contact
  setRing(powerUpCol);
  setRing(strip.Color(0, 0, 255));

  ringBlink(powerUpCol, 50, 10); // fast flashes for activation
  setRing(strip.Color(255, 255, 230));
  setRing(strip.Color(0, 0, 0));

  colorWipe(powerUpCol, 100); // this sets the reset time
  ringBlink(powerUpCol, 500, 1); // slow flashes for ready
  digitalWrite(rst, LOW);
}

/*Name: Chaitany Goyal
  Purpose: This function set the colour of the set ring to "OFF"
  Inputs: nil
   Outputs: nil */
void LED_OFF()
{
  setRing(strip.Color(0, 0, 0));
}


/*Name:
  Purpose: This function set the wiping function of the 16 LED lights
  Inputs: The colour of the LED as a 32bit int and the wait time as a 16bit int
   Outputs: None
*/
void colorWipe(uint32_t c, uint16_t wait)
{
  for (uint16_t i = 0; i < 16; i++)
  {
    delay(wait);
    strip.setPixelColor(i, c);
    strip.show();
  }
}


/*Name: 
  Purpose: This function set the colour of the set ring (turning them off)
  Inputs: The colour of the LED as a 32bit int
   Outputs: None
*/
void setRing(uint32_t c)
{
  for (int i = 0; i < 16; i++)
  {
    strip.setPixelColor(i, c);
  }
  strip.show();
}

/*Name:
  Purpose: This function set blink time
  Inputs: The colour of the LED as a 32bit int, rate of the blinking as a 16bit int and the nom of times as an int
   Outputs: None
*/
void ringBlink(uint32_t c, uint16_t rate, int times)
{
  for (int i = 0; i < times; i++)
  {
    setRing(c);
    delay(rate);
    setRing(strip.Color(255, 255, 255));
    delay(rate);
  }
}
/*Name: Adeepa Rajamanthri
  Purpose: This function Writes the ID tags on to the wire to be sent to the master
  Inputs: It will validate on request when the request is recieved from the master
   Outputs: Write to wire
*/
void requestEvent()
{
  if (activated)
  {
    Wire.write(uid[0]);              // sends one byte at a time
    Wire.write(uid[1]);
    Wire.write(uid[2]);
    Wire.write(uid[3]);
    Wire.write(uid[4]);
    Wire.write(uid[5]);
    Wire.write(uid[6]);
    //delay(1500);
    activated = false;
  }
}

/*Name: Chaitany Goyal
  Purpose: This function turns powerup "ON"
  Inputs: It will validate on receiving data from master
   Outputs: nil, only sets global variables correct timings
*/
void receiveEvent()
{
  while (0 < Wire.available())
  {
    start_time = millis() * 1000; // Marks the current time in seconds
    duration = Wire.read() * 1000; // get the duration in Seconds
    Serial.println("The starting Time and Duration in seconds is:");
    Serial.println(start_time);
    Serial.println(duration);
  }
}

void printBuffer()
{
  //The card details now get printed to serial including its length and values in uid
  Serial.println("Found a card!");
  Serial.print("UID Length: "); Serial.print(uidLength, DEC); Serial.println(" bytes");
  Serial.print("UID Value: ");
  //calculating the UID
  for (uint8_t i = 0; i < uidLength; i++)
  {
    Serial.print(" 0x"); Serial.print(uid[i], HEX);
  }
}
void readBuffer()
{
 
  
}
