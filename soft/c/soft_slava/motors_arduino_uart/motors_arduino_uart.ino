#define frequency 2000
#define STEP_PIN1 2
#define DIR_PIN1 3
#define STEP_PIN2 4
#define DIR_PIN2 5 
#define ms1_1mot_pin 8
#define ms1_2mot_pin 9


#define ms1_for_first 1
#define ms1_for_second 1

void Convert_to_int(String str,int *intarr)
{
String number="";
    int j=0;
    for (int i=0;str[i]!='\0';i++)
    {
      if (str[i]==' ')
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


void setup()
  {
      // put your setup code here, to run once:
    Serial.begin(115200);
    pinMode(STEP_PIN1,OUTPUT);
    pinMode(DIR_PIN1,OUTPUT);
    pinMode(STEP_PIN2,OUTPUT);
    pinMode(DIR_PIN2,OUTPUT);
    pinMode(ms1_1mot_pin,OUTPUT);
    digitalWrite(ms1_1mot_pin,HIGH);
    pinMode(ms1_2mot_pin,OUTPUT);
    digitalWrite(ms1_2mot_pin,HIGH);
  }

void loop() {
  // put your main code here, to run repeatedly: 
  if (Serial.available() > 0) 
    {
  
      String str=Serial.readStringUntil('\0');
      int intarr[6]={0};
      
      Convert_to_int(str,intarr);
      
      
      //Serial.read();
      
      
      digitalWrite(DIR_PIN1,intarr[2]);       //code for two motors
      digitalWrite(DIR_PIN2,intarr[5]);
      while (intarr[1]>0||intarr[4]>0)
        {
          if (intarr[1]>0) digitalWrite(STEP_PIN1,HIGH);
          if (intarr[4]>0) digitalWrite(STEP_PIN2,HIGH);
          delayMicroseconds(frequency);
          digitalWrite(STEP_PIN1,LOW);
          digitalWrite(STEP_PIN2,LOW);
          intarr[1]--;
          intarr[4]--;
        } 
      if (intarr[0]!=0) Serial.print("done");  
    }
}


 
