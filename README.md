# Techman-touchsense-
project created for the purpose  of research for pick/drop using touch sensors 

#This project objective: 
is to create an algorithm to control Techman collaborative robot to do pick and drop using touch sensor. also to back up and monitor the data input by the sensor in 3D shape figure. this project contains codes for : 
- sensor input  
- TCP robot/pc communication code  
- serial control for the gripper  
- Gui for the live feed 





#TODO list: 
- add input from EtherCat terminal to activate program with button press 
-  add alarm and error options


# Libraries needed to run:
- pyserial 
- aphyt
- techmanpy
- asyncio
- matplotlib
- PySimpleGUI
- libscrc



just run pip install -r requirements.txt to install 

# Run set up linux 
check your lan cable location using the ifconfig command on the terminal 
if ifconfig is not istalled use this command to install it:

sudo apt install net-tools

set your network for the nx1:

sudo ifconfig network1  192.168.250.3 netmask 255.255.255.0

set your envierment for techman:

sudo ifconfig network2  169.254.130.3 netmask 255.255.255.0

check the perrmission on the usb ports if its not open use this command:
chmod 666 /dev/ttyUSB(number of port)

example: chmod 66 /dev/ttyUSB0


to change the permission access permanatly use this command:

sudo usermod -a -G dialout K090 

you can set your network in the setting menu :

for NX1 :
![Capture_167](https://user-images.githubusercontent.com/47193436/143407255-c64c2549-872e-4c72-bfd3-1b27df492750.PNG)
for Techman robot :
![Capture_166](https://user-images.githubusercontent.com/47193436/143407333-a8c3b0e1-6b3d-43b7-946a-63a46416bf5c.PNG)
# Run set up windows: 
Install needed drivers to access ports on windows you can find the derivers online according to the serial addapter 
for lan setup you go to internet adpter settings and set the IP adress 
for NX1 : 
![Capture_168](https://user-images.githubusercontent.com/47193436/143407626-0cece2a9-697a-412c-a5ee-eb2fbc32c4dc.PNG)
for Techman robot 
![Capture_169](https://user-images.githubusercontent.com/47193436/143407697-895f54a7-4dea-4780-9ac1-0c4aa80d5a33.PNG)
you can check if connection is set by using the ping IP adress command 
