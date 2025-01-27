/* Charlotte BRICOUT et Nathan MARTIN - IMA 5 Polytech Lille */
/* 05.02.2015 */ 
/* Control of 3 cavities in order to move a silicone robot */

/*  PIN assignments Serie 1: */

const byte PINsense1 = 0;         // Actuator 1 pressure sense
const byte PINsense2 = 1;         // Actuator 2 pressure sense
const byte PINsense3 = 2;         // Actuator 3 pressure sense
const byte PINpressure1 = 10;     // Actuator 1 pressure command
const byte PINpressure2 = 9;      // Actuator 2 pressure command
const byte PINpressure3 = 8;      // Actuator 3 pressure command

// initialization

int nbCavity=3;
boolean setNumberCavity=true; 

int Cavity_Pressure[3];

int header = 0; //to spot the beginning of informations on the serial port
int pressure= 0; //Pressure in cavity at the initialization 

int test=0;

#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup() 
{ 
  // set ADC prescaler to 16 ->77kHz read
  sbi(ADCSRA,ADPS2) ;
  cbi(ADCSRA,ADPS1) ;
  cbi(ADCSRA,ADPS0) ;
  
  analogReference(INTERNAL2V56);
  analogRead(PINsense1);
  analogRead(PINsense2);
  analogRead(PINsense3);

  TCCR1B = TCCR1B & 0b11111000 | 0x01;  //Prescaler 1 modified, fPWM=32kHz
  TCCR2B = TCCR2B & 0b11111000 | 0x01;  //Prescaler 2 modified, fPWM=32kHz
  TCCR3B = TCCR3B & 0b11111000 | 0x01;  //Prescaler 3 modified, fPWM=32kHz
  TCCR4B = TCCR4B & 0b11111000 | 0x01;  //Prescaler 4 modified, fPWM=32kHz
  
  analogWrite(PINpressure1, 0);
  analogWrite(PINpressure2, 0);
  analogWrite(PINpressure3, 0);

  Serial.begin(115200);  
  delay(2000);
  /*
  // we send the number of cavity
  int c;  
  while(c!=97)
  {
  while(!Serial.available());
  c = Serial.read();
  delay(1);
  if(c!=97)
  {
    Serial.print(-1);
  }
  }
  
  Serial.print(nbCavity);
  Serial.flush();
  delay(1);
*/
} 

void loop() 
{
  if(Serial.available())
  {
   delay(1);
   test=Serial.read();
   while(test!=245)
   {
     delay(1);
     test=Serial.read();
   }
   
   test=Serial.read();

// 0.33 = facteur pour passer de Sofa aux distributeurs pneumatiques
   while(!Serial.available());
   Cavity_Pressure[0]=0.33*Serial.read();
   delay(1);
   while(!Serial.available());
   Cavity_Pressure[1]=0.33*Serial.read();
   delay(1);
   while(!Serial.available());
   Cavity_Pressure[2]=0.33*Serial.read();
   delay(1);
  }

  Cavity_Pressure[0]=constrain(Cavity_Pressure[0], 1,80);
  Cavity_Pressure[1]=constrain(Cavity_Pressure[1], 1,80);
  Cavity_Pressure[2]=constrain(Cavity_Pressure[2], 1,80);
  
  analogWrite(PINpressure1,Cavity_Pressure[2]); 
  //delay(1);
  analogWrite(PINpressure2,Cavity_Pressure[1]); 
  //delay(1);
  analogWrite(PINpressure3,Cavity_Pressure[0]); 
  //delay(1);
} 
