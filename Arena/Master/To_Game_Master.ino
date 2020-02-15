

void printloop()
{
	lcd.setCursor(0,0);
	lcd.print("no");
	digitalWrite(ledPin, HIGH);
	String a;
	
	while(Serial.available()) 
	{
		digitalWrite(ledPin, LOW);
		lcd.setCursor(0,0);
		lcd.print("in");
		delay(5000);
	}
}
