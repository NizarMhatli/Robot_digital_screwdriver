import asyncio
import sys

import techmanpy
import csv
import time

async def move(poz,SP, TI):
   async with techmanpy.connect_sct(robot_ip='169.254.130.10') as conn:
      await conn.move_to_joint_angles_ptp(poz, SP, TI)
def robot(POZZ,SP, TI):
    asyncio.run(move(POZZ,SP,TI))

async def move_line(poz,SP, TI):
   async with techmanpy.connect_sct(robot_ip='169.254.130.10') as conn:
      await conn.move_to_point_line(poz, SP, TI)
def robot_line(POZZ,SP, TI):
    asyncio.run(move_line(POZZ,SP,TI))





def save_dictionary_to_csv(params_dict):
    with open("robot.csv", 'w') as file:
        writer = csv.writer(file)
        for parameter, value in params_dict.items():
            writer.writerow([parameter, value])
async def listen():
    async with techmanpy.connect_svr(robot_ip='169.254.130.10') as conn:
        conn.add_broadcast_callback(save_dictionary_to_csv)
        await conn.keep_alive()
def robotlog (SES,lad_sta):
    while True:
        try:
            time.sleep(2)
            if  lad_sta[2] != 0:
                break
            while SES[10] == 1:
                if SES[1] != 0 or lad_sta[2]  != 0 :
                    break
                try:
                    asyncio.run(listen())
                except:
                    exit()
        except:
            sys.exit()
