import glob
import serial.tools.list_ports
from sys import platform


def Port_detector(Port,SES):
    while SES[1]==0:
        port = glob.glob('/dev/tty[A-Za-z]*')
        port1 = []
        activeport2, activeport, activeport1 = 'F', 'F', 'F'
        for i in range(0, len(port)):
            if 'ttyUSB' in port[i]:
                port1.append(port[i])
        if len(port1) == 1: activeport = port1[0]
        if len(port1) >= 3: activeport,activeport1, activeport2 = port1[0],port1[1],port1[2]
        if len(port1) == 2: activeport,activeport1 = port1[0],port1[1]
        Port[0],Port[1],Port[2] = activeport.replace('/dev/', ''),activeport1.replace('/dev/', ''),activeport2.replace('/dev/', '')
        if SES[1] != 0:
            break


def Port_setter(port1):
        print(platform)
        if platform == 'win32':
            conne = [port.device for port in serial.tools.list_ports.comports()]
            for i in range(0,len(conne)):
                port1[i]=conne[i]

        else:
            port = glob.glob('/dev/tty[A-Za-z]*')
            for i in range(0, len(port)):
                if 'ttyUSB' in port[i]:
                    port1[i] = port[i]
        return (port1)
