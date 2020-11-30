# M2M-Arduino-ESP32-NodeRED
M2M project between Arduino and ESP32 using Node-RED flows.

![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/image2.JPG)

***

## Topics:

:small_blue_diamond: [Project Description](#project-description)

:small_blue_diamond: [UART Protocol](#uart-protocol)

:small_blue_diamond: [MQTT Protocol](#mqtt-protocol)

:small_blue_diamond: [Application Topology](#application-topology)

:small_blue_diamond: [Raspberry Pi](#raspberry-pi)

  - [Install and run the Mosquitto MQTT Broker](#install-and-run-the-mosquitto-mqtt-broker)

  - [Install and run the Node-RED](#install-and-run-the-node-red)

:small_blue_diamond: [Wiring](#wiring)

:small_blue_diamond: [Results](#results)

***

## Project Description
This is an M2M (machine to machine) project that connects an Arduino UNO and an ESP32. The leds connected to the Arduino signal the status of the sensor connected to the ESP32, and similarly, the leds connected to the ESP32 signal the status of the sensor connected to the Arduino.
This cross-logic was configured in a very simple way, using function nodes in the Node-RED flows.
For communication, the AURT and MQTT protocols were used.

***

## UART Protocol
A universal asynchronous receiver-transmitter (UART) can refer to the protocol or the hardware, and as the name says, it is an asynchronous serial communication. A UART is used for full-duplex serial communication between devices equipped with this technology.
Data transfer is done bit by bit, using a wire to send and a wire to receive. To be successful in communication, the parameters of the devices must match, such as baud-rate, data bits, parity and stop-bit.
The simplicity of the application, makes its use very common in systems that do not require high speed communication.

***

## MQTT Protocol
MQTT is a messaging protocol for TCP/IP networks.
It is simple and light. Its basic architecture consists of broker and clients. The message exchange scheme is based on the Publish-Subscribe model.

Version 3.1.1 documentation:
http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html

***

## Application Topology

![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/topology.jpg)

The cycle starts in the Python application:

I- Python application:
- publishes an initial message in the topic "esp32/led"

II- ESP32:
- receives the message from the broker, of the subscribed topic (esp32/led)
- deals with the message, turning the corresponding led on or off
- reads the pressure and temperature sensor
- publishes in the topics "esp32/press" and "esp32/temp", the values of pressure and temperature

III- Node-RED:
- shows the pressure and temperature on the dashboard
- classifies the temperature value
- publish a temperature status message to the "arduino/led" topic

IV- Python application:
- receives the status message from the broker, of the subscribed topic (arduino/led)
- writes on the serial port, a status message, in the form of a byte

V- Arduino
- read the serial port byte
- deals with the received byte, turning the corresponding led on or off
- reads the distance sensor
- writes on the serial port, the distance values

VI- Python application:
- read the distance data from the serial port
- publish distance data in the topic "arduino/distance"

VII- RED-node:
- shows the distance on the dashboard
- classifies the distance value
- posts a distance status message to the topic "esp32 / led"

- returns to point II and continues the cycle

This is the simplest way to explain the cycle, but because it is a full-duplex communication, the devices send and receive data simultaneously.

***

## Raspberry Pi
Raspberry Pi is a series of small computers, which basically connects to a monitor, a keyboard and a mouse. There are several models, varying the available resources and performance.
It is developed in the United Kingdom by the Raspberry Pi Foundation.
In this application, Raspberry Pi 4 Model B with Raspbian operating system (based on Debian) was used. Learn more at https://www.raspberrypi.org/help/

On the Raspberry Pi, will be running the Mosquitto MQTT broker, Node-RED and the Python application. Follow the next instructions.

### Install and run the Mosquitto MQTT Broker
See how to install and run the Mosquitto on repository https://github.com/MrFMach/Mosquitto-Broker-RaspberryPi

### Install and run the Node-RED
See how to install and run the Node-RED on page https://nodered.org/docs/getting-started/raspberrypi

These are our flows and dashboard:

![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/flows.png)

![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/dashboard.png)

***

### Run the Python Application
If not have Python 3 in your Raspberry, see how to install in https://www.raspberrypi.org/documentation/linux/software/python.md. I use 3.7 version.
Install the Paho MQTT library. See how in https://pypi.org/project/paho-mqtt/
Install the Serial library. See how in https://pypi.org/project/pyserial/

Make the download and run "RPi-MQTT-Serial.py"

```
python3 RPi-MQTT-Serial.py
```

## Wiring

The wiring is simple, the only observation is the Arduino Tx terminal, becouse your voltage is 5V and Raspberry Pi serial port is 3,3V. So was needed a voltage divider. I use three 1k5 resistors, but can to be one 3k3 and one 1k5 resitors, for example.

![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/fritzing1.png)

***

## Results
![](https://github.com/MrFMach/M2M-Arduino-ESP32-NodeRED/blob/main/media/gif.gif)

***

Thank you!

#### Fabio Machado
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/fabio-machado-b932a476/)](https://www.linkedin.com/in/fabio-machado-b932a476/)

:computer:  Computer Engeneering  | :zap: Electronic  | :brazil:  Brazil

##### " cooperating, we'll go far " :rocket:
