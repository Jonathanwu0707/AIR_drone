#include <cvzone.h>
#include <Servo.h>
SerialData serialData(4,3); //(numOfValsRec,digitsPerValRec)

/*0 or 1 - 1 digit
0 to 99 -  2 digits 
0 to 999 - 3 digits 
 */

int valsRec[4];
//PWM pins are 3, 5, 6, 9, 10 and 11
boolean run = false;

//  3v(target voltage)/5v(input voltage)*256(PWM 0-255)=153
//  設定PWM輸出值（註：FA-130馬達供電不要超過3v）
int motorSpeed = 10;//

//(KV值）*V(電壓）=rpm（轉速)
//970*11.1=10767

// This is our motor.
Servo Brushless1;
Servo Brushless2;
Servo Brushless3;
Servo Brushless4;
  
void setup() {
  serialData.begin(); 
//  pinMode(LF,OUTPUT);
//  pinMode(LB,OUTPUT);
//  pinMode(RF,OUTPUT);
//  pinMode(RB,OUTPUT);
//  pinMode(13,OUTPUT);
  Brushless1.attach(3);//左後
  Brushless2.attach(5);//右後
  Brushless3.attach(9);//右前
  Brushless4.attach(10);//左前 
  Serial.begin(9600);
  Brushless1.write(0);
  Brushless2.write(0);
  Brushless4.write(0);
  Brushless3.write(0);
}

void loop() {
  serialData.Get(valsRec);
  //pwm output range 0-255
  //val1= LR, val2= FB, val3= UpDown, val4= rotate
  Brushless1.write(-( motorSpeed +valsRec[0] +valsRec[1] +valsRec[2] +valsRec[3]));
  Brushless2.write( motorSpeed +valsRec[0] -valsRec[1] +valsRec[2] -valsRec[3]);
  Brushless3.write( motorSpeed -valsRec[0] +valsRec[1] +valsRec[2] -valsRec[3]);
  Brushless4.write( motorSpeed -valsRec[0] -valsRec[1] +valsRec[2] +valsRec[3]);

  String ans = Serial.readString();
  if (ans == "s") {
    exit(0);
  }
  
//  run= true;

  
//  if (run) {  
//    // 如果要啟動馬達…
//    // 向馬達輸出指定的類比電壓值
//    analogWrite(LF, motorSpeed);
//    analogWrite(LB, motorSpeed);
//  } else {
//    // 否則…
//    // 將馬達的電壓值設定成0
//    analogWrite(LF, 0);
//    analogWrite(LB, 0);
//  }
}
