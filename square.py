import numpy as np

def colorblind(size,color):
    if 6 <= size <= 7:
        c = color
    elif 5 <= size < 6:
        c = 'darkgreen'
    elif 4 <= size < 5:
        c = 'olive'
    elif 3 <= size < 4:
        c = 'gold'
    elif 2 <= size < 3:
        c = 'orange'
    elif 1 <= size < 2:
        c = 'orangered'
    elif 0 <= size < 1:
        c = 'tomato'
    elif  size < 0:
        c = 'red'
    else:
        c = color
    return (c)

def square_maker(ax,fig_agg,center,size,color):
    rep,i,rep1,rep2,rep3,k,rep4,j=[],0,[0,0,0],[],[],0,[0,0,0],0
    while i < len(center) :
        rep.append(np.linspace(center[i] - size[i] / 2, center[i] + size[i] / 2, num=10))
        i+=1
    rep1[0], rep4[0] = np.meshgrid(rep[1], rep[2])
    rep1[1], rep4[1] = np.meshgrid(rep[0], rep[2])
    rep1[2], rep4[2] = np.meshgrid(rep[0], rep[1])
    while k < len(rep1):
        rep2.append(np.ones_like(rep1[k]) * (center[k] - size[k] / 2))
        rep3.append(np.ones_like(rep1[k]) * (center[k] + size[k] / 2))
        k+=1
    p = colorblind(size[0],color)
    ax.plot_wireframe(rep3[0], rep1[0], rep4[0], color=p, rstride=1, cstride=1, alpha=0.6)
    ax.plot_wireframe( rep1[1], rep2[1], rep4[1], color='gray', rstride=1, cstride=1, alpha=0.6)
    ax.plot_wireframe( rep1[1], rep3[1], rep4[1], color='gray', rstride=1, cstride=1, alpha=0.6)
    return (ax, fig_agg)

def square_maker1(ax,fig_agg,center,size,color):
    rep, i, rep1, rep2, rep3, k, rep4, j = [], 0, [0, 0, 0], [], [], 0, [0, 0, 0], 0
    while i < len(center):
        rep.append(np.linspace(center[i] - size[i] / 2, center[i] + size[i] / 2, num=10))
        i += 1
    rep1[0], rep4[0] = np.meshgrid(rep[1], rep[2])
    rep1[1], rep4[1] = np.meshgrid(rep[0], rep[2])
    rep1[2], rep4[2] = np.meshgrid(rep[0], rep[1])
    while k < len(rep1):
        rep2.append(np.ones_like(rep1[k]) * (center[k] - size[k] / 2))
        rep3.append(np.ones_like(rep1[k]) * (center[k] + size[k] / 2))
        k += 1
    p = colorblind(size[0], color)
    ax.plot_wireframe(rep2[0], rep1[0], rep4[0], color=p, rstride=1, cstride=1, alpha=0.6)
    ax.plot_wireframe(rep1[1], rep2[1], rep4[1], color='gray', rstride=1, cstride=1, alpha=0.6)
    ax.plot_wireframe(rep1[1], rep3[1], rep4[1], color='gray', rstride=1, cstride=1, alpha=0.6)
    return (ax, fig_agg)


def DIS(ax,fig_agg,center,center1):
    ax.plot( [center[0][0],center1[0][0]], [0, 0], [0, 0], 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[1][0],center1[1][0]], [7.5, 7.5], [0, 0], 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[1][0], center[1][0]], [0, 7.5], [0, 0], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[1][0], center1[1][0]], [0, 7.5], [0, 0], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[2][0],center1[2][0]], [0, 0],[7.5, 7.5] , 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[0][0], center[2][0]], [0, 0], [0, 7.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[0][0], center1[2][0]], [0, 0], [0, 7.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[3][0],center1[3][0]], [7.5, 7.5], [7.5, 7.5], 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[1][0], center[3][0]], [0, 7.5], [7.5, 7.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[1][0], center[3][0]], [7.5, 7.5], [0, 7.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[1][0], center1[3][0]], [0, 7.5], [7.5, 7.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[1][0], center1[3][0]], [7.5, 7.5], [0, 7.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[4][0],center1[4][0]], [0, 0], [15, 15], 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[2][0], center[4][0]], [0, 0], [7.5, 15], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[2][0], center1[4][0]], [0, 0], [7.5, 15], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[5][0],center1[5][0]], [7.5, 7.5], [15, 15], 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[4][0], center[5][0]], [0, 7.5], [15, 15], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[4][0], center1[5][0]], [0, 7.5], [15, 15], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[3][0], center[5][0]], [7.5, 7.5], [7.5, 15], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[3][0], center1[5][0]], [7.5, 7.5], [7.5, 15], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[6][0],center1[6][0]], [0, 0], [22.5, 22.5], 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[4][0], center[6][0]], [0, 0], [15, 22.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[4][0], center1[6][0]], [0, 0], [15, 22.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[7][0],center1[7][0]], [7.5, 7.5], [22.5, 22.5], 'black', linewidth=2, label='Line 1',marker = 'o')
    ax.plot([center[5][0], center[7][0]], [7.5, 7.5], [15, 22.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[5][0], center1[7][0]], [7.5, 7.5], [15, 22.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center[7][0], center[6][0]], [0, 7.5], [22.5, 22.5], 'black', linewidth=2, label='Line 1', marker='o')
    ax.plot([center1[7][0], center1[6][0]], [0, 7.5], [22.5, 22.5], 'black', linewidth=2, label='Line 1', marker='o')

    return (ax, fig_agg)



