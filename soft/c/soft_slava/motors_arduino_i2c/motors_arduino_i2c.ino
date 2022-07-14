#include  <Wire.h>
#define frequency 1500
#define STEP_PIN1 2
#define DIR_PIN1 3
#define STEP_PIN2 4
#define DIR_PIN2 5
#define ms1_1mot_pin 8
#define ms1_2mot_pin 9 

int SLAVE_ADDRESS=0x04;
int ledPin=13;
int analogPin=A0;
boolean ledOn=false;

//-----------------------------
void write_data(int a,int b,int c)//выводит принятые данные
{
    Serial.println(a);
    Serial.println(b);
    Serial.println(c);  
}
//----------------------------
void toggleLED() //меняет состояние встроенного пина
{
  ledOn=!ledOn;
  digitalWrite(ledPin,ledOn);
  
 }
//---------------------------
void sendAnalogReading() //отправляет данные с аналогового входа
{
  int reading=analogRead(analogPin);
  Wire.write(reading>>2); //отправляем данные , для пирмера читал аналаговый вход
  }
//----------------------------------
void rmotor(int motor,int steps,int dir)
{
  if (motor==1){
digitalWrite(DIR_PIN1,dir);
 for (int i=0;i<steps;i++) {
  digitalWrite(STEP_PIN1,HIGH);
  delayMicroseconds(frequency);
  digitalWrite(STEP_PIN1,LOW);
  }}

if (motor==2){
digitalWrite(DIR_PIN2,dir);
 for (int i=0;i<steps;i++) {
  digitalWrite(STEP_PIN2,HIGH);
  delayMicroseconds(frequency);
  digitalWrite(STEP_PIN2,LOW);
  }
  }
}
//------------------------------
void rmotors(int motor1,int steps1,int dir1,int motor2,int steps2,int dir2)
{
  digitalWrite(DIR_PIN1,dir1);       //code for two motors
  digitalWrite(DIR_PIN2,dir2);
  while (steps1>0||ateps2>0)
  {
    if (steps1>0) digitalWrite(STEP_PIN1,HIGH);
    if (steps2>0) digitalWrite(STEP_PIN2,HIGH);
    delayMicroseconds(frequency);
    digitalWrite(STEP_PIN1,LOW);
    digitalWrite(STEP_PIN2,LOW);
    steps1--;
    steps2--;
  }
}

  

void setup() {
  // put your setup code here, to run once:
pinMode(ledPin,OUTPUT);
Wire.begin(SLAVE_ADDRESS);//задаем адресс ведомого устройства
Wire.onReceive(processMessage);//функция которая вызывается при посткплении данных от мастера
Wire.onRequest(sendAnalogReading);//функция которая вызывается при получении запросов от мастера
Serial.begin(9600);
pinMode(STEP_PIN1,OUTPUT);
pinMode(DIR_PIN1,OUTPUT);
pinMode(STEP_PIN2,OUTPUT);
pinMode(DIR_PIN2,OUTPUT);
pinMode(ms1_1mot_pin,OUTPUT);
digitalWrite(ms1_1mot_pin,HIGH);
pinMode(ms1_2mot_pin,OUTPUT);
digitalWrite(ms1_2mot_pin,HIGH);
}

void loop() {}



void processMessage(int n)
{  
   int a,b,c;
   //пробовал организовать через массив , не получилось , передаются каждый раз одинаковые числа ,не понятно откуда взятые   
   a=Wire.read();
   b=Wire.read();
   c=Wire.read();
   
   write_data(a,b,c);
   rmotor(a,b,c);
   toggleLED();
   

}
