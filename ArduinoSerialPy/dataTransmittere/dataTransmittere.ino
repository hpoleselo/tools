// Analog Pin A0 from the potentiometer (the middle pin from the potentiometer)
const int potentiometer = 0;
int value = 0;
int actualTime = 0;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  actualTime = millis();
  value = analogRead(potentiometer);
  Serial.print(actualTime);
  Serial.print(",");
  Serial.println(value);
  delay(100);
}
