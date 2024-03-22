#include <Servo.h>

Servo servo;
#define LED_PIN LED_BUILTIN
#define pinServo 9

unsigned long previousMillis = 0;
const long interval = 3000;

void setup() {
  Serial.begin(9600);
  servo.attach(pinServo);
  servo.write(90);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();
  
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    if (Serial.available() > 0) {
      String command = Serial.readStringUntil('\n');  // Read the command until newline character
      if (command.equals("plastic")) {
        // Turn on LED
        digitalWrite(LED_PIN, LOW);
        Serial.println("Plastic");
        servo.write(180);
        delay(5000);
        servo.write(90);
      } else if (command.equals("paper")) {
        // Turn off LED
        digitalWrite(LED_PIN, HIGH);
        Serial.println("Paper");
        servo.write(0);
        delay(5000);
        servo.write(90);
      } else {
        Serial.println("Waiting for object...");
        servo.write(90);
        delay(1000);
      }
    }
  }
}
