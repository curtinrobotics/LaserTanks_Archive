#include "AdagioPro.h"

//*********************************************************************************************************//
// Declarations
//*********************************************************************************************************//

// RS-485 RX on pin 6, TX on pin 7 (this is tested on a Arduino MEGA 2560 with linksprite RS-485 v2 shield.)
AdagioPro adagio(6, 7, true);   // RX, TX, PLC-MODE


//*********************************************************************************************************//
// Main methods
//*********************************************************************************************************//

void setup() {
	Serial.begin(115200);
    Serial.println("Initializing RS485");
    // Init RS485 interface
    adagio.Initialize();									// Open comms, turn lights on (relay and soft)
	
	adagio.AutoSyncronize();								// Start the syncronizing sequence for syncing the LED's (if you have more then one)
}

void loop() {
  // Nothing to do here, just wait until the syncing has been done, takes up to 20 seconds 
  // the system will turn itself on and off a couple of times.
}
