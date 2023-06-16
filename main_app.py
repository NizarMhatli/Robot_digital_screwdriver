import multiprocessing
from multiprocessing import freeze_support
from gui_create2 import gui1,Gui_figure,Gui_figure1,Gui_figure3,Gui_manual,gui_display
from sensor_input import sensormain,sensormain1
from Robot_pick import robot_controler
from Dataloger_tech import Dataloger
from robot_control import robotlog
from NX1Com import PlC_Com
from PRO_FUSE_MAN import Screw_man
import csv
state,ext,sensorDD,gri,sen,pos,Spe,Foc,fig,Grip_count,clos,clos1,ext1,SIN,SOUT,tool,counter,G_count,fulltime,cytime,fullcount,IAI,savt,timer1,timer2,screw2,manual,cycle,datad1,datad2,datad3 = '0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0',0,0,0,0,0,'0',0,0,0,0,0,0,0,0,0
activeport,activeport1,activeport2 = '/dev/sensor1','/dev/sensor2','/dev/gripperport'
rows = {}
if __name__ ==  '__main__':
    manager = multiprocessing.Manager()
    puredata = manager.list([0, 0, 0, 0, 0, 0, 0, 0])
    puredata1 = manager.list([0, 0, 0, 0, 0, 0, 0, 0])
    Robot_joints = manager.list([0, 0, 0, 0, 0, 0])
    Robot_car_data = manager.list([0, 0, 0, 0, 0, 0])
    Robot_data = manager.list([0, 0, 0])
    con_sta = manager.list([0,0,0,0,0,0,0,0])
    lad_sta = manager.list([0,0,0,0,0,0])
    PORT = manager.list([activeport,activeport1,activeport2])
    SES = manager.list([state,ext,sensorDD,gri,sen,pos,Spe,Foc,fig,Grip_count,clos,clos1,ext1,SIN,SOUT,tool,counter,G_count,fulltime,cytime,fullcount,IAI,savt,timer1,timer2,screw2,manual,cycle,datad1,datad2,datad3])
         #                0    1      2     3   4   5    6  7    8      9      10    11   12   13  14   15    16      17      18      19        20     21   22   23     24    25     26,    27     28     29     30
    with open("datalog.csv",'r' ) as f:
        for line in csv.DictReader(f,fieldnames=('Time', 'Right sensor values', 'Left sensor values',
                     'Grip Position', 'Robot State', 'Robot joint positions',
                      'Total product count','Total good product count','Bad product count','Gripper use number','Screw Tool use number ')):
            rows = line
    SYS =  manager.list([0,0,int(rows['Total product count']),int(rows['Total good product count']),int(rows['Bad product count']),'0',0,0,0,int(rows['Gripper use number']) if float(rows['Gripper use number']) <1000 else 0,int(rows['Screw Tool use number ']), 0, 0, 0])
   #                     1 2 3 4 5 6 7 8 9 10 11 12 13 14
    print(SYS[10])
    SCE1 = manager.list(['0',0,0,0,0,0,0,0])
    SCE2 = manager.list(['0',0,0,0,0,0,0,0])
    thread1 = multiprocessing.Process(target=gui1, args=[puredata, puredata1, PORT, SES, con_sta, lad_sta,SYS])
    thread3 = multiprocessing.Process(target=robot_controler, args=[PORT, SES, con_sta,lad_sta,SYS,SCE1,SCE2,Robot_car_data])
    thread2 = multiprocessing.Process(target=sensormain, args=[puredata, PORT, SES, con_sta,lad_sta,SYS])
    thread4 = multiprocessing.Process(target=sensormain1, args=[puredata1, PORT, SES, con_sta,lad_sta,SYS])
    thread5 = multiprocessing.Process(target=Gui_figure, args=[puredata, puredata1, SES,lad_sta])
    thread7 = multiprocessing.Process(target=robotlog, args=[SES,lad_sta])
    thread6 = multiprocessing.Process(target=Dataloger, args=[SES, puredata, puredata1,lad_sta,SYS])
    thread8 = multiprocessing.Process(target=PlC_Com, args=[SES, puredata, puredata1, con_sta, lad_sta,SYS,SCE1,SCE2,Robot_car_data])
    thread9 = multiprocessing.Process(target=Gui_figure1, args=[puredata, puredata1, SES,lad_sta])
    thread10 = multiprocessing.Process(target=Screw_man, args=[SES,con_sta,lad_sta])
    thread11 = multiprocessing.Process(target=Gui_figure3, args=[puredata,puredata1,SES,lad_sta])
    thread12 = multiprocessing.Process(target=Gui_manual, args=[SES, lad_sta,con_sta,PORT])
    thread13 = multiprocessing.Process(target=gui_display, args=[PORT,SES,con_sta,lad_sta])
    freeze_support()
    while True:
        try:
            if SES[1]==0 :
                    thread1.start()
                    thread2.start()
                    thread4.start()
                    thread3.start()
                    thread5.start()
                    thread7.start()
                    thread6.start()
                    thread8.start()
                    thread9.start()
                    thread10.start()
                    thread11.start()
                    thread12.start()
                    thread13.start()
                    thread3.join()
                    thread1.join()
                    thread2.join()
                    thread4.join()
                    thread5.join()
                    thread7.join()
                    thread6.join()
                    thread8.join()
                    thread9.join()
                    thread10.join()
                    thread11.join()
                    thread12.join()
                    thread13.join()
            else:
                    thread1.terminate()
                    thread2.terminate()
                    thread4.terminate()
                    thread3.terminate()
                    thread5.sterminate()
                    thread7.terminate()
                    thread6.terminate()
                    thread8.terminate()
                    thread9.terminate()
                    thread10.terminate()
                    thread11.terminate()
                    thread12.terminate()
                    thread13.terminate()
        except:
            thread1.terminate()
            thread2.terminate()
            thread4.terminate()
            thread3.terminate()
            thread5.terminate()
            thread7.terminate()
            thread6.terminate()
            thread8.terminate()
            thread9.terminate()
            thread10.terminate()
            thread11.terminate()
            thread12.terminate()
            thread13.terminate()
            break
            sys.exit()



# Grip_spe = SES[5]
# Grip_Fo = SES[6]
# data[2] = Rob_Mod = Robot_data[0]
# data[3] = Rob_Er = Robot_data[1]
# data[4] = Rob_Speed = Robot_data[2]
####################################################
#SYS[0] = Op_st
#SYS[1] = PrNu
#SYS[2] = ToPrCo
#SYS[3] =  ToGoPrCo
#SYS[4] = ToBaPrCo
#SYS[5] = ASI
#SYS[6] = Cy_T
#SYS[7] = Ma_T
#SYS[8] = AuMo_T
#SYS[9] = Er_S_T
#SYS[10] = Grip_use_C
#SYS[11] = Dri_use_C
#SYS[12] = Pre_T
#SYS[13] = Post_T
