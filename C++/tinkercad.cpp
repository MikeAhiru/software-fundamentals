const int BATHROOM_LIGHT = 11;
const int BEDROOM_LIGHT = 12;
const int KITCHEN_LIGHT = 13;

void menu(){
  Serial.println("[1]. Turn on bathroom_light");
  Serial.println("[2]. Turn off bathroom_light");
  Serial.println("[3]. Turn on bedroom_light");
  Serial.println("[4]. Turn off bedroom_light");
  Serial.println("[5]. Turn on kitchen_light");
  Serial.println("[6]. Turn off kitchen_light");
  Serial.println("[7]. Turn on all lights");
  Serial.println("[8]. Turn off all lights");
  Serial.println("[9]. Blinking lights");
  Serial.println("Please, press any option: ");
}

void setup() {
  pinMode(BATHROOM_LIGHT, OUTPUT);
  pinMode(BEDROOM_LIGHT, OUTPUT);
  pinMode(KITCHEN_LIGHT, OUTPUT);

  Serial.begin(9600);
  menu();
}

void loop() {
  if (Serial.available() > 0) {
    char opt = Serial.read();

    switch(opt){
      case '1':
        digitalWrite(BATHROOM_LIGHT, HIGH);
        break;
      case '2':
        digitalWrite(BATHROOM_LIGHT, LOW);
        break;
      case '3':
        digitalWrite(BEDROOM_LIGHT, HIGH);
        break;
      case '4':
        digitalWrite(BEDROOM_LIGHT, LOW);
        break;
      case '5':
        digitalWrite(KITCHEN_LIGHT, HIGH);
        break;
      case '6':
        digitalWrite(KITCHEN_LIGHT, LOW);
        break;
      case '7':
        digitalWrite(BATHROOM_LIGHT, HIGH);
        digitalWrite(BEDROOM_LIGHT, HIGH);
        digitalWrite(KITCHEN_LIGHT, HIGH);
        break;
      case '8':
        digitalWrite(BATHROOM_LIGHT, LOW);
        digitalWrite(BEDROOM_LIGHT, LOW);
        digitalWrite(KITCHEN_LIGHT, LOW);
        break;
      case '9':
        for(int i=0; i<100; i++){
          digitalWrite(BATHROOM_LIGHT, HIGH);
          digitalWrite(BEDROOM_LIGHT, HIGH);
          digitalWrite(KITCHEN_LIGHT, HIGH);
          delay(300);
          digitalWrite(BATHROOM_LIGHT, LOW);
          digitalWrite(BEDROOM_LIGHT, LOW);
          digitalWrite(KITCHEN_LIGHT, LOW);
          delay(300);
        }
        break;
      default:
        Serial.println("option invalid");
        break;
    }
  }
}
