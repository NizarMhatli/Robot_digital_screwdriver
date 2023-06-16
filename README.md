# Robot powered industrial digital screwdriver machine with convyor: 

# Scope of the project: 
Personal project based around previous professional project, the goal is to showcase my industrial/robotic programming skils.
This package mainly uses python.
This software has both hardware control algorthims and human machine interface.
this project combines all the knowhow used in the previous pragramms used for Touchence sensors, digital screwdriver control software and Robotiq f2-85
gripper. (you can see all the different packages used in this profile)
Hardware used: 
Omron Cobot Techman robot: https://www.tm-robot.com/en/tm5-900/ 
Omron NX1 PLC: https://industrial.omron.eu/en/products/nx1
Robotiq f2-85: https://robotiq.com/products/2f85-140-adaptive-robot-gripper
PRO-FUSE digital screwdriver: https://www.hp-vanguard.com/products/2015101425/
Touchence pressure sensor: http://www.touchence.jp/en/products/cube03.html
Pascal Robot tool changer: https://www.pascaleng.co.jp/us/products/robot/robot_tool_changer/

#packages used: 
Robotic-gripper-with-haptic-feedback
PRO-FUSE-CONTROL
ROBOTIQ-python-manager
Touchence-python-GUI

# Libraries needed to run:
- pyserial 
- aphyt
- techmanpy
- asyncio
- matplotlib
- PySimpleGUI
- libscrc

# set up

just run pip install -r requirements.txt to install 

# Hardware connection set up linux 
check your lan cable location using the ifconfig command on the terminal 
if ifconfig is not istalled use this command to install it:

sudo apt install net-tools

set your network for the nx1:

sudo ifconfig network1  192.168.250.3 netmask 255.255.255.0

set your envierment for techman:

sudo ifconfig network2  169.254.130.3 netmask 255.255.255.0

set your envierment for PRO-FUSE: 

sudo ifconfig network3  192.168.20.99 netmask 255.255.255.0

Robotiq f2-85 and Touchence use serial usb ports
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

for PRO-FUSE follow same pattern.


# Run set up windows: 
Install needed drivers to access ports on windows you can find the derivers online according to the serial addapter 
for lan setup you go to internet adpter settings and set the IP adress 
for NX1 : 
![Capture_168](https://user-images.githubusercontent.com/47193436/143407626-0cece2a9-697a-412c-a5ee-eb2fbc32c4dc.PNG)
for Techman robot 
![Capture_169](https://user-images.githubusercontent.com/47193436/143407697-895f54a7-4dea-4780-9ac1-0c4aa80d5a33.PNG)

Same for PRO-FUSE just check the IP adress.

you can check if connection is set by using the ping IP adress command 

Robotiq f2-85 and Touchence use serial usb ports

Note: the conveyor and Tool changer are connected and controlled by the NX1 PLC.


#Features:

- Control screw in/out using the digital screwdriver.
- Control robot pick and place trajectory.
- control conveyor motion.
- control robot end effector tool using tool changer.
- collect data for robot motion, gripper sensors and product count.
- display sensor data in in HMi in different forms
- display machine and hardware statues
- manual control for each hardware part 
- reset hardware
- emergency and safety control 

# Process: 

To activate this programm after checking all the connections just run the main_app.py 

The HMI will appear: 

#HMI explain: 

