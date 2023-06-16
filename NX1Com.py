from aphyt import omron
import time
from Newtonconvertor import converter
from string_to_list import joint_list_creat
import timeit
from random import randrange
def PlC_Com(SES,puredata, puredata1,con_sta,lad_sta,SYS,SCE1,SCE2,Robot_car_data):
    LS =['LS1','LS2','LS3','LS4','LS5','LS6','LS7','LS8']
    RS =['RS1','RS2','RS3','RS4','RS5','RS6','RS7','RS8']
    Jo =['RPoJ0','RPoj1','RPoj2','RPoj3','RPoj4','RPoj5']
    Ja = ['Rja0', 'Rja1', 'Rja2', 'Rja3', 'Rja4', 'Rja5']

    eip_instance = omron.n_series.NSeriesEIP()
    eip_instance.connect_explicit('192.168.251.1')
    eip_instance.register_session()
    eip_instance.update_variable_dictionary()
    while True:
        while True:
            try:
                        if lad_sta[4] == 1:
                            reply = eip_instance.write_variable('GREEN_Lamp', False)
                        if lad_sta[3] == 1:
                            reply = eip_instance.write_variable('GREEN_Lamp', True)
                            reply = eip_instance.write_variable('YELLOW_Lamp', False)
                            ################################input#####################################

                        if str(eip_instance.read_variable('STOP_PB')) == 'True':
                            lad_sta[1] = 1
                        i = 0
                        Robot_joints,joint_data,Joint_amp,cor_car_data,current = joint_list_creat()
                        for i in range(0,len(Robot_car_data)):
                            Robot_car_data[i] = cor_car_data[i]
                        for i in range(0,len(Joint_amp)):
                            Joint_amp[i] = float(current[1])/6 + randrange(5)/10
                    ############################GRIPPER#########################################
                        con_sta[4] = 1
                        ##############################Robot data #########################
                        reply = eip_instance.write_variable('Rob_Mod', str( int(joint_data[0][1])))
                        reply = eip_instance.write_variable('Rob_Er',str((int(float(joint_data[1][1])))) )
                        reply = eip_instance.write_variable('Rob_speed', str(int(float(joint_data[2][1]))))
                        ###########################SYStem data #########################################
                        reply = eip_instance.write_variable('Op_st', int(SYS[0]))  #  1 = system working 2 = system stopping  ok
                        SYS[1] = 'edgecross001'
                        reply = eip_instance.write_variable('PrNu', str(SYS[1])) # ok
                        reply = eip_instance.write_variable('ASI',  SYS[5])
                        reply = eip_instance.write_variable('Pre_T',str(SYS[12]))
                        reply = eip_instance.write_variable('Post_T',str(SYS[13]) )
                    ################################ROBOTJOINTS#####################################
                        for i in range(0,len(Robot_joints)):
                            reply = eip_instance.write_variable(Jo[i], str(Robot_joints[i]))
                            reply = eip_instance.write_variable(Ja[i], str(Joint_amp[i]))
                        for i in range(0,len(puredata)):
                            reply = eip_instance.write_variable(LS[i], puredata[i])
                            reply = eip_instance.write_variable(RS[i], puredata1[i])
                        reply = eip_instance.write_variable('Gri', str(SES[9]))
                        reply = eip_instance.write_variable('Grip_spe', str(250))
                        reply = eip_instance.write_variable('Grip_Fo', str(250))
                    ################################Screw Data#####################################

            except:
                break