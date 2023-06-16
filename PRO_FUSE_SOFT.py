
#!/usr/bin/env python3
import socket
import json
from aphyt import omron
###################### SET UP Functions###########################
def UUID_get():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('192.168.20.99', 5000))
            s.send(bytes([0]))
            data = s.recv(1024)
            s.close()
        except:
            print('UUID cant be accessed')
            data = b'\x00'
    if data == b'\xfe':
        print('UUID not accessed correctly')
    return(data)




def Z_Homing (UUID):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('192.168.20.99', 5000))
            s.send(UUID +b'\04')
            data3 = s.recv(1024)
            s.close()
        except:
            print('the command was not excuted')
            data = b'\x00'
            data3 =  b'\x00'
        if data3 == b'\xff':
            print('the command was not excuted correctly')
        elif data3 == b'\xfd':
            print('the command sent is not correct')
    return (data3)



#################### ACTION FUNCTIONS#####################################

def PRO_SCREW_pik():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       try:
                if data == b'\x01':
                    s.connect(('192.168.20.99', 5000))
                    s.send(UUID +b'\01' + b'\00\00\00\01')
                    data1 = s.recv(1024)
                    s.close()
                else:
                    print('No command was sent')
                    data1 = b'\x00'
       except:
           print('the command was not excuted')
       if data1 == b'\xff':
               print('the command was not excuted correctly')
       elif data1 == b'\xfd':
               print('the command sent is not correct')


def PRO_SCREW_in(UUID):
    data = Z_Homing(UUID)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\01' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
                data1 = b'\x00'
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')
    return (data1)



def PRO_SCREW_out(UUID):
    data = Z_Homing(UUID)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\03' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
                data1 =  b'\x00'
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')

        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)
################################ ACTION AND RETURN FUNCTIONS######################################################

def PRO_SCREW_pik_RE():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       try:
                if data == b'\x01':
                    s.connect(('192.168.20.99', 5000))
                    s.send(UUID +b'\01' + b'\00\00\00\01')
                    data1 = s.recv(1024)
                    s.close()
                else:
                    print('No command was sent')
       except:
           print('the command was not excuted')
       if data1 == b'\xff':
               print('the command was not excuted correctly')
       elif data1 == b'\xfd':
               print('the command sent is not correct')

    return (data1)

def PRO_SCREW_in_RE():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\02' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)


def PRO_SCREW_out_RE():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\03' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)

###################################PARAMETER SETTING########################

def PRO_PARA_IN(UUID):
    data = Z_Homing(UUID)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + bytes([0x0c]) + b'\00\00\00\01')
                print(UUID + bytes([0x0c]) + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)




def PRO_CANCEL_C():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5100))
                s.send(UUID + b'\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)


def PRO_DATA_IN(eip_instance,UUID):
    data = Z_Homing(UUID)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + bytes([0x1b]) + b'\00\00\00\01'+ b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
                data1 = b'\xff'
        except:
            print('the command was not excuted')
            data1 = b'\xff'
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')
        try:
            data1 = str(data1).replace("b'", '')
            data1 = str(data1).replace("x00", '')
            data1 = str(data1).replace("xff", '')
            data1 = str(data1).replace("xf", '')
            data1 = str(data1).replace("\\\\", '')
            data1 = data1[1:]
            data1 = str(data1).replace('{"Result List":[{"Result Element":', '')
            data1 = str(data1).replace("}]}", '')
            data1 = str(data1).replace("'", '')
            data1 = json.loads(data1)
            reply = eip_instance.write_variable('ADT1', str(data1["Date"]))
            reply = eip_instance.write_variable('RPG_no', str(int(data1["Number"])))
            reply = eip_instance.write_variable('TC1', str(int(data1["Turn Count"] * 10)))
            reply = eip_instance.write_variable('MaxTV', str(int(data1["Max Torque"] * 10)))
            reply = eip_instance.write_variable('TT', str(int(data1["Time"] * 10)))
            reply = eip_instance.write_variable('ZEP', str(int(data1["Z End Position"] * 100)))
            reply = eip_instance.write_variable('ZCP', str(int(data1["Z Current"] * 100)))
            print(int(data1["Operation Result"]))
            reply = eip_instance.write_variable('R1', True if int(data1["Operation Result"]) == 0 else False)
        except:
            print('the command was not excuted')
            data1 = 'none'
    return ()


def PRO_DATA_IN2(eip_instance,UUID):
    data = Z_Homing(UUID)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + bytes([0x1b]) + b'\00\00\00\01'+ b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
                data1 = b'\xff'
        except:
            print('the command was not excuted')
            data1 = b'\xff'
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')
        try:
            data1 = str(data1).replace("b'", '')
            data1 = str(data1).replace("x00", '')
            data1 = str(data1).replace("xff", '')
            data1 = str(data1).replace("xf", '')
            data1 = str(data1).replace("\\\\", '')
            data1 = data1[1:]
            data1 = str(data1).replace('{"Result List":[{"Result Element":', '')
            data1 = str(data1).replace("}]}", '')
            data1 = str(data1).replace("'", '')
            data1 = json.loads(data1)
            reply = eip_instance.write_variable('ADT2', str(data1["Date"]))
            reply = eip_instance.write_variable('RPG_no2', str(int(data1["Number"])))
            reply = eip_instance.write_variable('TC2', str(int(data1["Turn Count"]*10)))
            reply = eip_instance.write_variable('MaxTV2', str(int(data1["Max Torque"]*10)))
            reply = eip_instance.write_variable('TT2', str(int(data1["Time"]*10)))
            reply = eip_instance.write_variable('ZEP2', str(int(data1["Z End Position"]*100)))
            reply = eip_instance.write_variable('ZCP2', str(int(data1["Z Current"]*100)))
            print(int(data1["Operation Result"]))
            reply = eip_instance.write_variable('R2', True if int(data1["Operation Result"]) == 0 else False)
        except:
            print('the command was not excuted')
            data1 = 'none'
    return ()
