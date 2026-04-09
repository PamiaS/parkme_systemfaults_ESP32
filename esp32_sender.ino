//This is a test file implemented in Arduino Sketch(.ino) to make sure that the ESP32 works and can show data on serial port.
int available_spots = 25;// This is just a test number

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println(available_spots);
  delay(1000);
}
