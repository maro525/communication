import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress remote;
String address = "/pos";

int receivePort = 1234;
String sendIP = "127.0.0.1";
int sendPort = 1234;
String sendAddress = "/data";

void setup() {
    size(800, 800);
    background(0);

    frameRate(30);

    oscP5 = new OscP5(this, receivePort);
    remote = new NetAddress(sendIP, sendPort);
}

void draw() {

}

void oscEvent(OscMessage message) {
    if(message.checkAddrPattern(address)) {
        int a = message.get(0).intValue();
    }
}

void sendOsc() {
    int i = 1;
    OscMessage myMessage = new OscMessage(sendAddress);
    myMessage.add(i);
    oscP5.send(myMessage, remote);
}

