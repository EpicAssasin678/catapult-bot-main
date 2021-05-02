

void setup(){
    Serial.begin(9600);
}


void loop(){
    Serial.println("Beggining communication. Communicating with raspberry pi.");
    delay(500);
}

void printMessage(String message) {
    Serial.println(message);
}

String readMessage() {
    return Serial.readString();
}