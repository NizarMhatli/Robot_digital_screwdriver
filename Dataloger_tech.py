
import csv
import sys
from datetime import datetime
import time
from Newtonconvertor import converter


def Dataloger(SES,puredata,puredata1,lad_sta,SYS):
    csv_columns   = ['Time', 'Right sensor values', 'Left sensor values','R1','R2','R3','R4','R5','R6','R7','R8',
                     'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8',
                     'Grip Position', 'Robot State', 'Robot joint positions',
                      'Total product count','Total good product count','Bad product count','Gripper use number','Screw Tool use number '
                     ]
    dict_data = []
    csv_file =  "datalog.csv"
    while True:
            time.sleep(2)
            if  lad_sta[2] != 0:
                break
            while SES[10] == 1:
                if SES[1] != 0 or lad_sta[2]  != 0 :
                    break
                with open("robot.csv", newline='') as f:
                    reader = csv.reader(f)
                    joint = list(reader)

                if len(joint) > 0: g = joint[1]
                else: g = ['0','0']
                dict_data.append({'Time': str(datetime.now())
                                ,'Right sensor values': (converter(puredata))
                                ,'Left sensor values': (converter(puredata1)),
                                  'R1' : puredata[0]
                                 , 'R2' : puredata[1]
                                 , 'R3' : puredata[2]
                                 , 'R4': puredata[3]
                                 , 'R5': puredata[4]
                                 , 'R6': puredata[5]
                                 , 'R7': puredata[6]
                                 , 'R8': puredata[7],
                                  'L1': puredata1[0]
                                 , 'L2': puredata1[1]
                                 , 'L3': puredata1[2]
                                 , 'L4': puredata1[3]
                                 , 'L5': puredata1[4]
                                 , 'L6': puredata1[5]
                                 , 'L7': puredata1[6]
                                 , 'L8': puredata1[7]

                                     ,'Grip Position': SES[9],'Robot State': SES[0],'Robot joint positions': g[1],
                                  'Total product count': SYS[2],'Total good product count':SYS[3],'Bad product count':SYS[4],
                                  'Gripper use number': SYS[9], 'Screw Tool use number ': SYS[10]
                                  })
                with open(csv_file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in dict_data:
                        writer.writerow(data)