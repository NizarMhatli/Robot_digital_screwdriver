import matplotlib.pyplot as plt
import numpy as np

def make_cube1(fig,ax,data,fig_agg):
    ax.cla()
    ######################################################################################################################
    #################################################################################
    ##############################SET UP SENSOR1####################################
    ################################################################################
    center = [(375-((250 - (data[4])) / 2)), 0, 0]
    length = 250 - ((data[4]))
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

    ######################################################################################
    ############################senseor 1 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1, y11, z1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1, y12, z1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2, y2, z21, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2, y2, z22, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31, y3, z3, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32, y3, z3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR2####################################
    ################################################################################
    center1 = [(375-((250 - (data[0])) / 2)), 280, 0]
    size1 = (250 - (data[0]), 280, 330)
    ox1, oy1, oz1 = center1
    l1, w1, h1 = size1

    x_1 = np.linspace(ox1 - l1 / 2, ox1 + l1 / 2, num=10)
    y_1 = np.linspace(oy1 - w1 / 2, oy1 + w1 / 2, num=10)
    z_1 = np.linspace(oz1 - h1 / 2, oz1 + h1 / 2, num=10)
    x1_1, z1_1 = np.meshgrid(x_1, z_1)  ####
    y11_1 = np.ones_like(x1_1) * (oy1 - w1 / 2)  ####
    y12_1 = np.ones_like(x1_1) * (oy1 + w1 / 2)
    x2_1, y2_1 = np.meshgrid(x_1, y_1)
    z21_1 = np.ones_like(x2_1) * (oz1 - h1 / 2)
    z22_1 = np.ones_like(x2_1) * (oz1 + h1 / 2)
    y3_1, z3_1 = np.meshgrid(y_1, z_1)
    x31_1 = np.ones_like(y3_1) * (ox1 - l1 / 2)
    x32_1 = np.ones_like(y3_1) * (ox1 + l1 / 2)

    ######################################################################################
    ############################senseor 2 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_1, y11_1, z1_1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_1, y12_1, z1_1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_1, y2_1, z21_1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_1, y2_1, z22_1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_1, y3_1, z3_1, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_1, y3_1, z3_1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR3####################################
    ################################################################################
    center2 = [(375-((250 - (data[5])) / 2)), 0, 330]
    size2 = (250 - (data[5]), 280, 330)
    ox2, oy2, oz2 = center2
    l2, w2, h2 = size2

    x_2 = np.linspace(ox2 - l2 / 2, ox2 + l2 / 2, num=10)
    y_2 = np.linspace(oy2 - w2 / 2, oy2 + w2 / 2, num=10)
    z_2 = np.linspace(oz2 - h2 / 2, oz2 + h2 / 2, num=10)
    x1_2, z1_2 = np.meshgrid(x_2, z_2)  ####
    y11_2 = np.ones_like(x1_2) * (oy2 - w2 / 2)  ####
    y12_2 = np.ones_like(x1_2) * (oy2 + w2 / 2)
    x2_2, y2_2 = np.meshgrid(x_2, y_2)
    z21_2 = np.ones_like(x2_2) * (oz2 - h2 / 2)
    z22_2 = np.ones_like(x2_2) * (oz2 + h2 / 2)
    y3_2, z3_2 = np.meshgrid(y_2, z_2)
    x31_2 = np.ones_like(y3_2) * (ox2 - l2 / 2)
    x32_2 = np.ones_like(y3_2) * (ox2 + l2 / 2)

    ######################################################################################
    ############################senseor 3 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_2, y11_2, z1_2, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_2, y12_2, z1_2, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_2, y2_2, z21_2, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_2, y2_2, z22_2, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_2, y3_2, z3_2, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_2, y3_2, z3_2, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR4####################################
    ################################################################################
    center3 = [(375-((250 - (data[1])) / 2)), 280, 330]
    size3 = (250 - (data[1]), 280, 330)
    ox3, oy3, oz3 = center3
    l3, w3, h3 = size3

    x_3 = np.linspace(ox3 - l3 / 2, ox3 + l3 / 2, num=10)
    y_3 = np.linspace(oy3 - w3 / 2, oy3 + w3 / 2, num=10)
    z_3 = np.linspace(oz3 - h3 / 2, oz3 + h3 / 2, num=10)
    x1_3, z1_3 = np.meshgrid(x_3, z_3)  ####
    y11_3 = np.ones_like(x1_3) * (oy3 - w3 / 2)  ####
    y12_3 = np.ones_like(x1_3) * (oy3 + w3 / 2)
    x2_3, y2_3 = np.meshgrid(x_3, y_3)
    z21_3 = np.ones_like(x2_3) * (oz3 - h3 / 2)
    z22_3 = np.ones_like(x2_3) * (oz3 + h3 / 2)
    y3_3, z3_3 = np.meshgrid(y_3, z_3)
    x31_3 = np.ones_like(y3_3) * (ox3 - l3 / 2)
    x32_3 = np.ones_like(y3_3) * (ox3 + l3 / 2)

    ######################################################################################
    ############################senseor 4 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_3, y11_3, z1_3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_3, y12_3, z1_3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_3, y2_3, z21_3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_3, y2_3, z22_3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_3, y3_3, z3_3, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_3, y3_3, z3_3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR5####################################
    ################################################################################
    center4 = [(375-((250 - data[6]) / 2)), 0, 660]
    size4 = (250 - (data[6]), 280, 330)
    ox4, oy4, oz4 = center4
    l4, w4, h4 = size4

    x_4 = np.linspace(ox4 - l4 / 2, ox4 + l4 / 2, num=10)
    y_4 = np.linspace(oy4 - w4 / 2, oy4 + w4 / 2, num=10)
    z_4 = np.linspace(oz4 - h4 / 2, oz4 + h4 / 2, num=10)
    x1_4, z1_4 = np.meshgrid(x_4, z_4)  ####
    y11_4 = np.ones_like(x1_4) * (oy4 - w4 / 2)  ####
    y12_4 = np.ones_like(x1_4) * (oy4 + w4 / 2)
    x2_4, y2_4 = np.meshgrid(x_4, y_4)
    z21_4 = np.ones_like(x2_4) * (oz4 - h4 / 2)
    z22_4 = np.ones_like(x2_4) * (oz4 + h4 / 2)
    y3_4, z3_4 = np.meshgrid(y_4, z_4)
    x31_4 = np.ones_like(y3_4) * (ox4 - l4 / 2)
    x32_4 = np.ones_like(y3_4) * (ox4 + l4 / 2)

    ######################################################################################
    ############################senseor 5 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_4, y11_4, z1_4, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_4, y12_4, z1_4, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_4, y2_4, z21_4, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_4, y2_4, z22_4, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_4, y3_4, z3_4, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_4, y3_4, z3_4, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR6####################################
    ################################################################################
    center5 = [(375-((250 - data[2]) / 2)), 280, 660]
    size5 = (250 - (data[2]), 280, 330)
    ox5, oy5, oz5 = center5
    l5, w5, h5 = size5

    x_5 = np.linspace(ox5 - l5 / 2, ox5 + l5 / 2, num=10)
    y_5 = np.linspace(oy5 - w5 / 2, oy5 + w5 / 2, num=10)
    z_5 = np.linspace(oz5 - h5 / 2, oz5 + h5 / 2, num=10)
    x1_5, z1_5 = np.meshgrid(x_5, z_5)  ####
    y11_5 = np.ones_like(x1_5) * (oy5 - w5 / 2)  ####
    y12_5 = np.ones_like(x1_5) * (oy5 + w5 / 2)
    x2_5, y2_5 = np.meshgrid(x_5, y_5)
    z21_5 = np.ones_like(x2_5) * (oz5 - h5 / 2)
    z22_5 = np.ones_like(x2_5) * (oz5 + h5 / 2)
    y3_5, z3_5 = np.meshgrid(y_5, z_5)
    x31_5 = np.ones_like(y3_5) * (ox5 - l5 / 2)
    x32_5 = np.ones_like(y3_5) * (ox5 + l5 / 2)

    ######################################################################################
    ############################senseor 6 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_5, y11_5, z1_5, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_5, y12_5, z1_5, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_5, y2_5, z21_5, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_5, y2_5, z22_5, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_5, y3_5, z3_5, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_5, y3_5, z3_5, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR7####################################
    ################################################################################
    center6 = [(375-((250 - (data[7])) / 2)), 0, 990]
    size6 = (250 - (data[7]), 280, 330)
    ox6, oy6, oz6 = center6
    l6, w6, h6 = size6

    x_6 = np.linspace(ox6 - l6 / 2, ox6 + l6 / 2, num=10)
    y_6 = np.linspace(oy6 - w6 / 2, oy6 + w6 / 2, num=10)
    z_6 = np.linspace(oz6 - h6 / 2, oz6 + h6 / 2, num=10)
    x1_6, z1_6 = np.meshgrid(x_6, z_6)  ####
    y11_6 = np.ones_like(x1_6) * (oy6 - w6 / 2)  ####
    y12_6 = np.ones_like(x1_6) * (oy6 + w6 / 2)
    x2_6, y2_6 = np.meshgrid(x_6, y_6)
    z21_6 = np.ones_like(x2_6) * (oz6 - h6 / 2)
    z22_6 = np.ones_like(x2_6) * (oz6 + h6 / 2)
    y3_6, z3_6 = np.meshgrid(y_6, z_6)
    x31_6 = np.ones_like(y3_6) * (ox6 - l6 / 2)
    x32_6 = np.ones_like(y3_6) * (ox6 + l6 / 2)

    ######################################################################################
    ############################senseor 7 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_6, y11_6, z1_6, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_6, y12_6, z1_6, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_6, y2_6, z21_6, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_6, y2_6, z22_6, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_6, y3_6, z3_6, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_6, y3_6, z3_6, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR8####################################
    ################################################################################
    center7 = [(375-((250 - (data[3])) / 2)), 280, 990]
    size7 = (250 - (data[3]), 280, 330)
    ox7, oy7, oz7 = center7
    l7, w7, h7 = size7

    x_7 = np.linspace(ox7 - l7 / 2, ox7 + l7 / 2, num=10)
    y_7 = np.linspace(oy7 - w7 / 2, oy7 + w7 / 2, num=10)
    z_7 = np.linspace(oz7 - h7 / 2, oz7 + h7 / 2, num=10)
    x1_7, z1_7 = np.meshgrid(x_7, z_7)  ####
    y11_7 = np.ones_like(x1_7) * (oy7 - w7 / 2)  ####
    y12_7 = np.ones_like(x1_7) * (oy7 + w7 / 2)
    x2_7, y2_7 = np.meshgrid(x_7, y_7)
    z21_7 = np.ones_like(x2_7) * (oz7 - h7 / 2)
    z22_7 = np.ones_like(x2_7) * (oz7 + h7 / 2)
    y3_7, z3_7 = np.meshgrid(y_7, z_7)
    x31_7 = np.ones_like(y3_7) * (ox7 - l7 / 2)
    x32_7 = np.ones_like(y3_7) * (ox7 + l7 / 2)

    ######################################################################################
    ############################senseor 8 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_7, y11_7, z1_7, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_7, y12_7, z1_7, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_7, y2_7, z21_7, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_7, y2_7, z22_7, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_7, y3_7, z3_7, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_7, y3_7, z3_7, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #######################################################################################################################
    ###################################PLOTTING ALL##########################################
    ########################################################################################################################
    ax.set_xlim(00, 1000)
    # ax.set_ylim(-1000, 1000)
    ax.set_zlim(0, 900)
    ###########################
    return (fig_agg)