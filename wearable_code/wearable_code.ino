boolean tilt = false;

void setup() {
  pinMode(3, INPUT);
  pinMode(4, OUTPUT);
  pinMode(0, OUTPUT);
}

void loop() {
  
  tilt = digitalRead(3);

  if(tilt == true) {
    digitalWrite(4, HIGH);
    digitalWrite(0, HIGH);
    delay(100);
    digitalWrite(0, LOW);
    digitalWrite(4, LOW);
  }  
}
