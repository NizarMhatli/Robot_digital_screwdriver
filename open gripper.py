import serial
import time
from crc_math import command_creat
from aphyt import omron
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout=1)
'''
ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x00\x00\x00\x00\x00\x00\x73\x30')
data_raw = ser.readline()
time.sleep(0.01)
ser.write(b'\x09\x03\x07\xD0\x00\x01\x85\xCF')
data_raw = ser.readline()
time.sleep(0.01)
####################################
ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x09\x00\x00\x00\xFF\xFF\x72\x19')
'''
ser.write(command_creat(220, 250, 250))

eip_instance = omron.n_series.NSeriesEIP()
eip_instance.connect_explicit('192.168.251.1')
eip_instance.register_session()
eip_instance.update_variable_dictionary()


se = 'EXIT'
if se ==  'EXIT':
    reply = eip_instance.write_variable('Condi', 0)
    time.sleep(0.1)
    reply = eip_instance.write_variable('Condi', 1)
    time.sleep(0.1)

if se ==  'ENTER':
    reply = eip_instance.write_variable('Condi', 0)
    time.sleep(0.1)
    reply = eip_instance.write_variable('Condi', 2)
    time.sleep(0.1)



