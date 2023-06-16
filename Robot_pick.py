import time
import serial
from crc_math import command_creat
from robot_control import robot_line
from PRO_FUSE_SOFT import  PRO_DATA_IN,PRO_SCREW_in,PRO_SCREW_out,Z_Homing,PRO_DATA_IN2,UUID_get
import timeit
from aphyt import omron
from robot_line import grip_check
from test_line_robot import wait_for_robot
import sys
def tim(f):
    time.sleep(f)
def tim1(f):
    time.sleep(f)
def robot_controler(PORT,SES,con_sta,lad_sta,SYS,SCE1,SCE2,Robot_car_data):
    t = 0
    f = 0
    g = 0
    f1 = 0
    cond = 0
    AT=0
    CT = 0
    ERT = 0
    mega = 0
    SES[5] = 160
    SES[5] = 250
    SES[6] = 250
    eip_instance = omron.n_series.NSeriesEIP()
    eip_instance.connect_explicit('192.168.251.1')
    eip_instance.register_session()
    eip_instance.update_variable_dictionary()
    UUID = UUID_get()
    while True:
        reply = eip_instance.write_variable('handng', False)
        cv2 = eip_instance.read_variable('cv2st')
        if str(eip_instance.read_variable('START_PB')) == 'True':
            lad_sta[0] = 1
            SES[10] = 1

        g = 0
        if cv2 == True:
            while SES[10] == 1:
                    SES[27] = 1
                    if SES[1] != 0 or lad_sta[1] != 0: break
                    ser = serial.Serial(port=PORT[2], baudrate=115200, parity=serial.PARITY_NONE,
                                         stopbits=serial.STOPBITS_ONE,
                                         bytesize=serial.EIGHTBITS, timeout=1)
                    con_sta[2] = 1
                    con_sta[5] = 1
                    time.sleep(2)
                    SES[9], SES[0] = 0, "gripper set"
                    if SES[25] == 0:
                        mega = 0
                    if SES[25] == 1:
                        mega = 10
                    if g ==0:
                        ######## Gripper tool
                        try:
                            Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
                        except:
                            break
                        ######### drill tool
                        try:
                            Tool_sensor2 = eip_instance.read_variable('t2')
                        except:
                            break
                        f = (372 - 1 < Robot_car_data[0] < 372 + 1) and (239 - 1 < Robot_car_data[1] < 239 + 1) \
                            and (600 - 1 < Robot_car_data[2] < 600 + 1) and (0 - 1 < Robot_car_data[5] < 0 + 1)
                        f1 = (-67.4 - 1 < Robot_car_data[0] < -67.4 + 1) and (452.5 - 1 < Robot_car_data[1] < 452.5+ 1) \
                            and (287 - 2 < Robot_car_data[2] < 287 + 2) and (-90.5 - 1 < Robot_car_data[5] < -90.5 + 1)
                        f2 = (58 - 1 < Robot_car_data[0] < 58 + 1) and (486 - 1 < Robot_car_data[1] < 486 + 1) \
                             and (297 - 1 < Robot_car_data[2] < 297 + 1) and (89.5 - 1 < Robot_car_data[5] < 89.5 + 1)
                        if f != True and f1 != True and f2 != True:
                            if Tool_sensor1 == False and Tool_sensor2 == True:
                                # recover from drill
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([366.5, 424.4, 600, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([57, 452.5, 600, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([-67.4, 452.5, 600, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                               # if SES[1] != 0 or lad_sta[1] != 0: break
                                f = wait_for_robot(Robot_car_data, [-67.4, 452.5, 286, -180, 0, -90.5])
                                try:
                                  reply = eip_instance.write_variable('tol', False)
                                  reply = eip_instance.write_variable('toolu', False)
                                  reply = eip_instance.write_variable('tol', True)
                                except:
                                    break
                                robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                               # if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                                #if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                               # if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                                f = wait_for_robot(Robot_car_data, [58, 486, 297, -180, 0, 89.5])
                                try:
                                    reply = eip_instance.write_variable('tol', False)
                                    reply = eip_instance.write_variable('toolu', False)
                                    reply = eip_instance.write_variable('toolu', True)
                                except:
                                    break
                                robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                               # if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                            elif Tool_sensor1 == True and Tool_sensor2 == False:
                                # recover from gripper
                                try:
                                    reply = eip_instance.write_variable('tol', False)
                                    reply = eip_instance.write_variable('toolu', False)
                                    reply = eip_instance.write_variable('toolu', True)
                                except:
                                    break
                                tim(1)
                                robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                             #   if SES[1] != 0 or lad_sta[1] != 0: break
                            elif Tool_sensor1 == False and Tool_sensor2 == False:
                                # no tool
                                robot_line([58, 350, 600, -180, 0, 89.5], 1, 5)
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 400, -180, 0, 89.5], 1, 5)
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)
                              #  if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)
                                f = wait_for_robot(Robot_car_data, [58, 486, 297, -180, 0, 89.5])
                                try:
                                    reply = eip_instance.write_variable('tol', False)
                                    reply = eip_instance.write_variable('toolu', False)
                                    reply = eip_instance.write_variable('toolu', True)
                                except:
                                    break
                                robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                             #   if SES[1] != 0 or lad_sta[1] != 0: break
                                robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                        if f1 == True:
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('tol', True)
                            except:
                                break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data, [58, 486, 297, -180, 0, 89.5])
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('toolu', True)
                            except:
                                break
                            robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot upTool_sensor2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                        if f2 == True:
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('toolu', True)
                            except:
                                break
                            robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                    g=1
                    #f = wait_for_robot(Robot_car_data, [372, 239, 600, -180, 0, 0])
                    ####################################
                    start = timeit.default_timer()
                    start_pre = timeit.default_timer()
                    ser.write(command_creat(220, 250, 250))
                    SES[9] = 220
                    cycle_start_time = time.time()
                    try:
                        reply = eip_instance.write_variable('Condi', 0)
                        time.sleep(0.1)
                        reply = eip_instance.write_variable('Condi', 2)
                        time.sleep(0.1)
                    except:
                        break
                    f = f+1
                    SES[20] = f
                    stop_pre = timeit.default_timer()
                    SYS[12] = stop_pre - start_pre

                    ############################################PICK UP#####################################
                    #########move from base#################
                    con_sta[3] = 1
                    SES[0] = "base point"
                    SES[15] = 'GRIPPER'
                    SYS[9] =   SYS[9] + 1
                    try:
                        reply = eip_instance.write_variable('Grip_use_C', str(SYS[9]))
                    except:
                        break
                    start_machine = timeit.default_timer()
                    robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                  #  if SES[1] != 0 or lad_sta[1] != 0: break
                    print('here4')
                    f = wait_for_robot(Robot_car_data,[372, 239, 600, -180, 0, 0])
                    ser.write(command_creat(0, 250, 250))
                    time.sleep(0.5)
                    SES[9] = 0
                    try:
                        reply = eip_instance.write_variable('Grip_use_C', str(SYS[9]))
                    except:
                        break
                    robot_line([372, 239, 398, -180, 0, 0], 1, 5)  # Move to pick zone 4
                    SES[9] = 200
                    # if SES[1] != 0 or lad_sta[1] != 0: break
                    f = wait_for_robot(Robot_car_data,[372, 239, 398, -180, 0, 0])
                    ser.write(command_creat(200, int(SES[5]), int(SES[6])))


                    grip = grip_check(ser)
                    if grip == 'ok':
                        #####################################################MOVE TO DROP#######################################
                        SES[9], SES[0]  = int(SES[5]),"pickup succsesful"
                        ser.write(command_creat(int(SES[9]), int(SES[5]), int(SES[6])))
                        SES[0] = "pickup "
                        time.sleep(0.5)
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([372, 239, 450, -180, 0, 0], 1, 5)
                        SES[0] = "drop point"
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([375, 485, 450, -180, 0, 0], 1, 5)
                        SES[0] = "drop point"
                                #####################################################Drop#########################################
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([375,485,400,-180,0,0],1,5)
                        SES[0] = "drop"
                        SES[9] = 0
                        hndng = eip_instance.read_variable('handng')
                        if hndng == True:
                            time.sleep(2)
                        f = wait_for_robot(Robot_car_data,[375,485,400,-180,0,0] )
                        ser.write( command_creat(int(SES[9]), int(SES[5]), int(SES[6])))
                        SES[0] = "drop"
                        ######################################################RETURN TO BASE####################################
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([368,486,600,-180,0,0],1,5)      # new return tool 1
                        SES[0] = "Tool change"
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58,486,600,-180,0,89.5],1,5)      # new return tool 2
                        SES[0] = "Return to Tool base "
                    #    if SES[1] != 0 or lad_sta[1] != 0: break
                        f = wait_for_robot(Robot_car_data, [58,486,600,-180,0,89.5])
                        ser.write(command_creat(220, 250, 250))
                        SES[9] = 220
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # return tool 2
                        SES[0] = "Return to Tool base"
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # Gripper drop
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'FREETOOL'
                        f = wait_for_robot(Robot_car_data,[58, 486, 297, -180, 0, 89.5] )
                        try:
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('tol', True)
                        except:
                            break
                        SES[15] = '0'
                        SES[0] = "unlock  Tool base"
                    #    if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Change tool 2
                    #    if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 400, -180, 0, 89.5], 1, 5)  # Change tool 2
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 449, 500, -180, 0, 0], 1, 5)  # Change tool 3 ############
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # Change tool 3 ############
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "move to new Tool base"
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Change tool 4
                   #     if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 287, -180, 0, 269.5], 0.01, 5)  # Change tool 6
                    #    if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'LOCKTOOL'
                        f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 287, -180, 0, -90.5] )
                        try:
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('toolu', True)
                        except:
                            break
                        SES[15] = 'SCREW'
                        SYS[10] =  SYS[10] + 1
                        try:
                            reply = eip_instance.write_variable('Dri_use_C', str( SYS[10]))
                        except:
                            break
                        SES[0] = "lock screw Tool "
                        SES[0] = "move to screw location "
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # screw  2
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # screw  2
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([366.5+mega, 400, 500, -180, 0.4, 269.5], 1, 5)  # screw  2
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([366.5+mega, 424, 270, -180, 0.4, 269.5], 1, 5)  # screw  5
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "screw out"
                        con_sta[7] = 1
                        f = wait_for_robot(Robot_car_data,[366.3+mega, 424.2, 270, -180, 0.4, -90.5] )
                        screw_data = PRO_SCREW_out(UUID)
                        if screw_data not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([366.5, 424, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                           # if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('tol', True)
                            except:
                                break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data, [58, 486, 297, -180, 0, 89.5])
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('toolu', True)
                            except:
                                break
                            robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            try:
                                reply = eip_instance.write_variable('Er_S_T', str(ERT))
                                SYS[4] = SYS[4] + 1
                                reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                                SYS[2] = SYS[3] + SYS[4]
                                reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                                reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                                reply = eip_instance.write_variable('handng', True)
                            except:
                                break
                            time.sleep(2)
                            ################################################################

                            break
                        con_sta[7] = 0
                        robot_line([366.5+mega, 424, 270, -180, 0.4, 269.5], 1, 5)  # screw out  1
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        con_sta[6] = 1
                        f = wait_for_robot(Robot_car_data,[366.3+mega, 424.2, 270, -180, 0.4, -90.5] )
                        screw_data1 = PRO_SCREW_in(UUID)
                        if screw_data1 not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                            robot_line([368, 394.5, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('tol', True)
                            except:
                                break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                           # if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                           # if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data, [58, 486, 297, -180, 0, 89.5])
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('toolu', True)
                            except:
                                break
                            robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                           # if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                           # if SES[1] != 0 or lad_sta[1] != 0: break


                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            try:
                                reply = eip_instance.write_variable('Er_S_T', str(ERT))
                                SYS[4] = SYS[4] + 1
                                reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                                SYS[2] = SYS[3] + SYS[4]
                                reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                                reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                                reply = eip_instance.write_variable('handng', True)
                            except:
                                break
                            break
                                        ################################################################

                            break
                        PRO_DATA_IN(eip_instance,UUID)
                        con_sta[6] = 0
                                    ####################################
                        SES[0] = "screw in"
                        robot_line([366.5+mega, 394, 270, -180, 0.4, 269.5], 1, 5)  # screw out  2
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "screw out"
                        con_sta[7] = 1
                        f = wait_for_robot(Robot_car_data,[366.3+mega, 394.4, 270, -180, 0.4, -90.5] )
                        screw_data2 = PRO_SCREW_out(UUID)
                        if screw_data2 not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                            robot_line([366.5, 394.4, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('tol', True)
                            except:
                                break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data, [58, 486, 297, -180, 0, 89.5])
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('toolu', True)
                            except:
                                break
                            robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            try:
                                reply = eip_instance.write_variable('Er_S_T', str(ERT))
                                SYS[4] = SYS[4] + 1
                                reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                                SYS[2] = SYS[3] + SYS[4]
                                reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                                reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                                reply = eip_instance.write_variable('handng', True)
                            except:
                                break
                            time.sleep(2)
                            ################################################################
                            break
                        con_sta[7] = 0
                        robot_line([366.5+mega, 394, 270, -180, 0.4, 269.5], 1, 5)  # screw out  2
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "screw out"
                        con_sta[6] = 1
                        f = wait_for_robot(Robot_car_data,[366.3+mega, 394.4, 270, -180, 0.4, -90.5] )
                        screw_data3 = PRO_SCREW_in(UUID)
                        if screw_data3 not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                            robot_line([366.5, 394.4, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('tol', True)
                            except:
                                break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data, [58, 486, 297, -180, 0, 89.5])
                            try:
                                reply = eip_instance.write_variable('tol', False)
                                reply = eip_instance.write_variable('toolu', False)
                                reply = eip_instance.write_variable('toolu', True)
                            except:
                                break
                            robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            try:
                                reply = eip_instance.write_variable('Er_S_T', str(ERT))
                                SYS[4] = SYS[4] + 1
                                reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                                SYS[2] = SYS[3] + SYS[4]
                                reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                                reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                                reply = eip_instance.write_variable('handng', True)
                                time.sleep(2)
                            except:
                                break
                            break
                        PRO_DATA_IN2(eip_instance,UUID)
                        con_sta[6] = 0
                        tim1(SES[24])
                        ####################################
                        SES[0] = "screw in"
                        ##############Change back tool#################
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([366.5+mega, 394.2, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "return to tool base"
                        robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'FREETOOL'
                        f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                        try:
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('tol', True)
                        except:
                            break
                        SES[15] = '0'
                        SES[0] = "unlock screw tool"
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "move to gripper tool"
                        robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'LOCKTOOL'
                        f = wait_for_robot(Robot_car_data,[58, 486, 297, -180, 0, 89.5] )
                        try:
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('toolu', True)
                        except:
                            break
                        SES[15] = 'GRIPPER'
                        SYS[9] =  SYS[9] + 1
                        try:
                            reply = eip_instance.write_variable('Grip_use_C', str(SYS[9]))
                        except:
                            break
                        SES[0] = " lock gripper"
                      #  if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 483, 600, -180, 0, 0], 1, 5)  # Move robot up
                       # if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "move to drop location"
                        robot_line([375, 486, 600, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        f = wait_for_robot(Robot_car_data,[375, 486, 600, -180, 0, 0] )
                        ser.write(command_creat(0, 250, 250))
                        time.sleep(0.5)
                        SES[9] = 0
                        robot_line([375, 484.5, 600, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                     #   if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "pick up object"
                        robot_line([375,484.5,398,-180,0,0],1,5)  #Move robot to pick point 2
                        SES[9] = 200
                        f = wait_for_robot(Robot_car_data,[375,484.5,398,-180,0,0] )

                        ser.write(command_creat( SES[9] , int(SES[5]), int(SES[6])))
                        grip = grip_check(ser)
                        if grip == 'ok':
                            SES[9] = 200
                            SES[9], SES[0] = int(SES[5]), "pickup succsesful"
                            SES[0] = "pickup "
                            robot_line([375, 484.5, 450, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                        #    if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 450, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            SES[0] = "move to pick up location"
                            robot_line([372, 239, 400, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            SES[0] = "drop"
                            f = wait_for_robot(Robot_car_data,[372, 239, 400, -180, 0, 0] )
                            hndng = eip_instance.read_variable('handng')
                            if hndng == True:
                                time.sleep(2)
                            ser.write(command_creat(0, 250, 250))
                            SES[9] = 0
                            ####################return to base##################################
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # return to base 1
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            try:
                                reply = eip_instance.write_variable('Condi', 0)
                                time.sleep(0.1)
                                reply = eip_instance.write_variable('Condi', 1)
                                time.sleep(0.1)
                            except:
                                break
                           # if SES[1] != 0 or lad_sta[1] != 0: break
                            SES[0] = "return to tool base"
                            ser.write(command_creat(220, 250, 250))
                            SES[9] = 220
                            stop_machine = timeit.default_timer()
                            start_post = timeit.default_timer()
                            stop_post = timeit.default_timer()
                            SYS[13] = stop_post - start_post
                            SES[9] = 0
                            stop = timeit.default_timer()
                            CT = stop - start ###################
                            print(CT)
                            try:
                                reply = eip_instance.write_variable('Condi', 0)
                                time.sleep(0.1)
                                reply = eip_instance.write_variable('Condi', 1)
                                time.sleep(0.1)
                                SYS[3] = SYS[3] + 1
                                AT = AT + CT ################################
                                SYS[2] =  SYS[3] +  SYS[4]
                                reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                                reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                                reply = eip_instance.write_variable('ToBaPrCo', str( SYS[4]))
                                reply = eip_instance.write_variable('Cy_T', str(int(CT)))
                                reply = eip_instance.write_variable('Ma_T', str(int(stop_machine - start_machine)))
                                reply = eip_instance.write_variable('AuMo_T', str(int(AT)))
                            except:
                                break
                            time.sleep(1)
                            SES[9] = 0
                        else:
                            start_err = timeit.default_timer()
                            robot_line([368, 486, 600, -180, 0, 0], 1, 5)  # return tool 1
                            ######################################################RETURN TO BASE####################################
                            robot_line([368, 486, 600, -180, 0, 0], 1, 5)  # new return tool 1
                            SES[0] = " return"
                          #  if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 600, -180, 0, 0], 1, 5)
                            SES[0] = " base "
                         #   if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            try:
                                reply = eip_instance.write_variable('Er_S_T', str(ERT))
                                SYS[4]=  SYS[4] + 1
                                reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                                SYS[2] = SYS[3] + SYS[4]
                                reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                                reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                                reply = eip_instance.write_variable('handng', True)
                            except:
                                break
                            break
                            ############################################### return from drop 2
                    else:
                        start_err = timeit.default_timer()
                        robot_line([375, 240, 600, -180, 0, 0], 1, 5)  # return to base 1
                        stop_err = timeit.default_timer()
                        ERT = stop_err - start_err
                        try:
                            reply = eip_instance.write_variable('Er_S_T', str(ERT))
                            SYS[4] = SYS[4] + 1
                            reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                            SYS[2] = SYS[3] + SYS[4]
                            reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                            reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                            reply = eip_instance.write_variable('handng', True)
                        except:
                            break
                        break
                        ############################################## return from drop 1
            if SES[1] != 0 or lad_sta[1] != 0:
                con_sta[2] = 0
                con_sta[3] = 0
                SES[27] = 0

