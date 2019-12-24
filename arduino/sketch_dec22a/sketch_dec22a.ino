#include <DRV8835MotorShield.h>
DRV8835MotorShield motors;
int incoming_state = 1;

#define LED_PIN 13
void setup() {
  Serial.begin(9600);
  motors.flipM1(true);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    incoming_state = incoming_state * (Serial.read() - '0');
    Serial.println(incoming_state);
    if(incoming_state == 0) {
        digitalWrite(LED_PIN, LOW);
        motors.setM1Speed(200);
    }
    else if(incoming_state == 1) {
        digitalWrite(LED_PIN, HIGH);
        motors.setM1Speed(-200);
    }
    else {
      motors.setM1Speed(0);
    }
  }
  delay(1);
}
