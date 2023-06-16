import serial.tools.list_ports


def Port_detector(Port,SES):
    while True:
        connected = [port.device for port in serial.tools.list_ports.comports()]

        if len(connected) >= 3:
            Port[0] ,Port[1],Port[2] = connected[0], connected[1] , connected[2]
        elif len(connected) == 2:
            Port[0] ,Port[1],Port[2] = connected[0], connected[1], ''
        elif len(connected) == 1:
            Port[0],Port[1],Port[2] = connected[0], '', ''
        else:
            Port[0] ,Port[1],Port[2] = '', '', ''

        if SES[1] != 0:
            break