def vecdef(ax,fig_agg,center,center1):
    if center[0][0] < -10.7:
        ax.quiver(center[0][0], center[0][1], center[0][2], center[0][0]/2, 0, 0, color='r')
    if center[1][0] < -10.7:
        ax.quiver(center[1][0], center[1][1], center[1][2], center[1][0]/2, 0, 0, color='r')
    if center[2][0] < -10.7:
        ax.quiver(center[2][0], center[2][1], center[2][2], center[2][0]/2, 0, 0, color='r')
    if center[3][0] < -10.7:
        ax.quiver(center[3][0], center[3][1], center[3][2], center[3][0]/2, 0, 0, color='r')
    if center[4][0] < -10.7:
        ax.quiver(center[4][0], center[4][1], center[4][2], center[4][0]/2, 0, 0, color='r')
    if center[5][0] < -10.7:
        ax.quiver(center[5][0], center[5][1], center[5][2], center[5][0]/2, 0, 0, color='r')
    if center[6][0] < -10.7:
        ax.quiver(center[6][0], center[6][1], center[6][2], center[6][0]/2, 0, 0, color='r')
    if center[7][0] < -10.7:
        ax.quiver(center[7][0], center[7][1], center[7][2], center[7][0]/2, 0, 0, color='r')

    if center1[0][0] > 10.7:
        ax.quiver(center1[0][0], center1[0][1], center1[0][2], center1[0][0]/2, 0, 0, color='r')
    if center1[1][0] > 10.7:
        ax.quiver(center1[1][0], center1[1][1], center1[1][2], center1[1][0]/2, 0, 0, color='r')
    if center1[2][0] > 10.7:
     ax.quiver(center1[2][0], center1[2][1], center1[2][2], center1[2][0]/2, 0, 0, color='r')
    if center1[3][0] > 10.7:
        ax.quiver(center1[3][0], center1[3][1], center1[3][2], center1[3][0]/2, 0, 0, color='r')
    if center1[4][0] > 10.7:
        ax.quiver(center1[4][0], center1[4][1], center1[4][2], center1[4][0]/2, 0, 0, color='r')
    if center1[5][0] > 10.7:
        ax.quiver(center1[5][0], center1[5][1], center1[5][2], center1[5][0]/2, 0, 0, color='r')
    if center1[6][0] > 10.7:
        ax.quiver(center1[6][0], center1[6][1], center1[6][2], center1[6][0]/2, 0, 0, color='r')
    if center1[7][0] > 10.7:
        ax.quiver(center1[7][0], center1[7][1], center1[7][2], center1[7][0]/2, 0, 0, color='r')


    return (ax, fig_agg)

def arrow3d(ax, length=1, width=0.05, head=0.2, headwidth=2,
                theta_x=0, theta_z=0, offset=(0,0,0), **kw):
    w = width
    h = head
    hw = headwidth
    theta_x = np.deg2rad(theta_x)
    theta_z = np.deg2rad(theta_z)

    a = [[0,0],[w,0],[w,(1-h)*length],[hw*w,(1-h)*length],[0,length]]
    a = np.array(a)

    r, theta = np.meshgrid(a[:,0], np.linspace(0,2*np.pi,30))
    z = np.tile(a[:,1],r.shape[0]).reshape(r.shape)
    x = r*np.sin(theta)
    y = r*np.cos(theta)

    rot_x = np.array([[1,0,0],[0,np.cos(theta_x),-np.sin(theta_x) ],
                      [0,np.sin(theta_x) ,np.cos(theta_x) ]])
    rot_z = np.array([[np.cos(theta_z),-np.sin(theta_z),0 ],
                      [np.sin(theta_z) ,np.cos(theta_z),0 ],[0,0,1]])

    b1 = np.dot(rot_x, np.c_[x.flatten(),y.flatten(),z.flatten()].T)
    b2 = np.dot(rot_z, b1)
    b2 = b2.T+np.array(offset)
    x = b2[:,0].reshape(r.shape);
    y = b2[:,1].reshape(r.shape);
    z = b2[:,2].reshape(r.shape);
    ax.plot_surface(x,y,z, **kw)
    return (ax)

