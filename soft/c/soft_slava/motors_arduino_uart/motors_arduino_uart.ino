#include <Arduino_FreeRTOS.h>
#include <semphr.h>
#include <stdbool.h>

#define frequency 1000

void turn_installation1();
void turn_installation2();

int installation1_arr[6]={0};
int installation2_arr[6]={0};


//configure first installation
struct FisrtInstallation
{
const uint8_t STEP_PIN1=2;
const uint8_t DIR_PIN1=3;
const uint8_t STEP_PIN2=4;
const uint8_t DIR_PIN2=5;
const uint8_t ms1_1mot_pin=8;
const uint8_t ms1_2mot_pin=9;
};

struct SecondInstallation
{
const uint8_t STEP_PIN1=22;
const uint8_t DIR_PIN1=24;
const uint8_t STEP_PIN2=26;
const uint8_t DIR_PIN2=28;
const uint8_t ms1_1mot_pin=30;
const uint8_t ms1_2mot_pin=32;
};

struct FisrtInstallation inst1;
struct SecondInstallation inst2;

void setup()
{
  Serial.begin(115200);

  //configure first installation
  pinMode(inst1.STEP_PIN1,OUTPUT);
  pinMode(inst1.DIR_PIN1,OUTPUT);
  pinMode(inst1.STEP_PIN2,OUTPUT);
  pinMode(inst1.DIR_PIN2,OUTPUT);
  pinMode(inst1.ms1_1mot_pin,OUTPUT);
  digitalWrite(inst1.ms1_1mot_pin,HIGH);
  pinMode(inst1.ms1_2mot_pin,OUTPUT);
  digitalWrite(inst1.ms1_2mot_pin,HIGH);
  //configure second installation
  pinMode(inst2.STEP_PIN1,OUTPUT);
  pinMode(inst2.DIR_PIN1,OUTPUT);
  pinMode(inst2.STEP_PIN2,OUTPUT);
  pinMode(inst2.DIR_PIN2,OUTPUT);
  pinMode(inst2.ms1_1mot_pin,OUTPUT);
  digitalWrite(inst2.ms1_1mot_pin,HIGH);
  pinMode(inst2.ms1_2mot_pin,OUTPUT);
  digitalWrite(inst2.ms1_2mot_pin,HIGH); 
}

void loop()
{
  if (Serial.available() > 0) 
    {
      String str=Serial.readStringUntil('\0');
      int signals[7]={0};
      
      Convert_to_int(str,signals);
      if (signals[0]==1)
        {
          //Serial.print("1");
          for  (int i=0;i<6;i++) installation1_arr[i]=signals[i+1];
          xTaskCreate(turn_installation1,"installation1",1024, NULL,5,NULL);
          
        }
      if (signals[0]==2)
        {
          //Serial.print("2");         
          for  (int i=0;i<6;i++) installation2_arr[i]=signals[i+1];
          xTaskCreate(turn_installation2,"installation1",1024, NULL,5,NULL);
        }
      
      
    }
}

void Convert_to_int(String str,int *intarr)
{
String number="";
    int j=0;
    for (int i=0;str[i]!='\0';i++)
    {
      if (str[i]==';')
      {
        intarr[j]=atoi(number.c_str());
        j++;
        number="";
      }
      else
      {
        number=number+str[i];
      }
    }
    intarr[j]=atoi(number.c_str());  
  }


void turn_installation1(void *pvParameters)
{
      digitalWrite(inst1.DIR_PIN1,installation1_arr[2]);       //code for two motors
      digitalWrite(inst1.DIR_PIN2,installation1_arr[5]);
      while (installation1_arr[1]>0||installation1_arr[4]>0)
        {
          if (installation1_arr[1]>0) digitalWrite(inst1.STEP_PIN1,HIGH);
          if (installation1_arr[4]>0) digitalWrite(inst1.STEP_PIN2,HIGH);
          delayMicroseconds(frequency);
          digitalWrite(inst1.STEP_PIN1,LOW);
          digitalWrite(inst1.STEP_PIN2,LOW);
          installation1_arr[1]--;
          installation1_arr[4]--;
          delayMicroseconds(frequency);
        } 
      Serial.print('1');
}

void turn_installation2(void *pvParameters)
{
    digitalWrite(inst2.DIR_PIN1,installation2_arr[2]);       
    digitalWrite(inst2.DIR_PIN2,installation2_arr[5]);
    while (installation2_arr[1]>0||installation2_arr[4]>0)
      {
        if (installation2_arr[1]>0) digitalWrite(inst2.STEP_PIN1,HIGH);
        if (installation2_arr[4]>0) digitalWrite(inst2.STEP_PIN2,HIGH);
        delayMicroseconds(frequency);
        digitalWrite(inst2.STEP_PIN1,LOW);
        digitalWrite(inst2.STEP_PIN2,LOW);
        installation2_arr[1]--;
        installation2_arr[4]--;
        delayMicroseconds(frequency);
      } 
    Serial.print('2');
}
