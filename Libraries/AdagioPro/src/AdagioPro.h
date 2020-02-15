
/*
  AdagioPro.h - Library for Adagio Pro Pool Lights.
  Created by Filip Slaets, January 23, 2017.
*/
#ifndef AdagioPro_h
#define AdagioPro_h

#define WRITE_DELAY 20			// 20 ms delay after writing

#include "SoftwareSerial.h"

class AdagioPro {
private:
	bool _plcMode;
	SoftwareSerial* _serial;
	long _lastMilliWrite;
public:
	// Constructor (plcMode is running mode of the PLP-REM300)
	AdagioPro(int rxPin, int txPin, bool plcMode);
	
	// Initialize the RS module (open comms)
	void Initialize();
	// All lamps OFF
	void AllLampsOff();
	// All lamps ON
	void AllLampsOn();
	// Jump to next program
	void ProgramUp();
	// Return to previous program
	void ProgramDown();
	// xx is the decimal representation of the program number (01 - 14)
	void SetProgram(int x);
	// executes the auto sync procedure
	void AutoSyncronize();
	// Jump to White 1 (program 12)
	void White1();
	// Jump to White 2 (program 13)
	void White2();
	// Jump to White 3 (program 14)
	void White3();
	// rrr, ggg and bbb are the decimal representation of the RGB value (with leading zero’s)
	// example: 
	// 1) PC255128064 = Full output level on Red color, half output	level on Green color, 1 / 4 output level on Blue color
	// 2) PC255255255 = All colors at full output level
	// 3) PC000000000 = All colors OFF
	void SetRGB(int r, int g, int b);
	// Set the OUTPUT value of the lamp in % (000 - 100) on all LEDS
	void SetDimValue(int pct);
	// PA035E = set DMX start address to 35 [35(R), 36(G), 37(B)]
	void SetDMXStartAddress(int address);
	// variable size, rgb = ASCII 0-255, e = end character
	// example: Pp25050100e = Red 25%, Green 50%, Blue 100%
	void SetColorInPct(int r, int g, int b);
	// variable size, rgb = ASCII 0-255, e = end character
	// example: Pc64128255e = Red 25%, Green 50%, Blue 100%
	void SetColorHex(int r, int g, int b);
	// x = 1 (ON), 0 (OFF), P (Pulse) !this overrules dipswitch
	// example: PRA1 = Relay A ON PRA0 = Relay A OFF
	void RelayAControl(char mode);
	// x = 1 (ON), 0 (OFF), P (Pulse) !this overrules dipswitch
	// example: PRB1 = Relay A ON PRA0 = Relay A OFF
	void RelayBControl(char mode);
	// PRM1 = Relay ON/OFF control ON
	void RelayOnOff(bool on);
	// x = ten thousand ; y = thousand ; z = hundred
	// example: PT035 = Set white color temperature to 3500K (in steps of 500K)
	// = ColorTemperature(0,3,5);
	void ColorTemperature(int tenThousand, int thousand, int hundred);
private:
	// Does zero padding for getting two digits and sends it over the line
	void SendPaddedTwoDigit(int digit);
	void SendPaddedThreeDigit(int digit);
	bool MaySend();
	void RecordSend();
};

#endif