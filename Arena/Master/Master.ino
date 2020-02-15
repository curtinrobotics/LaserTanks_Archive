
/*Adeepa Rajamanthri
 * Title: Master
 * Purpose: This program will collect all the data from slave arduinos and process them through 12c communication protocols
 * Date: 11/10/2018
 */
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
bool check =false;
byte in;
int i = 1;
const int ledPin =53;

LiquidCrystal_I2C lcd(0x27,16,2);  
void setup() 
{
	Wire.begin();
	lcd.backlight();
	lcd.init();  
	Serial.begin(115200);//set baud rate
	pinMode(ledPin, OUTPUT);
}

void loop() 
{
	while(Serial.available()) 
	{
		digitalWrite(ledPin, LOW);
		lcd.setCursor(0,0);
		Serial.print("in");
	}

	
	int val = Serial.read();
	lcd.setCursor(0,1);
	lcd.print(val);
	for(i=1;i<3;i++)
	{
		//Serial.println(i);
		in = Wire.requestFrom(i, 8);
		if(in>5)
		{
			receiving();
		}
	}
	printloop();

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
	uint8_t a = 0; //b,c,d,e,f,g,h;
	uint8_t b = 0;
	uint8_t c = 0;
	uint8_t d = 0;
	uint8_t e = 0;
	uint8_t f = 0;
	uint8_t g = 0;
	//uint8_t h = 0;
	
	delay(5);
	
	while (Wire.available()>5)
	{
		// loop through all but the last
		a = Wire.read(); // receive byte as a character
		b = Wire.read();
		c = Wire.read();
		d = Wire.read();
		e = Wire.read();
		f = Wire.read();
		g = Wire.read();
		//h = Wire.read();
		String str = "";
		str += a;
		str += b;
		str += c;
		str += d;
		str += e;
		str += f;
		str += g;
		if(str != "0255255255255255255")
		{
			Serial.println(str);
		}
		//.print(a, HEX); Serial.print(b, HEX); Serial.print(c, HEX); Serial.print(d, HEX); Serial.print(e, HEX); // print the character
		//Serial.print(f, HEX); Serial.print(g, HEX); Serial.print('\n');
	}
	//delay(500);

}
