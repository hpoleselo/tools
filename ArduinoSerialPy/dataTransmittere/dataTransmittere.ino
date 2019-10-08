// Analog Pin A0 from the potentiometer (the middle pin from the potentiometer)
const int potentiometer = 0;
int value = 0;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  value = analogRead(potentiometer);
  Serial.println(value);
  delay(10);
}
