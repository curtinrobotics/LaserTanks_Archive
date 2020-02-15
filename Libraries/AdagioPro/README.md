# Arduino.AdagioPro
Spectrovision Adagio Pro Pool light library for arduino by Filip Slaets

Makes the leds controllable from an Arduino (compatible) device.

## What does it do

It makes it possible by simple coding instructions to control the AdagioPro RGB Poollights of your pool.
This way you can hookup other events with your lights.

I for example use it to make my poollights react on music when there is a party ;)

## What do you needed

- An arduino controller (i have an Arduino Mega 2560)
- RS-485 shield (got a linksprite RS-485 v2.0 shield)
- AdagioPro RGB poollights (and preferably a pool also) (example of such a light)[https://www.poolandspacentre.co.uk/products/spectravision-adagio-pro-led-lights.html]
- PLPREM-300 module which drives the poollights (manual)[http://propulsionsystems.be/sites/default/files/downloads/manual_PLP-REM-300_NL.pdf]
- A Wire to connect from the RS-485 shield to the PLPREM300 RS-485 connector.

## Download and install

Lastest release: v1.0.0

1. Download latest release
2. Extract it to the **libraries** folder inside your Sketchbook. Default is **[user]\Arduino\libraries**.
3. Restart Arduino IDE if you had it open.
4. Done

## Usage

### AdagioPro object

Using this library is straight forward. Just create a new object that you can use through your sketch.

	AdagioPro myAdagio([rxPin], [txPin], [true/false]);

where:
- rxPin: is the RX pin for the RS-485 shield (i use linksprite RS-485 v2.0 shield)
- txPin: is the TX pin for the RS-485 shield
- true/false :  true when running in PLC mode, false when running in Classic mode (adagio installation specific)

**Note: this object will protect the PLREM by throttling the speed of the commands, every 20ms by default you send a new command. 
This is done because my lights tend to de-syncronize if I send instructions too fast. 
If your installation does not have that problem then you can shorten this delay by setting the constant in AdagioPro.h**

	#define WRITE_DELAY 20

**to a shorter value the delay is in milliseconds.**

### Initialisation

After that you should initialize the object which will open communications to the RS-485 shield.

	myAdagio.Initialize();

This library uses the *SoftwareSerial* library in the background. 

You can change it in the AdagioPro.h file if desired:

	comment out the line : 

	#include "SoftwareSerial.h"

	change the line:

	SoftwareSerial* _serial;

	to your own serial communiciation port, like for example:

	HardwareSerial* _serial;

	then you should edit the constructor part in AdagioPro.cpp 

	from:	_serial = new SoftwareSerial(rxPin, txPin);

	to:		_serial = &Serial1; // if you want to use Serial1 for example


### Calls you can make

Short explanation of the calls you can make to the PLPREM 300 module of your AdagioPro lights.

#### Turn all lamps off
	myAdagio.AllLampsOff();

#### Turn all lamps ON
	myAdagio.AllLampsOn();

#### Jump to next program
	myAdagio.ProgramUp();

#### Return to previous program
	myAdagio.ProgramDown();

#### Goto a specific program (1 - 14)
	myAdagio.SetProgram(x); // 1 <= x <= 14

#### Execute the auto sync procedure

There is an example in the library which illustrates this, this should be used at installation time if needed.

	myAdagio.AutoSyncronize();

#### Jump to White 1 (program 12)
	myAdagio.White1();

#### Jump to White 2 (program 13)
	myAdagio.White2();

#### Jump to White 3 (program 14)
	myAdagio.White3();

#### Set RGB colors
	// rrr, ggg and bbb are the decimal representation of the RGB value (with leading zero’s)
	void SetRGB(int r, int g, int b);

	myAdagio.SetRGB(0,0,0);			// turn of all the lights
	myAdagio.SetRGB(255,0,0);		// set to max brightness RED

#### Set the OUTPUT value of the lamp in % (000 - 100) on all LEDS
	void SetDimValue(int pct);

	myAdagio.SetDimValue(50);		// Dim the lights to 50%

#### Set DMX address (when you use DMX input to PLPREM module)
	
	void SetDMXStartAddress(int address);

	myAdagio.SetDMXStartAddress(35);		// Set DMX start address to 35 [35(R), 36(G), 37(B)]

#### Set color in percentage

r, b, g are in range of 0 to 100

	void SetColorInPct(int r, int g, int b);

	myAdagio.SetColorInPct(0, 100, 0);		// put green to 100% brightness

#### Set color in HEX

This is actually an other way to communicate to the controller but equally in calling it from the code. This instruction will send the color values in HEX instead of decimal.

	void SetColorHex(int r, int g, int b);

	myAdagio.SetColorHex(0, 0xFF, 0);	// put green to max
	
#### Switch relay A of the PLPREM Module
	// x = '1' (ON), '0' (OFF), 'P' (Pulse) !this overrules dipswitch
	void RelayAControl(char mode);

####  Switch relay B of the PLPREM Module
	// x = 1 (ON), 0 (OFF), P (Pulse) !this overrules dipswitch
	void RelayBControl(char mode);

#### Switch all relays on or off (kills the power to lights itself also)
	void RelayOnOff(bool on);

	myAdagio.RelayOnOff(true); // turn on the lights (relay wise)

#### Set color temperature
	// x = ten thousand ; y = thousand ; z = hundred
	// example: PT035 = Set white color temperature to 3500K (in steps of 500K)
	// = myAdagio.ColorTemperature(0,3,5);
	void ColorTemperature(int tenThousand, int thousand, int hundred);