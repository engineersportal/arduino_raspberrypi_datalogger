// dummy output for testing Python datalogger
void setup() {
  Serial.begin(9600); // initialize the serial port 
}
void loop() {
  for (int x = 0;x<20;x++){ // loop from 0-19
    Serial.println(x); // print values for Python to read
    delay(100); // delay 100 ms
  }
}
