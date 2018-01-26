long randNumber;
String userGuess;
int userIntGuess = 0;
int guessesMade = 0;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  randomSeed(analogRead(0));
  while(!Serial);
  randNumber = random(1, 10000 + 1);
}

void loop() {
  // put your main code here, to run repeatedly:
  //userGuess = Serial.parseInt(Serial.read());
  while(!Serial.available());
  userGuess = Serial.readString();
  userIntGuess = userGuess.toInt();
  
  guessesMade += 1;
  if(userIntGuess > randNumber) {
    delay(1000);
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  
    Serial.print("Guess is too high.");
  }
  
  else if(userIntGuess < randNumber) {
    delay(1000);
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  
    Serial.print("Guess is too low.");
  }
  
  else {
    Serial.println("Guess is correct.");
    Serial.println(guessesMade);
    while(true) {
      delay(1000);
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    }
  }
}
