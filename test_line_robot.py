import time

def wait_for_robot(input_data, condi ):
    con = True

    while con == True:
         S = (condi[0] - 1 < input_data[0] < condi[0] + 1) and (condi[1] - 1 < input_data[1] < condi[1] + 1) \
            and (condi[2] - 1 < input_data[2] < condi[2] + 1) and (condi[5] - 1 < input_data[5] < condi[5] + 1)
         if  S == True:
            con = False
            re_wait = True
         #time.sleep(0.5)
    return(re_wait)

''''
 
 
 
 
 
 
 
 
 
 
'''