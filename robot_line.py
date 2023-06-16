from robot_control import robot_line
from PRO_FUSE_SOFT import  PRO_SCREW_pik,PRO_SCREW_in,PRO_SCREW_out,Z_Homing
import serial
import time
from crc_math import command_creat
from aphyt import omron
import time
lad_sta = [0,0]
#  X +    , robot goes closer tp nizar
#  x -    , robot goes further back from nizar
#  y +    , robot goes goes to nizars right
#  y -    , robot goes goes to nizars left
#  z +    , robot goes goes up
#  z -    , robot goes goes down
#  A +    , robot goes turns right
#  A -    , robot goes turns left

def tim():
    time.sleep(1)


def grip_check(ser):
    data_raw = list(ser.readline())
    time.sleep(0.001)
    ser.write(b'\x09\x03\x07\xD0\x00\x03\x04\x0E')
    time.sleep(0.001)
    data_raw = list(ser.readline())
    if data_raw[3] == 185:
            grip = 'ok'
    else:
            grip = 'not ok'
    return (grip)

def rec_ov():
    eip_instance = omron.n_series.NSeriesEIP()
    eip_instance.connect_explicit('192.168.251.1')
    eip_instance.register_session()
    eip_instance.update_variable_dictionary()
    ######## Gripper tool
    Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
    ######### drill tool
    Tool_sensor2 = eip_instance.read_variable('t2')
    if Tool_sensor1 == False and Tool_sensor2 == True:
        robot_line([366.5, 424.4, 600, -180, 0.4, 269.5], 1, 5)  # Return screw 1
        tim()
        robot_line([57, 452.5, 600, -180, 0, 269.5], 1, 5)  # Return screw 2.5
        tim()
        robot_line([-67.4, 452.5, 600, -180, 0, 269.5], 1, 5)  # Return screw 2.5
        tim()
        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
        tim()
        robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
        tim()
        tim()
        reply = eip_instance.write_variable('tol', False)
        reply = eip_instance.write_variable('toolu', False)
        reply = eip_instance.write_variable('tol', True)
        tim()
        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
        tim()
        robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
        tim()
        robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
        tim()
        robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
        tim()
        robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
        tim()
        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
        tim()
        robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
        tim()
        tim()
        reply = eip_instance.write_variable('tol', False)
        reply = eip_instance.write_variable('toolu', False)
        reply = eip_instance.write_variable('toolu', True)
        tim()
        robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
        tim()
        robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
        tim()
        robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
        tim()

def res_gri(PORT):
    ser = serial.Serial(port=PORT[2], baudrate=115200, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)
    eip_instance = omron.n_series.NSeriesEIP()
    eip_instance.connect_explicit('192.168.251.1')
    eip_instance.register_session()
    eip_instance.update_variable_dictionary()
    ######## Gripper tool
    Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
    ######### drill tool
    Tool_sensor2 = eip_instance.read_variable('t2')
    if Tool_sensor1 == True and Tool_sensor2 == False:
        tim()
        robot_line([58, 350, 600, -180, 0, 89.5], 1, 5)
        tim()
        ser.write(command_creat(220, 250, 250))
        tim()
        robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)
        tim()
        robot_line([58, 486, 400, -180, 0, 89.5], 1, 5)
        tim()
        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)
        tim()
        robot_line([58, 486, 297, -180, 0, 89.5], 1, 5)
        tim()
        tim()
        tim()
        reply = eip_instance.write_variable('tol', False)
        reply = eip_instance.write_variable('toolu', False)
        reply = eip_instance.write_variable('toolu', True)
        tim()
        robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
        tim()
        robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
def gri_set(PORT):
    ser = serial.Serial(port=PORT[2], baudrate=115200, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)
    ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x00\x00\x00\x00\x00\x00\x73\x30')
    data_raw = ser.readline()
    time.sleep(0.01)
    ser.write(b'\x09\x03\x07\xD0\x00\x01\x85\xCF')
    data_raw = ser.readline()
    time.sleep(0.01)
    ####################################
    ser.write(b'\x09\x10\x03\xE8\x00\x03\x06\x09\x00\x00\x00\xFF\xFF\x72\x19')
def gri_op(PORT,f):
    ser = serial.Serial(port=PORT[2], baudrate=115200, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)
    ser.write(command_creat(f, 250, 250))

def final_rec():
    try:
        eip_instance = omron.n_series.NSeriesEIP()
        eip_instance.connect_explicit('192.168.251.1')
        eip_instance.register_session()
        eip_instance.update_variable_dictionary()
        ######## Gripper tool
        Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
        ######### drill tool
        Tool_sensor2 = eip_instance.read_variable('t2')
        if Tool_sensor1 == False and Tool_sensor2 == True:
            # recover from drill
            tim()
            robot_line([366.5, 424.4, 600, -180, 0.4, 269.5], 1, 5)  # Return screw 1
            tim()
            robot_line([57, 452.5, 600, -180, 0, 269.5], 1, 5)  # Return screw 2.5
            tim()
            robot_line([-67.4, 452.5, 600, -180, 0, 269.5], 1, 5)  # Return screw 2.5
            tim()
            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
            tim()
            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
            tim()
            tim()
            reply = eip_instance.write_variable('tol', False)
            reply = eip_instance.write_variable('toolu', False)
            reply = eip_instance.write_variable('tol', True)
            tim()
            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
            tim()
            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
            tim()
            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
            tim()
            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
            tim()
            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
            tim()
            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
            tim()
            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
            tim()
            tim()
            reply = eip_instance.write_variable('tol', False)
            reply = eip_instance.write_variable('toolu', False)
            reply = eip_instance.write_variable('toolu', True)
            tim()
            robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
            tim()
            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
            tim()
            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
            tim()
        elif Tool_sensor1 == True and Tool_sensor2 == False:
            # recover from gripper
            reply = eip_instance.write_variable('tol', False)
            reply = eip_instance.write_variable('toolu', False)
            reply = eip_instance.write_variable('toolu', True)
            tim()
            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
            tim()
            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
        elif Tool_sensor1 == False and Tool_sensor2 == False:
            # no tool
            tim()
            robot_line([58, 350, 600, -180, 0, 89.5], 1, 5)
            tim()
            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)
            tim()
            robot_line([58, 486, 400, -180, 0, 89.5], 1, 5)
            tim()
            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)
            tim()
            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)
            tim()
            tim()
            reply = eip_instance.write_variable('tol', False)
            reply = eip_instance.write_variable('toolu', False)
            reply = eip_instance.write_variable('toolu', True)
            tim()
            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
            tim()
            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
    except:
        time.sleep(2)
        print('try again')
    '''
    ######## Gripper tool
    Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
    ######### drill tool
    Tool_sensor2 = eip_instance.read_variable('t2')
    if Tool_sensor1 == False and Tool_sensor2 == False:
        tim()
        robot_line([58, 350, 600, -180, 0, 89.5], 1, 5)
        tim()
        tim()
        robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)
        tim()
        robot_line([58, 486, 400, -180, 0, 89.5], 1, 5)
        tim()
        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)
        tim()
        robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)
        tim()
    '''

#376
#robot_line([366.3, 424.2, 270, -180, 0.4, 269.5], 1, 5)  # screw  5