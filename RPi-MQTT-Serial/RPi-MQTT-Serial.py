
import serial
import paho.mqtt.client as mqttClient
import threading

event = threading.Event()

ser = serial.Serial(                          #start serial
    "/dev/ttyS0",
    baudrate = 4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2)

def on_connect(client, userdata, flags, rc):  #callback 
    if rc == 0:
        print("Connected to broker")
        global Connected                      #Use global variable
        Connected = True                      #Signal connection 
    else:
        print("Connection failed")

def on_message(client, userdata, message):    # mqtt message receive
    messageled = message.payload
    print (messageled)
    if (messageled == b'R'):
        ser.write('R'.encode('ascii'))
    elif (messageled == b'Y'):
        ser.write('Y'.encode('ascii'))
    elif (messageled == b'O'):
        ser.write('O'.encode('ascii'))
    else:
        print ("Invalid message")

Connected = False                                  #global variable for the state of the connection
 
broker_address= "192.168.0.13"
port = 1883
user = "mrfmach"
password = "mosquitto"
                                                   #init broker
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message

client.connect(broker_address, port=port)          #connect to broker
client.loop_start()                                #start the loop

while Connected != True:                           #Wait for connection
    event.wait(0.2)

client.subscribe("arduino/led")
client.publish("esp32/led", "o")                   #publish to start the cycle

try:
    while True:
        readArdu = ser.readline()
        print(readArdu)
        
        event.wait(0.15)                            #cycle time  
        client.publish("arduino/distance", readArdu)
        
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()