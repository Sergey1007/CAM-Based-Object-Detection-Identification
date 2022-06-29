#include  <Wire.h>
#define frequency 2000
#define STEP_PIN1 2
#define DIR_PIN1 3
#define STEP_PIN2 4
#define DIR_PIN2 5 

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
 for (int i=0;i<4*steps;i++) {
  digitalWrite(STEP_PIN1,HIGH);
  delayMicroseconds(frequency);
  digitalWrite(STEP_PIN1,LOW);
  }}

if (motor==2){
digitalWrite(DIR_PIN2,dir);
 for (int i=0;i<4*steps;i++) {
  digitalWrite(STEP_PIN2,HIGH);
  delayMicroseconds(frequency);
  digitalWrite(STEP_PIN2,LOW);
  }
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
