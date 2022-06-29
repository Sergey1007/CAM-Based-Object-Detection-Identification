#include  <Wire.h>
int SLAVE_ADDRESS=0x04;
int ledPin=13;
int analogPin=A0;
boolean ledOn=false;

//-----------------------------
void write_array(int a[4])
{
  for (int i=0;i<4;i++)
  {
    Serial.println(a[i]);
  }
  
}
//----------------------------
void toggleLED()
{
  ledOn=!ledOn;
  digitalWrite(ledPin,ledOn);
  
  }
//---------------------------
void sendAnalogReading()
{
  int reading=analogRead(analogPin);
  Wire.write(reading>>2); //отправляем данные , для пирмера читал аналаговый вход
  }



  

void setup() {
  // put your setup code here, to run once:
pinMode(ledPin,OUTPUT);
Wire.begin(SLAVE_ADDRESS);//задаем адресс ведомого устройства
Wire.onReceive(processMessage);//функция которая вызывается при посткплении данных от мастера
Wire.onRequest(sendAnalogReading);//функция которая вызывается при получении запросов от мастера
Serial.begin(9600);
}

void loop() {

}

void processMessage(int n)
{  
   int a,b,c;
   //пробовал организовать через массив , не получилось , передаются каждый раз одинаковые числа ,не понятно откуда взятые   
   a=Wire.read();
   b=Wire.read();
   c=Wire.read();
   
   Serial.println(a);
   Serial.println(b);
   Serial.println(c);

   toggleLED();

}
