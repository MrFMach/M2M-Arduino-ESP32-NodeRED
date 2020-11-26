#include <HCSR04.h>

int triggerPin = 4;
int echoPin = 5;
UltraSonicDistanceSensor distanceSensor(triggerPin, echoPin);

void setup () {
  Serial.begin(4800, SERIAL_8N1);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop () {
}

void serialEvent() {
  while (Serial.available()) {
    int receivedByte = Serial.read();

    switch (receivedByte) {
      case 82 :                 // 'R' red led
        digitalWrite(2, HIGH);
        digitalWrite(3, LOW);
        break;
      case 89 :                 // 'Y' yellow led
        digitalWrite(3, HIGH);
        digitalWrite(2, LOW);
        break;
      case 79 :                 // 'O' turn-off leds
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        break;
    }
    // send datas to Raspberry Pi
    float distance = distanceSensor.measureDistanceCm();
    char lineFeed = 10;
    Serial.print(distance);
    Serial.print(lineFeed);
  }
}
