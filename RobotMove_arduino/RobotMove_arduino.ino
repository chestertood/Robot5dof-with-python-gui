#include <Servo.h>  // Include the Servo library

Servo servo1;  // Create Servo object for the first servo
Servo servo2;  // Create Servo object for the second servo
Servo servo3;  // Create Servo object for the first servo
Servo servo4;  // Create Servo object for the second servo
Servo servo5;  // Create Servo object for the second servo

// angle1 = 0
// angle2 = 90
// angle3 = 0
// angle4 = 0
// angle5 = 0

int posF_theta1 = 0;
int posA_theta1 = 0;
int posF_theta2 = 69;
int posA_theta2 = 69;
int posF_theta3 = 42;
int posA_theta3 = 0;
int posF_theta4 = 159;
int posA_theta4 = 159;
int posF_theta5 = 0;
int posA_theta5 = 0;
int value1 = 0;  // Initialize value1 to 0
int value2 = 0;
int A = 0;  // Initialize value1 to 0


long tF = 100;
long tA = 0;
int tDelay = 100;

void setup() {
  Serial.begin(9600);
  tF = tF * 1000;
  
  servo1.attach(2);  // Attach the first Servo to pin 2
  servo1.write(posA_theta1);   // Set the first Servo to 0 degrees
  
  servo2.attach(3);  // Attach the second Servo to pin 3
  servo2.write(posA_theta2);   // Set the second Servo to 0 degrees
  
  servo3.attach(4);  // Attach the first Servo to pin 2
  servo3.write(posA_theta3);   // Set the first Servo to 0 degrees
  
  servo4.attach(5);  // Attach the second Servo to pin 3
  servo4.write(posA_theta4);   // Set the second Servo to 0 degrees
  
  servo5.attach(6);  // Attach the second Servo to pin 3
  servo5.write(posA_theta5);   // Set the second Servo to 0 degrees
  
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    
    int thetaValues[5];  // Array to store theta values
    int index = 0;
    char *str = strtok((char *)input.c_str(), ",");

    while (str != NULL && index < 5) {
      thetaValues[index++] = atoi(str);
      str = strtok(NULL, ",");
    }
    if (index == 5) {
      posF_theta1 = thetaValues[0];
      posF_theta2 = thetaValues[1];
      posF_theta3 = thetaValues[2];
      posF_theta4 = thetaValues[3];
      posF_theta5 = thetaValues[4];
      
      // Move each servo to the new position
      
      

      // Print to confirm
      Serial.print("Updated positions to: ");
      Serial.print(posF_theta1); Serial.print(", ");
      Serial.print(posF_theta2); Serial.print(", ");
      Serial.print(posF_theta3); Serial.print(", ");
      Serial.print(posF_theta4); Serial.print(", ");
      Serial.println(posF_theta5);
    }
    else if (input == "6") {
      value1 = 1;  // Set value1 to 1 persistently
      value2 = 0;
      tA = 0;}
    else if (input == "7") {
      value1 = 0;  // Stop the servos immediately
      value2 = 1;  // Set value1 to 1 persistently
      tA = 0;}
    else if (input == "8") {
      value1 = 2;  // Stop the servos immediately
      value2 = 0;  // Set value1 to 1 persistently
      tA = 0;
    
    }
    }
  if (value1 == 1 && value2 == 0 ){
    movej();
  }
  else if (value1 == 2 && value2 == 0){
    moveL();
  }
  else{
    value1 = 0;
    value2 = 1; // Reset state when STOP is triggered
  }
}

void mueveServo1_seta_up() {
  servo1.write(posA_theta1);  
  posA_theta1 = posA_theta1 + 1;
  
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo2_seta_up() { 
  servo2.write(posA_theta2);  
  posA_theta2 = posA_theta2 + 1; 
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo3_seta_up() { 
  servo3.write(posA_theta3);  
  posA_theta3 = posA_theta3 + 1; 
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo4_seta_up() { 
  servo4.write(posA_theta4);  
  posA_theta4 = posA_theta4 + 1; 
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo5_seta_up() { 
  servo5.write(posA_theta5);  
  posA_theta5 = posA_theta5 + 1; 
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo1_seta_down() {
  servo1.write(posA_theta1);  
  posA_theta1 = posA_theta1 - 1;
  
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo2_seta_down() { 
  servo2.write(posA_theta2);  
  posA_theta2 = posA_theta2 - 1; 
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo3_seta_down() { 
  servo3.write(posA_theta3);  
  posA_theta3 = posA_theta3 - 1; 
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo4_seta_down() { 
  servo4.write(posA_theta4);  
  posA_theta4 = posA_theta4 - 1; 
  delay(tDelay);
  tA = tA + tDelay;

}

void mueveServo5_seta_down() { 
  servo5.write(posA_theta5);  
  posA_theta5 = posA_theta5 - 1; 
  delay(tDelay);
  tA = tA + tDelay;

}


void movej(){
      if (posA_theta1 != posF_theta1 && tA <= tF && (posF_theta1-posA_theta1)>=0 ) {
        mueveServo1_seta_up();}
      if  (posA_theta2 != posF_theta2 && tA <= tF && (posF_theta2-posA_theta2)>=0 ) {
        mueveServo2_seta_up();}
      if  (posA_theta3 != posF_theta3 && tA <= tF && (posF_theta3-posA_theta3)>=0 ) {
        mueveServo3_seta_up();}
      if  (posA_theta4 != posF_theta4 && tA <= tF && (posF_theta4-posA_theta4)>=0 ) {
        mueveServo4_seta_up();}    
      if  (posA_theta5 != posF_theta5 && tA <= tF && (posF_theta5-posA_theta5)>=0 ) {
        mueveServo5_seta_up();
      }

      if (posA_theta1 != posF_theta1 && tA <= tF && (posF_theta1-posA_theta1)<=0 ) {
        mueveServo1_seta_down();}
      if  (posA_theta2 != posF_theta2 && tA <= tF && (posF_theta2-posA_theta2)<=0 ) {
        mueveServo2_seta_down();}
      if  (posA_theta3 != posF_theta3 && tA <= tF && (posF_theta3-posA_theta3)<=0 ) {
        mueveServo3_seta_down();}
      if  (posA_theta4 != posF_theta4 && tA <= tF && (posF_theta4-posA_theta4)<=0 ) {
        mueveServo4_seta_down();}    
      if  (posA_theta5 != posF_theta5 && tA <= tF && (posF_theta5-posA_theta5)<=0 ) {
        mueveServo5_seta_down();
      }
}

void moveL(){
      servo1.write(posF_theta1);
      servo2.write(posF_theta2);
      servo3.write(posF_theta3);
      servo4.write(posF_theta4);
      servo5.write(posF_theta5);
      }


