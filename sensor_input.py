import sys
import timeit
from sensorread2 import sensorread
def sensormain(puredata,PORT,SES,con_sta,lad_sta,SYS):
    while True:
        try:
            while SES[10] == 1:
                    try:
                        puredata = sensorread(puredata, PORT[1])
                        puredata[4] = puredata[0]
                        puredata[5] = puredata[0]
                        #print('primeordial data', puredata[0],puredata[2])       #4/5 dead
                        con_sta[0] = 1
                    except:
                        con_sta[0] = 0
                    if SES[1] != 0 or lad_sta[2]  != 0:
                        con_sta[0] = 0
                        break

        except:
            SYS[5] = 'sensor connection error'
            SYS[9] = timeit.default_timer()
            sys.exit()



def sensormain1(puredata1,PORT,SES,con_sta,lad_sta,SYS):
    while True:
        try:
            while SES[10] == 1:
                    try:
                        puredata1 = sensorread(puredata1, PORT[0])
                        con_sta[1] = 1
                    except:
                        con_sta[1] = 0
                    if SES[1] != 0 or lad_sta[2]  != 0:
                        con_sta[0] = 0
                        break
        except:
            SYS[5] = 'sensor connection error'
            SYS[9] = timeit.default_timer()
            sys.exit()

