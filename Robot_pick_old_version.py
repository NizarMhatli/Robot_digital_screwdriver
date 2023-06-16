import time
import serial
from crc_math import command_creat
from robot_control import robot_line
from PRO_FUSE_SOFT import  PRO_DATA_IN,PRO_SCREW_in,PRO_SCREW_out,Z_Homing,PRO_DATA_IN2
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
    cond = 0
    AT=0
    CT = 0
    ERT = 0
    eip_instance = omron.n_series.NSeriesEIP()
    eip_instance.connect_explicit('192.168.251.1')
    eip_instance.register_session()
    eip_instance.update_variable_dictionary()
    while True:

            while SES[10] == 1:

                    ser = serial.Serial(port=PORT[2], baudrate=115200, parity=serial.PARITY_NONE,
                                         stopbits=serial.STOPBITS_ONE,
                                         bytesize=serial.EIGHTBITS, timeout=1)
                    con_sta[2] = 1
                    con_sta[5] = 1
                    SES[9], SES[0] = 0, "gripper set"
                    ####################################
                    start = timeit.default_timer()
                    start_pre = timeit.default_timer()
                    ser.write(command_creat(220, 250, 250))
                    SES[9] = 220
                    reply = eip_instance.write_variable('Grip_spe', str(250))
                    reply = eip_instance.write_variable('Grip_Fo', str(250))
                    reply = eip_instance.write_variable('Gri', str(SES[9]))
                    cycle_start_time = time.time()
                    reply = eip_instance.write_variable('Condi', 0)
                    time.sleep(0.1)
                    reply = eip_instance.write_variable('Condi', 2)
                    time.sleep(0.1)
                    f = f+1
                    SES[20] = f
                    stop_pre = timeit.default_timer()
                    SYS[12] = stop_pre - start_pre

                    ############################################PICK UP#####################################
                    #########move from base#################
                    con_sta[3] = 1
                    SES[0] = "base point"
                    robot_line([58, 486, 297, -180, 0, 89.5], 1, 5)  # base point
                    if SES[1] != 0 or lad_sta[1] != 0: break
                    #SES[16] = 'LOCKTOOL'
                    f = wait_for_robot(Robot_car_data,[58, 486, 297, -180, 0, 89.5])
                    reply = eip_instance.write_variable('tol', False)
                    reply = eip_instance.write_variable('toolu', False)
                    reply = eip_instance.write_variable('toolu', True)
                    SES[15] = 'GRIPPER'
                    SYS[9] =   SYS[9] + 1
                    reply = eip_instance.write_variable('Grip_use_C', str(SYS[9]))
                    start_machine = timeit.default_timer()
                    robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                    if SES[1] != 0 or lad_sta[1] != 0: break
                    robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # Move robot up
                    if SES[1] != 0 or lad_sta[1] != 0: break
                    robot_line([372, 239, 600, -180, 0, 0], 1, 5)  # Move to pick zone 1
                    if SES[1] != 0 or lad_sta[1] != 0: break
                    f = wait_for_robot(Robot_car_data,[372, 239, 600, -180, 0, 0])
                    ser.write(command_creat(0, 250, 250))
                    time.sleep(0.5)
                    SES[9] = 0
                    reply = eip_instance.write_variable('Gri', str(SES[9]))
                    robot_line([372, 239, 398, -180, 0, 0], 1, 5)  # Move to pick zone 4
                    if SES[1] != 0 or lad_sta[1] != 0: break
                    f = wait_for_robot(Robot_car_data,[372, 239, 398, -180, 0, 0])
                    ser.write(command_creat(200, int(SES[5]), int(SES[6])))
                    SES[9] = 200
                    reply = eip_instance.write_variable('Gri', str(SES[9]))
                    grip = grip_check(ser)
                    if grip == 'ok':

                        #####################################################MOVE TO DROP#######################################
                        SES[9], SES[0]  = int(SES[5]),"pickup succsesful"
                        reply = eip_instance.write_variable('Gri', str(SES[9]))
                        ser.write(command_creat(int(SES[9]), int(SES[5]), int(SES[6])))
                        SES[0] = "pickup "
                        time.sleep(0.5)
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([372, 239, 450, -180, 0, 0], 1, 5)
                        SES[0] = "drop point"
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([375, 485, 450, -180, 0, 0], 1, 5)
                        SES[0] = "drop point"
                                #####################################################Drop#########################################
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([375,485,400,-180,0,0],1,5)
                        SES[0] = "drop"
                        SES[9] = 0
                        f = wait_for_robot(Robot_car_data,[375,485,400,-180,0,0] )
                        reply = eip_instance.write_variable('Gri', str(SES[9]))
                        ser.write( command_creat(int(SES[9]), int(SES[5]), int(SES[6])))
                        SES[0] = "drop"
                        ######################################################RETURN TO BASE####################################
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([368,486,600,-180,0,0],1,5)      # new return tool 1
                        SES[0] = "Tool change"
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58,486,600,-180,0,89.5],1,5)      # new return tool 2
                        SES[0] = "Return to Tool base "
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        f = wait_for_robot(Robot_car_data, [58,486,600,-180,0,89.5])
                        ser.write(command_creat(220, 250, 250))
                        SES[9] = 220
                        reply = eip_instance.write_variable('Gri', str(SES[9]))
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # return tool 2
                        SES[0] = "Return to Tool base"
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # Gripper drop
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'FREETOOL'
                        f = wait_for_robot(Robot_car_data,[58, 486, 297, -180, 0, 89.5] )
                        reply = eip_instance.write_variable('tol', False)
                        reply = eip_instance.write_variable('toolu', False)
                        reply = eip_instance.write_variable('tol', True)
                        SES[15] = '0'
                        SES[0] = "unlock  Tool base"
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Change tool 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 400, -180, 0, 89.5], 1, 5)  # Change tool 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 449, 500, -180, 0, 0], 1, 5)  # Change tool 3 ############
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # Change tool 3 ############
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "move to new Tool base"
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Change tool 4
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Change tool 6
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'LOCKTOOL'
                        f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                        reply = eip_instance.write_variable('tol', False)
                        reply = eip_instance.write_variable('toolu', False)
                        reply = eip_instance.write_variable('toolu', True)
                        SES[15] = 'SCREW'
                        SYS[10] =  SYS[10] + 1
                        reply = eip_instance.write_variable('Dri_use_C', str( SYS[10]))
                        SES[0] = "lock screw Tool "
                        SES[0] = "move to screw location "
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # screw  2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # screw  2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([366.3, 400, 500, -180, 0.4, 269.5], 1, 5)  # screw  2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([366.3, 424.2, 270, -180, 0.4, 269.5], 1, 5)  # screw  5
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "screw out"
                        con_sta[7] = 1
                        f = wait_for_robot(Robot_car_data,[366.3, 424.2, 270, -180, 0.4, -90.5] )
                        screw_data = PRO_SCREW_out()
                        if screw_data not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([366.3, 424.2, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('tol', True)
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            reply = eip_instance.write_variable('Er_S_T', str(ERT))
                            SYS[4] = SYS[4] + 1
                            reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                            SYS[2] = SYS[3] + SYS[4]
                            reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                            reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                            ################################################################

                            break
                        con_sta[7] = 0
                        robot_line([366.3, 424.2, 270, -180, 0.4, 269.5], 1, 5)  # screw out  1
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        con_sta[6] = 1
                        f = wait_for_robot(Robot_car_data,[366.3, 424.2, 270, -180, 0.4, -90.5] )
                        screw_data1 = PRO_SCREW_in()
                        if screw_data1 not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                            robot_line([368, 394.5, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('tol', True)
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            reply = eip_instance.write_variable('Er_S_T', str(ERT))
                            SYS[4] = SYS[4] + 1
                            reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                            SYS[2] = SYS[3] + SYS[4]
                            reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                            reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                                        ################################################################

                            break
                        PRO_DATA_IN(eip_instance)
                        con_sta[6] = 0
                                    ####################################
                        SES[0] = "screw in"
                        robot_line([366.3, 394.4, 270, -180, 0.4, 269.5], 1, 5)  # screw out  2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "screw out"
                        con_sta[7] = 1
                        f = wait_for_robot(Robot_car_data,[366.3, 394.4, 270, -180, 0.4, -90.5] )
                        screw_data2 = PRO_SCREW_out()
                        if screw_data2 not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                            robot_line([366.5, 394.4, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('tol', True)
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            reply = eip_instance.write_variable('Er_S_T', str(ERT))
                            SYS[4] = SYS[4] + 1
                            reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                            SYS[2] = SYS[3] + SYS[4]
                            reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                            reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                            ################################################################
                            break
                        con_sta[7] = 0
                        robot_line([366.3, 394.4, 270, -180, 0.4, 269.5], 1, 5)  # screw out  2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "screw out"
                        con_sta[6] = 1
                        f = wait_for_robot(Robot_car_data,[366.3, 394.4, 270, -180, 0.4, -90.5] )
                        screw_data3 = PRO_SCREW_in()
                        if screw_data3 not in (b'\xff',b'\x01'):
                            start_err = timeit.default_timer()
                            SYS[4] = SYS[4] + 1
                            con_sta[3] = 0
                            lad_sta[4] = 1
                            lad_sta[3] = 0
                            lad_sta[1] = 1
                            robot_line([366.5, 394.4, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([57, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                            reply = eip_instance.write_variable('tol', False)
                            reply = eip_instance.write_variable('toolu', False)
                            reply = eip_instance.write_variable('tol', True)
                            robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 269.5], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            reply = eip_instance.write_variable('Er_S_T', str(ERT))
                            SYS[4] = SYS[4] + 1
                            reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                            SYS[2] = SYS[3] + SYS[4]
                            reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                            reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                            break
                        PRO_DATA_IN2(eip_instance)
                        con_sta[6] = 0
                        tim1(SES[24])
                        ####################################
                        SES[0] = "screw in"
                        ##############Change back tool#################
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([366.5, 394.4, 500, -180, 0.4, 269.5], 1, 5)  # Return screw 1
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "return to tool base"
                        robot_line([-67.4, 400, 500, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 1, 5)  # Return screw 2.5
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 286, -180, 0, 269.5], 0.01, 5)  # Return screw 3
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'FREETOOL'
                        f = wait_for_robot(Robot_car_data,[-67.4, 452.5, 286, -180, 0, -90.5] )
                        reply = eip_instance.write_variable('tol', False)
                        reply = eip_instance.write_variable('toolu', False)
                        reply = eip_instance.write_variable('tol', True)
                        SES[15] = '0'
                        SES[0] = "unlock screw tool"
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 300, -180, 0, 269.5], 0.01, 5)  # get gripper again 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 452.5, 500, -180, 0, 0], 1, 5)  # get gripper again 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([-67.4, 451, 500, -180, 0, 89.5], 1, 5)  # get gripper again 3
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "move to gripper tool"
                        robot_line([58, 486, 500, -180, 0, 89.5], 1, 5)  # get gripper again 4
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # get gripper again 4
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # get gripper again 6
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        #SES[16] = 'LOCKTOOL'
                        f = wait_for_robot(Robot_car_data,[58, 486, 297, -180, 0, 89.5] )
                        reply = eip_instance.write_variable('tol', False)
                        reply = eip_instance.write_variable('toolu', False)
                        reply = eip_instance.write_variable('toolu', True)
                        SES[15] = 'GRIPPER'
                        SYS[9] =  SYS[9] + 1
                        reply = eip_instance.write_variable('Grip_use_C', str(SYS[9]))
                        SES[0] = " lock gripper"
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 0.01, 5)  # Move robot up
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 600, -180, 0, 0], 1, 5)  # Move robot up
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "move to drop location"
                        robot_line([375, 486, 600, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        f = wait_for_robot(Robot_car_data,[375, 486, 600, -180, 0, 0] )
                        ser.write(command_creat(0, 250, 250))
                        time.sleep(0.5)
                        SES[9] = 0
                        reply = eip_instance.write_variable('Gri', str(SES[9]))
                        robot_line([375, 484.5, 600, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        SES[0] = "pick up object"
                        robot_line([375,484.5,398,-180,0,0],1,5)  #Move robot to pick point 2
                        f = wait_for_robot(Robot_car_data,[375,484.5,398,-180,0,0] )
                        ser.write(command_creat(200, int(SES[5]), int(SES[6])))
                        grip = grip_check(ser)
                        if grip == 'ok':
                            SES[9] = 200
                            SES[9], SES[0] = int(SES[5]), "pickup succsesful"
                            reply = eip_instance.write_variable('Gri', str(SES[9]))
                            SES[0] = "pickup "
                            robot_line([375, 484.5, 450, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([372, 239, 450, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            SES[0] = "move to pick up location"
                            robot_line([372, 239, 400, -180, 0, 0], 1, 5)  # Move robot to pick point 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            SES[0] = "drop"
                            f = wait_for_robot(Robot_car_data,[372, 239, 400, -180, 0, 0] )
                            ser.write(command_creat(0, 250, 250))
                            SES[9] = 0
                            reply = eip_instance.write_variable('Gri', str(SES[9]))
                            ####################return to base##################################
                            robot_line([375, 240, 600, -180, 0, 0], 1, 5)  # return to base 1
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0,  89.5], 1, 5)  # return to base 2
                            f = wait_for_robot(Robot_car_data, [58, 486, 600, -180, 0,  89.5])
                            reply = eip_instance.write_variable('Condi', 0)
                            time.sleep(0.1)
                            reply = eip_instance.write_variable('Condi', 1)
                            time.sleep(0.1)
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[58, 486, 600, -180, 0,  89.5] )
                            SES[0] = "return to tool base"
                            ser.write(command_creat(220, 250, 250))
                            SES[9] = 220
                            reply = eip_instance.write_variable('Gri', str(SES[9]))
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # return to base 3
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # return to base 2
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_machine = timeit.default_timer()
                            start_post = timeit.default_timer()
                            stop_post = timeit.default_timer()
                            SYS[13] = stop_post - start_post
                            SES[9] = 0
                            stop = timeit.default_timer()
                            CT = stop - start ###################
                            print(CT)
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
                            time.sleep(1)
                            break
                            SES[9] = 0
                        else:
                            start_err = timeit.default_timer()
                            robot_line([368, 486, 600, -180, 0, 0], 1, 5)  # return tool 1
                            ######################################################RETURN TO BASE####################################
                            robot_line([368, 486, 600, -180, 0, 0], 1, 5)  # new return tool 1
                            SES[0] = "Tool change"
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 600, -180, 0, 0], 1, 5)  # new return tool 2
                            SES[0] = "Return to Tool base "
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            f = wait_for_robot(Robot_car_data,[58, 486, 600, -180, 0, 0] )
                            print(f)
                            ser.write(command_creat(220, 250, 250))
                            SES[9] = 220
                            reply = eip_instance.write_variable('Gri', str(SES[9]))
                            robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # return tool 2
                            SES[0] = "Return to Tool base"
                            robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # return tool 2
                            SES[0] = "Return to Tool base"
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # Gripper drop
                            if SES[1] != 0 or lad_sta[1] != 0: break
                            stop_err = timeit.default_timer()
                            ERT = stop_err - start_err
                            reply = eip_instance.write_variable('Er_S_T', str(ERT))
                            SYS[4]=  SYS[4] + 1
                            reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                            SYS[2] = SYS[3] + SYS[4]
                            reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                            reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                            break
                            ############################################### return from drop 2
                    else:
                        start_err = timeit.default_timer()
                        robot_line([375, 240, 600, -180, 0, 0], 1, 5)  # return to base 1
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 240, 600, -180, 0, 0], 1, 5)  # return to base 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        f = wait_for_robot(Robot_car_data,[58, 240, 600, -180, 0, 0] )
                        print(f)
                        reply = eip_instance.write_variable('Condi', 0)
                        time.sleep(0.1)
                        reply = eip_instance.write_variable('Condi', 1)
                        time.sleep(0.1)
                        SES[0] = "return to tool base"
                        robot_line([58, 240, 600, -180, 0, 89.5], 1, 5)  # return to base 2
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        f = wait_for_robot(Robot_car_data,[58, 240, 600, -180, 0, 89.5] )
                        print(f)
                        ser.write(command_creat(220, 250, 250))
                        SES[9] = 220
                        reply = eip_instance.write_variable('Gri', str(SES[9]))
                        robot_line([58, 486, 600, -180, 0, 89.5], 1, 5)  # return to base 3
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 310, -180, 0, 89.5], 1, 5)  # return to base 3
                        if SES[1] != 0 or lad_sta[1] != 0: break
                        robot_line([58, 486, 297, -180, 0, 89.5], 0.01, 5)  # return to base 2
                        stop_err = timeit.default_timer()
                        ERT = stop_err - start_err
                        reply = eip_instance.write_variable('Er_S_T', str(ERT))
                        SYS[4] = SYS[4] + 1
                        reply = eip_instance.write_variable('ToBaPrCo', str(SYS[4]))
                        SYS[2] = SYS[3] + SYS[4]
                        reply = eip_instance.write_variable('ToPrCo', str(SYS[2]))
                        reply = eip_instance.write_variable('ToGoPrCo', str(SYS[3]))
                        break
                        ############################################## return from drop 1