def D_vector(ax,fig_agg,center,center1):
   if center[0][0] > center[1][0]:
        AX = 90-(( center[0][0]*90)/10.5)
   elif  center[0][0] < center[1][0]:
        AX = 90 + ((center[0][0] * 90) / 10.5)
   elif   center[0][0] ==  center[1][0]:
        AX = 90

   if center[0][0] > center[1][0]:
       AX1 = 90 - ((center[1][0] * 90) / 10.5)
   elif center[0][0] < center[1][0]:
       AX1 = 90 + ((center[1][0] * 90) / 10.5)
   elif center[0][0] == center[1][0]:
       AX1 = 90

   if center[2][0] > center[3][0]:
       AX2 = 90 - ((center[2][0] * 90) / 10.5)
   elif center[2][0] < center[3][0]:
       AX2 = 90 + ((center[2][0] * 90) / 10.5)
   elif center[2][0] == center[3][0]:
       AX2 = 90

   if center[2][0] > center[3][0]:
       AX3 = 90 - ((center[3][0] * 90) / 10.5)
   elif center[2][0] < center[3][0]:
       AX3 = 90 + ((center[3][0] * 90) / 10.5)
   elif center[2][0] == center[3][0]:
       AX3 = 90

   if center[4][0] > center[5][0]:
       AX4 = 90 - ((center[4][0] * 90) / 10.5)
   elif center[4][0] < center[5][0]:
       AX4 = 90 + ((center[4][0] * 90) / 10.5)
   elif center[4][0] == center[5][0]:
       AX4 = 90

   if center[4][0] > center[5][0]:
       AX5 = 90 - ((center[5][0] * 90) / 10.5)
   elif center[4][0] < center[5][0]:
       AX5 = 90 + ((center[5][0] * 90) / 10.5)
   elif center[4][0] == center[5][0]:
       AX5 = 90

   if center[6][0] > center[7][0]:
       AX6 = 90 - ((center[6][0] * 90) / 10.5)
   elif center[6][0] < center[7][0]:
       AX6 = 90 + ((center[6][0] * 90) / 10.5)
   elif center[6][0] == center[7][0]:
       AX6 = 90

   if center[6][0] > center[7][0]:
       AX7 = 90 - ((center[7][0] * 90) / 10.5)
   elif center[6][0] < center[7][0]:
       AX7 = 90 + ((center[7][0] * 90) / 10.5)
   elif center[6][0] == center[7][0]:
       AX7 = 90


   if center[0][0] > center[2][0]:
        AZ = 90-(( center[0][0]*90)/10.5)
   elif  center[0][0] < center[2][0]:
        AZ = 90 + ((center[0][0] * 90) / 10.5)
   elif   center[0][0] ==  center[1][0]:
        AZ = 90
   else:
       AZ = 90

   if center[0][0] > center[2][0]:
       AZ1 = 90 - ((center[2][0] * 90) / 10.5)
   elif center[0][0] < center[2][0]:
       AZ1 = 90 + ((center[2][0] * 90) / 10.5)
   elif center[0][0] == center[1][0]:
       AZ1 = 90
   else:
       AZ1 = 90

   if center[1][0] > center[3][0]:
       AZ2 = 90 - ((center[1][0] * 90) / 10.5)
   elif center[1][0] < center[3][0]:
       AZ2 = 90 + ((center[1][0] * 90) / 10.5)
   elif center[1][0] == center[3][0]:
       AZ2 = 90
   else:
       AZ2 = 90

   if center[1][0] > center[3][0]:
       AZ3 = 90 - ((center[3][0] * 90) / 10.5)
   elif center[1][0] < center[3][0]:
       AZ3 = 90 + ((center[3][0] * 90) / 10.5)
   elif center[1][0] == center[3][0]:
       AZ3 = 90
   else:
       AZ3 = 90


   if center[2][0] > center[4][0]:
       AZ1 = 90 - ((center[2][0] * 90) / 10.5)
   elif center[2][0] < center[4][0]:
       AZ1 = 90 + ((center[2][0] * 90) / 10.5)
   elif center[1][0] == center[3][0]:
       AZ1 = 90
   else:
       AZ1 = 90


   if center[2][0] > center[4][0]:
       AZ5 = 90 - ((center[4][0] * 90) / 10.5)
   elif center[2][0] < center[4][0]:
       AZ5 = 90 + ((center[4][0] * 90) / 10.5)
   elif center[1][0] == center[3][0]:
       AZ5 = 90
   else:
       AZ5 = 90



   if center[3][0] > center[5][0]:
       AZ3 = 90 - ((center[3][0] * 90) / 10.5)
   elif center[3][0] < center[5][0]:
       AZ3 = 90 + ((center[3][0] * 90) / 10.5)
   elif center[3][0] == center[5][0]:
       AZ3 = 90
   else:
       AZ3 = 90


   if center[3][0] > center[5][0]:
       AZ7 = 90 - ((center[5][0] * 90) / 10.5)
   elif center[3][0] < center[5][0]:
       AZ7 = 90 + ((center[5][0] * 90) / 10.5)
   elif center[3][0] == center[5][0]:
       AZ7 = 90
   else:
       AZ7 = 90


   if center[4][0] > center[6][0]:
       AZ5 = 90 - ((center[4][0] * 90) / 10.5)
   elif center[4][0] < center[6][0]:
       AZ5 = 90 + ((center[4][0] * 90) / 10.5)
   elif center[4][0] == center[6][0]:
       AZ5 = 90
   else:
       AZ5 = 90



   if center[4][0] > center[6][0]:
       AZ9 = 90 - ((center[6][0] * 90) / 10.5)
   elif center[4][0] < center[6][0]:
       AZ9 = 90 + ((center[6][0] * 90) / 10.5)
   elif center[4][0] == center[6][0]:
       AZ9 = 90
   else:
       AZ9 = 90


   if center[5][0] > center[7][0]:
       AZ7 = 90 - ((center[5][0] * 90) / 10.5)
   elif center[5][0] < center[7][0]:
       AZ7 = 90 + ((center[5][0] * 90) / 10.5)
   elif center[5][0] == center[7][0]:
       AZ7 = 90
   else:
       AZ7 = 90


   if center[5][0] > center[7][0]:
       AZ11 = 90 - ((center[7][0] * 90) / 10.5)
   elif center[5][0] < center[7][0]:
       AZ11 = 90 + ((center[7][0] * 90) / 10.5)
   elif center[5][0] == center[7][0]:
       AZ11 = 90
   else:
       AZ11 = 90




   ax = arrow3d(ax, length=-(-10.5-center[0][0]), width=0.10, head=0.15, headwidth=1.8, offset=[center[0][0], center[0][1], center[0][2]],
                theta_x=AZ, theta_z= AX , color="red")
   ax = arrow3d(ax, length=-(-10.5 - center[1][0]), width=0.10, head=0.15, headwidth=1.8,offset=[center[1][0], center[1][1], center[1][2]],
                 theta_x=AZ1, theta_z=AX1 , color="red")
   ax = arrow3d(ax, length=-(-10.5 - center[2][0]), width=0.10, head=0.15, headwidth=1.8,offset=[center[2][0], center[2][1], center[2][2]],
                theta_x=AZ2, theta_z=AX2, color="red")
   ax = arrow3d(ax, length=-(-10.5 - center[3][0]), width=0.10, head=0.15, headwidth=1.8,offset=[center[3][0], center[3][1], center[3][2]],
                theta_x=AZ3, theta_z=AX3, color="red")
   ax = arrow3d(ax, length=-(-10.5 - center[4][0]), width=0.10, head=0.15, headwidth=1.8,offset=[center[4][0], center[4][1], center[4][2]],
                theta_x=AZ5, theta_z=AX4, color="red")
   ax = arrow3d(ax, length=-(-10.5 - center[5][0]), width=0.10, head=0.15, headwidth=1.8,offset=[center[5][0], center[5][1], center[5][2]],
                theta_x=AZ7, theta_z=AX5, color="red")
   ax = arrow3d(ax, length=-(-10.5 - center[6][0]), width=0.10, head=0.15, headwidth=1.8,offset=[center[6][0], center[6][1], center[6][2]],
                theta_x=AZ9, theta_z=AX6, color="red")
   ax = arrow3d(ax, length=-(-10.5 - center[7][0]), width=0.10, head=0.15, headwidth=1.8,offset=[center[7][0], center[7][1], center[7][2]],
                theta_x=AZ11, theta_z= AX7, color="red")

#####################################################################################################################################################



   return (ax,fig_agg)


 ####AZ = 0
 ####AZ2 = 1

 ####AZ1 = 2
 ####AZ4 = 2

 ####AZ6 = 3
 ####AZ3 = 3

 ####AZ8 = 4
 ####AZ5 = 4

 ####AZ10 = 5
 ####AZ7 = 5

 ####AZ9 = 6
 ####AZ11 = 7