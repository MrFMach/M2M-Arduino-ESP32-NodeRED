# M2M-Arduino-ESP32-NodeRED
M2M project between Arduino and ESP32 using Node-RED flows.

![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/image2.JPG)

***

## Topics:

:small_blue_diamond: [Project Description](#project-description)

:small_blue_diamond: [Application Topology](#application-topology)

:small_blue_diamond: [UART Protocol](#uart-protocol)

:small_blue_diamond: [MQTT Protocol](#mqtt-protocol)

:small_blue_diamond: [Raspberry Pi](#raspberry-pi)

:small_blue_diamond::small_blue_diamond: [Python Application](#python-application])

:small_blue_diamond::small_blue_diamond: [Node-RED](#node-red)

:small_blue_diamond: [Wiring](#wiring)

:small_blue_diamond: [ESP32 Code - Arduino Ide](#esp32-code---arduino-ide)

:small_blue_diamond: [Results](#results)

***

## Project Description
A M2M (machine-to-machine) project witch make a connection between Arduino Uno and ESP32 boards.
On the Arduin and ESP32 boards, status sensors and LEDs are connected. The Arduino leds signal the status of the sensor connected to the ESP32 and the ESP32 leds signal the status of the sensor connected to the Arduino. This flow was configured in Node-RED, and for communication the AURT and MQTT protocols were used.

***

## Application Topology
The cycle starts in the Python application:

the Python application publishes a message in the "esp32/led" topic of the MQTT broker

ESP32 receives the message from the broker, of the subscribed topic (esp32/led), and in its application:
- handles the message, turning the corresponding led on or off
- reads the pressure and temperature sensor
- publishes in the topics "esp32/press" and "esp32/temp", the read values of pressure and temperature

...Incluir o fluxo do Node-red...

now, the Python application receives the message from the broker, of the subscribed topic (arduino/led), and in its application:


![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/topology.jpg)

***

## UART Protocol
A universal asynchronous receiver-transmitter (UART) can refer to the protocol or the hardware, and as the name says, it is an asynchronous serial communication. A UART is used for full-duplex serial communication between devices equipped with this technology.
Data transfer is done bit by bit, using a wire to send and a wire to receive. To be successful in communication, the parameters of the devices must match, such as baud-rate, data bits, parity and stop-bit.
The simplicity of the application, makes its use very common in systems that do not require high communication speed.

***

## MQTT Protocol
MQTT is a messaging protocol for TCP/IP networks.
It is simple and light. Its basic architecture consists of broker and clients. The message exchange scheme is based on the Publish-Subscribe model.

Version 3.1.1 documentation:
http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html

***

## Raspberry Pi
Raspberry Pi is a series of small computers, which basically connects to a monitor, a keyboard and a mouse. There are several models, varying the available resources and performance.
It is developed in the United Kingdom by the Raspberry Pi Foundation.
In this application, Raspberry Pi 4 Model B with Raspbian operating system (based on Debian) was used. Learn more at https://www.raspberrypi.org/help/

On the Raspberry Pi, will be running the Mosquitto MQTT broker, Node-RED and the Python application. Follow the next instructions.

### Mosquitto Broker Installation
See how to install Mosquitto on repository: https://github.com/MrFMach/Mosquitto-Broker-RaspberryPi

### Node-RED Installation
See how to install Mosquitto on page: https://nodered.org/docs/getting-started/raspberrypi

### Python Application

### Node-RED

![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/flows.png)
***
![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/dashboard.png)

***

## Wiring
![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/fritzing1.png)

***


## ESP32 Code - Arduino Ide

Used libraries:
~~~c++
#include <WiFi.h>
#include <PubSubClient.h>
~~~

GPIO Pins. Configure according to your wiring:
~~~c++
#define YEL 12
#define RED 13
#define GRE 14
~~~

Fill in the name and password of your local network:
~~~c++
const char* ssid = "your ssid";
const char* password = "your password";
~~~

Fill in the IP address of that format, separated by commas:
~~~c++
IPAddress server(000, 000, 000, 000); 
~~~
To find the address, type in the terminal:
```
ip a
```
The IP will be described in "inet".

Finally, fill with mqtt_user and mqtt_password, as configured in the mosquitto ( [here](#mosquitto-user-authentication) ):
~~~c++
if (client.connect("espClient", "mqtt_user", "mqtt_password"))
~~~

***

## Results
![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/gif.gif)

***

Thank you!

#### Fabio Machado
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/fabio-machado-b932a476/)](https://www.linkedin.com/in/fabio-machado-b932a476/)

:computer:  Computer Engeneering  | :zap: Electronic  | :brazil:  Brazil
