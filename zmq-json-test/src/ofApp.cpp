#include "ofApp.h"

#include "ofxZmq.h"

ofxZmqSubscriber subscriber;
ofxZmqPublisher publisher;

void ofApp::setup()
{
    // start client
    subscriber.connect("tcp://localhost:3000");
}

void ofApp::update()
{
    while (subscriber.hasWaitingMessage())
    {
        ofBuffer data;
        subscriber.getNextMessage(data);
        
        std::string data_json = data.getText();
        std::cout << data_json << endl;
        
        bool parseSuccessful = result.parse(data_json);
        std::size_t numBodies = result["bodies"].size();
        if(numBodies == 0)
            continue;
    }
}

void ofApp::draw()
{
    ofBackground(0);

    ofSetHexColor(0x00FF00);

}
