/*
AdagioPro.cpp - Library for Adagio Pro Pool Lights.
Created by Filip Slaets, January 23, 2017.
*/
// For Arduino 1.0 and earlier
#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif

#include "AdagioPro.h"
#include "SoftwareSerial.h"

AdagioPro::AdagioPro(int rxPin, int txPin, bool plcMode) {
	_plcMode = plcMode;
	_serial = new SoftwareSerial(rxPin, txPin);
	_lastMilliWrite = 0;
}

void AdagioPro::Initialize() {
	// Allowed in PLC and OnOff mode
	_serial->begin(9600);
	RelayOnOff(true);
	delay(WRITE_DELAY);
	AllLampsOn();
	delay(WRITE_DELAY);
}

void AdagioPro::AllLampsOff() {
	// Allowed in PLC and OnOff mode
	if (!MaySend()) return;
	_serial->print("PL0");
	RecordSend();
}

void AdagioPro::AllLampsOn() {
	// Allowed in PLC and OnOff mode
	if (!MaySend()) return;
	_serial->print("PL1");
}

void AdagioPro::ProgramUp() {
	// Allowed in PLC and OnOff mode
	if (!MaySend()) return;
	_serial->print("PsU");
	RecordSend();
}

void AdagioPro::ProgramDown() {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (!MaySend()) return;
	_serial->print("PsU");
	RecordSend();
}

void AdagioPro::SetProgram(int x) {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (x < 1 || x > 14) return;	// out of range
	if (!MaySend()) return;
	// PSxx  xx = 01-14
	_serial->print("PS");
	SendPaddedTwoDigit(x);
	RecordSend();
}

void AdagioPro::AutoSyncronize() {
	// Allowed in PLC and OnOff mode
	if (!MaySend()) return;
	_serial->print("PsS");
	RecordSend();
}

void AdagioPro::White1() {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (!MaySend()) return;
	_serial->print("PW1");
	RecordSend();
}

void AdagioPro::White2() {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (!MaySend()) return;
	_serial->print("PW2");
	RecordSend();
}

void AdagioPro::White3() {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (!MaySend()) return;
	_serial->print("PW3");
	RecordSend();
}

void AdagioPro::SetRGB(int r, int g, int b) {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (r < 0 || r > 255) return;	// out of range
	if (g < 0 || g > 255) return;	// out of range
	if (b < 0 || b > 255) return;	// out of range
	if (!MaySend()) return;
	_serial->print("PC");
	SendPaddedThreeDigit(r);
	SendPaddedThreeDigit(g);
	SendPaddedThreeDigit(b);
	RecordSend();
}

void AdagioPro::SetDimValue(int pct) {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (!MaySend()) return;
	_serial->print("PD");
	SendPaddedThreeDigit(pct);
	RecordSend();
}

void AdagioPro::SetDMXStartAddress(int address) {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (!MaySend()) return;
	_serial->print("PA");
	SendPaddedThreeDigit(address);
	_serial->print("E");
	RecordSend();
}

void AdagioPro::SetColorInPct(int r, int g, int b) {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (r < 0 || r > 100) return;	// out of range
	if (g < 0 || g > 100) return;	// out of range
	if (b < 0 || b > 100) return;	// out of range
	if (!MaySend()) return;
	_serial->print("Pp");
	SendPaddedThreeDigit(r);
	SendPaddedThreeDigit(g);
	SendPaddedThreeDigit(b);
	_serial->print("e");
	RecordSend();
}

void AdagioPro::SetColorHex(int r, int g, int b) {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (r < 0 || r > 255) return;	// out of range
	if (g < 0 || g > 255) return;	// out of range
	if (b < 0 || b > 255) return;	// out of range
	if (!MaySend()) return;
	_serial->print("Pc");
	_serial->print(r, HEX);
	_serial->print(g, HEX);
	_serial->print(b, HEX);
	_serial->print("e");
	RecordSend();
}

void AdagioPro::RelayAControl(char mode) {
	// Allowed in PLC and OnOff mode
	if (!MaySend()) return;
	_serial->print("PRA");
	if (mode != '1' || mode != '0' || mode != 'P') return;	// out of range
	_serial->print(mode);
	RecordSend();
}

void AdagioPro::RelayBControl(char mode) {
	// Allowed in PLC and OnOff mode
	if (!MaySend()) return;
	_serial->print("PRB");
	if (mode != '1' || mode != '0' || mode != 'P') return;	// out of range
	_serial->print(mode);
	RecordSend();
}

void AdagioPro::RelayOnOff(bool on) {
	// Allowed in PLC and OnOff mode
	if (!MaySend()) return;
	_serial->print("PRM");
	if (on) {
		_serial->print("1");
	}
	else {
		_serial->print("0");
	}
	RecordSend();
}

void AdagioPro::ColorTemperature(int tenThousand, int thousand, int hundred) {
	// Allowed in PLC only
	if (!_plcMode) return;
	if (tenThousand < 0 || tenThousand > 9) return;	// out of range
	if (thousand < 0 || thousand > 9) return;	// out of range
	if (hundred < 0 || hundred > 9) return;	// out of range
	if (!MaySend()) return;
	_serial->print("PT");
	_serial->print(tenThousand);
	_serial->print(thousand);
	_serial->print(hundred);
	RecordSend();
}

// *********************************************************
// Private methods
// *********************************************************
void AdagioPro::SendPaddedTwoDigit(int digit) {
	if (digit < 10) {
		_serial->print("0");
	}
	_serial->print(digit);
}

void AdagioPro::SendPaddedThreeDigit(int digit) {
	if (digit < 100) {
		_serial->print("0");
	}
	if (digit < 10) {
		_serial->print("0");
	}
	_serial->print(digit);
}

bool AdagioPro::MaySend() {
	if (_lastMilliWrite == 0) return true;	// initial command
	return millis() >= _lastMilliWrite + WRITE_DELAY;
}

void AdagioPro::RecordSend() {
	// WRITE_DELAY
	_lastMilliWrite = millis();
}