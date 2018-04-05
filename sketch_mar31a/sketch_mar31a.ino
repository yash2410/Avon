// assign pin num
int bed = 7; //connects to pin No. 5 on CD4066
int gar = 8; //connects to pin No. 6 on CD4066
int bath = 6; //connects to pin No. 12 on CD4066
int kit = 5;//connects to pin No. 13 on CD4066

// duration for output
int time = 50;
char command;

void setup() {
  pinMode(bed, OUTPUT);
  pinMode(gar, OUTPUT);
  pinMode(bath, OUTPUT);
  pinMode(kit, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN,HIGH);
  }

void loop() {
   Serial.println(".....");
   delay(1000);
   while(Serial.available()){
    command = Serial.read();
    Serial.println(command); 
    switch(command){
      case '1':
        digitalWrite(gar, HIGH);
        break;
      case '2':
        digitalWrite(bed, HIGH);
        break;
      case '3':
        digitalWrite(kit, HIGH);
        break;
      case '4':
        digitalWrite(bath,HIGH);
        break;
      case '5':
        digitalWrite(gar,LOW);
        break;
      case '6':
        digitalWrite(bed,LOW);
        break;
      case '7':
        digitalWrite(kit, LOW);
        break;
      case '8':
        digitalWrite(bath,LOW);
        break;
       default:
       reset();
       break;    }
    /*if(command.equals("3")){
        digitalWrite(kit, HIGH);
        Serial.println("KITCHEN_ON");
    } else if(command.equals("7")){
        digitalWrite(kit, LOW);
        Serial.println("KITCHEN_OFF");
    } else if(command.equals("4")){
       digitalWrite(bath, HIGH);
        Serial.println("BATH_ON");
    } else if(command.equals("8")){
        digitalWrite(bath, LOW);
        Serial.println("BATH_LOW");
    } else if(command.equals("2")){
        Serial.println("BED_ON");
        digitalWrite(bed, HIGH);
    } else if(command.equals("6")){
        digitalWrite(bed, LOW);
        Serial.println("BED_LOW");
    } else if(command.equals("1")){
        digitalWrite(gar, HIGH);
        Serial.println("GAR_HIGH");
    } else if(command.equals("5")){
        digitalWrite(gar, LOW);
        Serial.println("GAR_LOW");
    }else{
      reset();
      } */
    }
   
    
}


void reset(){
  
  digitalWrite(LED_BUILTIN,HIGH);
  delay(1000);
  
  }
