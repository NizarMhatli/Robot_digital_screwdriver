import csv
def joint_list_creat():
    with open("robot.csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    joint_data = [[0,0], [0,0], [0,0]]
    j,j1,j2,j3,j4,j5,J0str, J1str, J2str, J3str, J4str, J5str, J0, J1, J2, J3, J4, J5=0,0,0,0,0,0,'', '', '', '', '', '', [], [], [], [], [], []
    ja,ja1,ja2,ja3,ja4,ja5,Ja0str, Ja1str, Ja2str, Ja3str, Ja4str, Ja5str, Ja0, Ja1, Ja2, Ja3, Ja4, Ja5=0,0,0,0,0,0,'', '', '', '', '', '', [], [], [], [], [], []
    jc, jc1, jc2, jc3, jc4, jc5, Jc0str, Jc1str, Jc2str, Jc3str, Jc4str, Jc5str, Jc0, Jc1, Jc2, Jc3, Jc4, Jc5 = 0, 0, 0, 0, 0, 0, '', '', '', '', '', '', [], [], [], [], [], []
    if len(data) > 0:
        g = data[1]
        joint_data[0] = data[2]
        joint_data[1] = data[3]
        joint_data[2] = data[4]
        Robot_joints = g[1]
        Joint_amp = data[5][1]
        current = data[6]
        cart_cor = data[7][1]
    else:
        g = ['0', '0']
        Robot_joints = [0, 0, 0, 0, 0, 0]
        Joint_amp = [0, 0, 0, 0, 0, 0]
        cart_cor = [0, 0, 0, 0, 0, 0]
    ###########################################################
    for i in range(1,(len(Robot_joints)-1)):
        if Robot_joints[i] == ',':
            j = i
            break
        J0.append(Robot_joints[i])
    for a in range(j+1,(len(Robot_joints)-1)):
        if Robot_joints[a] == ',':
            j1 = a
            break
        J1.append(Robot_joints[a])
    for b in range(j1+1,(len(Robot_joints)-1)):
        if Robot_joints[b] == ',':
            j2 = b
            break
        J2.append(Robot_joints[b])
    for c in range(j2+1,(len(Robot_joints)-1)):
        if Robot_joints[c] == ',':
            j3 = c
            break
        J3.append(Robot_joints[c])
    for d in range(j3+1,(len(Robot_joints)-1)):
        if Robot_joints[d] == ',':
            j4 = d
            break
        J4.append(Robot_joints[d])
    for e in range(j4+1,(len(Robot_joints)-1)):
        if Robot_joints[e] == ',':
            j5 = e
            break
        J5.append(Robot_joints[e])
############################################################################################

    for i in range(0,len(J0)):J0str = J0str + str(J0[i])
    for i in range(1,len(J1)):J1str = J1str +str(J1[i])
    for i in range(1,len(J2)):J2str = J2str +str(J2[i])
    for i in range(1,len(J3)):J3str = J3str +str(J3[i])
    for i in range(1,len(J4)):J4str = J4str +str(J4[i])
    for i in range(1,len(J5)):J5str = J5str +str(J5[i])
    joint_list = [float(J0str),float(J1str),float(J2str),float(J3str),float(J4str),float(J5str)]
    ###############################################################################################
###################################################################################################################
    for i in range(1, (len(Joint_amp) - 1)):
        if Joint_amp[i] == ',':
            ja = i
            break
        Ja0.append(Joint_amp[i])
    for a in range(ja + 1, (len(Joint_amp) - 1)):
        if Joint_amp[a] == ',':
            ja1 = a
            break
        Ja1.append(Joint_amp[a])
    for b in range(ja1 + 1, (len(Joint_amp) - 1)):
        if Joint_amp[b] == ',':
            ja2 = b
            break
        Ja2.append(Joint_amp[b])
    for c in range(ja2 + 1, (len(Joint_amp) - 1)):
        if Joint_amp[c] == ',':
            ja3 = c
            break
        Ja3.append(Joint_amp[c])
    for d in range(ja3 + 1, (len(Joint_amp) - 1)):
        if Joint_amp[d] == ',':
            ja4 = d
            break
        Ja4.append(Joint_amp[d])
    for e in range(ja4 + 1, (len(Joint_amp) - 1)):
        if Joint_amp[e] == ',':
            ja5 = e
            break
        Ja5.append(Joint_amp[e])
        ############################################################################################

    for i in range(0, len(Ja0)): Ja0str = Ja0str + str(Ja0[i])
    for i in range(1, len(Ja1)): Ja1str = Ja1str + str(Ja1[i])
    for i in range(1, len(Ja2)): Ja2str = Ja2str + str(Ja2[i])
    for i in range(1, len(Ja3)): Ja3str = Ja3str + str(Ja3[i])
    for i in range(1, len(Ja4)): Ja4str = Ja4str + str(Ja4[i])
    for i in range(1, len(Ja5)): Ja5str = Ja5str + str(Ja5[i])
    joint_amp_data = [float(Ja0str), float(Ja1str), float(Ja2str), float(Ja3str), float(Ja4str), float(Ja5str)]
####################################################################################################################################
####################################################################################################################################

    for i in range(1, (len(cart_cor) - 1)):
        if cart_cor[i] == ',':
            jc = i
            break
        Jc0.append(cart_cor[i])
    for a in range(jc + 1, (len(cart_cor) - 1)):
        if cart_cor[a] == ',':
            jc1 = a
            break
        Jc1.append(cart_cor[a])
    for b in range(jc1 + 1, (len(cart_cor) - 1)):
        if cart_cor[b] == ',':
            jc2 = b
            break
        Jc2.append(cart_cor[b])
    for c in range(jc2 + 1, (len(cart_cor) - 1)):
        if cart_cor[c] == ',':
            jc3 = c
            break
        Jc3.append(cart_cor[c])
    for d in range(jc3 + 1, (len(cart_cor) - 1)):
        if cart_cor[d] == ',':
            jc4 = d
            break
        Jc4.append(cart_cor[d])
    for e in range(jc4 + 1, (len(cart_cor) - 1)):
        if cart_cor[e] == ',':
            jc5 = e
            break
        Jc5.append(cart_cor[e])
        ############################################################################################

    for i in range(0, len(Jc0)): Jc0str = Jc0str + str(Jc0[i])
    for i in range(1, len(Jc1)): Jc1str = Jc1str + str(Jc1[i])
    for i in range(1, len(Jc2)): Jc2str = Jc2str + str(Jc2[i])
    for i in range(1, len(Jc3)): Jc3str = Jc3str + str(Jc3[i])
    for i in range(1, len(Jc4)): Jc4str = Jc4str + str(Jc4[i])
    for i in range(1, len(Jc5)): Jc5str = Jc5str + str(Jc5[i])
    cart_cor_data = [float(Jc0str), float(Jc1str), float(Jc2str), float(Jc3str), float(Jc4str), float(Jc5str)]

######################################################################################################################################
######################################################################################################################################
    return (joint_list,joint_data,joint_amp_data,cart_cor_data,current)