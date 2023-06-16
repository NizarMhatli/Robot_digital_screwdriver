import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
fig.set_size_inches(6, 6)
ax = fig.add_subplot(projection='3d')

ax.cla()
center = [0, 0, 0]
length = 250
width = 280
height = 330
size = (length, width, height)
ox, oy, oz = center
l, w, h = size

x = np.linspace(ox - l / 2, ox + l / 2, num=10)
y = np.linspace(oy - w / 2, oy + w / 2, num=10)
z = np.linspace(oz - h / 2, oz + h / 2, num=10)
x1, z1 = np.meshgrid(x, z)  ####
y11 = np.ones_like(x1) * (oy - w / 2)  ####
y12 = np.ones_like(x1) * (oy + w / 2)
x2, y2 = np.meshgrid(x, y)
z21 = np.ones_like(x2) * (oz - h / 2)
z22 = np.ones_like(x2) * (oz + h / 2)
y3, z3 = np.meshgrid(y, z)
x31 = np.ones_like(y3) * (ox - l / 2)
x32 = np.ones_like(y3) * (ox + l / 2)


# outside surface
ax.plot_surface(x1, y11, z1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
# inside surface
ax.plot_surface(x1, y12, z1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
# bottom surface
ax.plot_surface(x2, y2, z21, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
# upper surface
ax.plot_surface(x2, y2, z22, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
# left surface
ax.plot_wireframe(x31, y3, z3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
# right surface
ax.plot_surface(x32, y3, z3, color='b', rstride=1, cstride=1, alpha=0.6)  # 6
#ax.plot([0,300], [0,0], [0,0], 'r', linewidth=2, label='Line 1')




ax.quiver(0,0 ,100 ,50, 0,0,color= 'r')
     #     x  y   z     v   a1a2
                #           y z
plt.show()
