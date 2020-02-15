/*Adeepa rajamanthri
 * Title = Slave2
 * Purpose: to read a card using RFID technology by utalising a PN532 board. It will send the data to a master for calculation
 *          of the boosts a certain tank receives by going over the board. This code will also contain the neccesery steps for 
 *          the lighting of an Adafruit light cicuit which will indicate when a tank drives on top of the board.
 *Date last chnaged: 11/10/18
 */


/*When the number after #if set as 1, it will be switch to SPI Mode
 *The following code is for the declaration of the PN532 board  
 */
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
#define PIN 6 /*the light ring signal cable is at pin 6*/

Adafruit_NeoPixel strip = Adafruit_NeoPixel(16, PIN, NEO_GRB);

uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID of the card
int toggle = 5; //The toggeling pin from the master to indicate when card is found*****************************
byte x = 0;

boolean set = false;

void setup() {
	pinMode(toggle, OUTPUT);//setting the bit for toggleing as output
	Serial.begin(115200);//sets the baud rate
	Serial.println("Hello!");
	nfc.begin(); 
	Wire.onRequest(requestEvent);//If the go ahead is given from the master, the slave will start sending the data
	
	uint32_t versiondata = nfc.getFirmwareVersion();//storing board details
	if (! versiondata) //checking if a board is found
	{
		Serial.print("Didn't find PN53x board");
		while (1); // halt
	}
	// Got ok data, print it out!
	Serial.print("Found chip PN5"); Serial.println((versiondata>>24) & 0xFF, HEX); 
	Serial.print("Firmware ver. "); Serial.print((versiondata>>16) & 0xFF, DEC); 
	Serial.print('.'); Serial.println((versiondata>>8) & 0xFF, DEC);
	
	// Set the max number of retry attempts to read from a card
	// This prevents us from waiting forever for a card, which is
	// the default behaviour of the PN532.
	nfc.setPassiveActivationRetries(0xFF);\
	
	// configure board to read RFID tags
	nfc.SAMConfig();
	
	Serial.println("Waiting for an ISO14443A card");
	//The 2 following codes are for the intializing of the light strip 
	strip.begin(); // this innitilises the light for the powerUp
	pinMode(2,INPUT_PULLUP);
	
	Wire.begin(1);//Wire Identifier for transfering of data*****************************************                 
	//register event
	Wire.onRequest(requestEvent);
}

void loop() {
	uint32_t powerUpCol = strip.Color(100, 0, 0); // this sets the resting colour of the lights
	setRing(powerUpCol); // send it to the function setring
	uint8_t uidLength,i;// Length of the UID (4 or 7 bytes depending on ISO14443A card type)
	boolean success = false;
	// Wait for an ISO14443A type cards (Mifare, etc.).  When one is found
	// 'uid' will be populated with the UID, and uidLength will indicate
	// if the uid is 4 bytes (Mifare Classic) or 7 bytes (Mifare Ultralight)
	success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, &uid[0], &uidLength);
	Serial.println(success);
	if (success) 
	{
		set =true;
		Serial.println("in");
		//The card details now get printed to serial including its length and values in uid
		Serial.println("Found a card!");
		Serial.print("UID Length: ");Serial.print(uidLength, DEC);Serial.println(" bytes");
		Serial.print("UID Value: ");
		//calculating the UID
		
		for (uint8_t i=0; i < uidLength; i++) 
		{
			Serial.print(" 0x");Serial.print(uid[i], HEX); 
		}
		Serial.println("");
		Serial.println("in1");
		Serial.println("in2");
		
		//light ring Code for on contact
		uint32_t powerUpCol = strip.Color(255, 0, 0); // this sets the resting colour of the lights
		setRing(powerUpCol);
		setRing(strip.Color(0, 0, 255));
		//Send powerup notification to Game Master
		Serial.println("after");
		ringBlink(powerUpCol, 50, 10); // fast flashes for activation
		setRing(strip.Color(255, 255, 230));
		//delay(1000);
		setRing(strip.Color(0, 0, 0));
		colorWipe(powerUpCol, 100); // this sets the reset time
		ringBlink(powerUpCol, 500, 1); // slow flashes for ready
		//Wire.onRequest(waiting);
	}
	else
	{
		// PN532 probably timed out waiting for a card
		Serial.println("Timed out waiting for a card");
		//Wire.onRequest(waiting);
		//digitalWrite(toggle, LOW);
	}
}
/*Name:
 *Purpose: This function set the wiping function of the 16 LED lights  
 *Inputs: The colour of the LED as a 32bit int and the wait time as a 16bit int
 * Outputs: None
 */
void colorWipe(uint32_t c, uint16_t wait) 
{
	for(uint16_t i=0; i<16; i++) 
	{
		delay(wait);
		strip.setPixelColor(i, c);
		strip.show();
	}
}

/*Name:
 *Purpose: This function set the colour of the set ring (turning them off)
 *Inputs: The colour of the LED as a 32bit int 
 * Outputs: None
 */
void setRing(uint32_t c) 
{
	for(int i=0;i<16;i++)
	{
		strip.setPixelColor(i, c); 
	}
	strip.show();
}

/*Name:
 *Purpose: This function set blink time 
 *Inputs: The colour of the LED as a 32bit int, rate of the blinking as a 16bit int and the nom of times as an int
 * Outputs: None
 */
void ringBlink(uint32_t c, uint16_t rate, int times) 
{
	for(int i=0; i < times; i++) 
	{
		setRing(c);
		delay(rate);
		setRing(strip.Color(255, 255, 255));
		delay(rate);
	}
}
/*Name: Adeepa Rajamanthri
 *Purpose: This function Writes the ID tags on to the wire to be sent to the master
 *Inputs: It will validate on request when the request is recieved from the master
 * Outputs: Write to wire
 */
void requestEvent() 
{
	if (set)
	{
		//Wire.beginTransmission(1); // transmit to device #8 
		Wire.write(uid[0]);              // sends one byte
		Wire.write(uid[1]);
		Wire.write(uid[2]);
		Wire.write(uid[3]);
		Wire.write(uid[4]);
		Wire.write(uid[5]);
		Wire.write(uid[6]);
		//delay(1500);
		set = false;
	}
	//waiting();
}
/*Name: Adeepa Rajamanthri
 *Purpose: This function Write the ID tags on to the wire to be sent to the master
 *Inputs: It will validate on request when the request is recieved from the master
 * Outputs: Write to wire
 */
void waiting() 
{
	//Wire.beginTransmission(1); // transmit to device #8 
	Wire.write("0");              // sends one byte
	Wire.write("0");            // sends one byte
	Wire.write("0");  
	Wire.write("0");  
	Wire.write("0");  
	Wire.write("0");  
	Wire.write("0");  

	
	//Wire.endTransmission();    // stop transmitting
}
