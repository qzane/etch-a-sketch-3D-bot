
/*
 Stepper Motor Control w/ Serial

 This program drives two stepper motor and takes commands from serial port
 
 forked from Arduino Stepper Library by Tom Igoe


 Created June.17 2024
 by Qzane
 */

#include <Stepper.h>

#define STEPPER1_PINS 26,33,25,32
#define STEPPER2_PINS 13,14,12,27

const int stepsPerRevolution = 2048;  // change this to fit the number of steps per revolution
const int MAX_X = 6500; // 250 + 6500 + 250
const int MAX_Y = 4000; // 300 + 4000 + 250


// initialize the stepper library 
Stepper myStepper1(stepsPerRevolution, STEPPER1_PINS);
Stepper myStepper2(stepsPerRevolution, STEPPER2_PINS);

void dXdY(int dx, int dy){
    myStepper1.step(dx);
    myStepper2.step(dy);
}


int POS_X = 0;
int POS_Y = 0;

void reset_pos(){
  dXdY(-7200, -5000);
  dXdY(0, 400);
  dXdY(400, 0);
  dXdY(6500, 4000);
  dXdY(-6500, -4000);
  POS_X = 0;
  POS_Y = 0;
}

void toXY(int x, int y){
  int dx, dy;
  dx = x - POS_X;
  dy = y - POS_Y;
  POS_X = x;
  POS_Y = y;
  dXdY(dx, dy);
}


void setup() {
  myStepper1.setSpeed(10); // 18 max w/ charger power, 10 max w/ usb power?
  myStepper2.setSpeed(10); 
  // initialize the serial port:
  Serial.begin(9600);  
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
  //reset_pos();
  Serial.print("dXdY: 0 0\n");
}

void loop() {
  int dx, dy;
  if (Serial.available() > 0) {
    dx = Serial.parseInt();
    dy = Serial.parseInt();
    Serial.print("dXdY: ");
    Serial.print(dx);
    Serial.print(' ');
    Serial.print(dy);
    Serial.print('\n');
    dXdY(dx, dy);
  }
  delay(100);
}

