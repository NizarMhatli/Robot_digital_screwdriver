

import sys
import time

from PRO_FUSE_SOFT import  PRO_SCREW_pik,PRO_SCREW_in,PRO_SCREW_out,Z_Homing
import socket

def Screw_man(SES,con_sta,lad_sta):
    while True:
        try:

            while SES[27] == 0:
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.connect(('192.168.20.99', 5000))
                            time.sleep(1)
                            s.close()
                        con_sta[5] = 1
                        while SES[13] == 1 :
                            con_sta[6] = 1
                            PRO_SCREW_in()
                            SES[13] = 0
                            con_sta[6] = 0
                        while SES[14] == 1:
                            con_sta[7] = 1
                            PRO_SCREW_out()
                            SES[14] = 0
                            con_sta[7] = 0
                    except:
                        con_sta[5] = 0
                    if SES[27] != 0 or lad_sta[1]  != 0:
                        con_sta[5] = 0
                        break
        except:
            sys.exit()


