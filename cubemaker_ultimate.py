import matplotlib.pyplot as plt
import numpy as np

def make_cube_ulti(fig,ax,data,data1, fig_agg,SES):
    ax.cla()
    ######################################################################################################################
    #################################################################################
    ##############################SET UP SENSOR1####################################
    ################################################################################
    center = [(((250 - (data[4])) / 2)-(500-SES[9])), 0, 0]
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
    ax.plot_wireframe(x31, y3, z3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32, y3, z3, color='b', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR2####################################
    ################################################################################
    center1 = [(((250 - (data[0])) / 2)-(500-SES[9])), 280, 0]
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
    ax.plot_wireframe(x31_1, y3_1, z3_1, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_1, y3_1, z3_1, color='b', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR3####################################
    ################################################################################
    center2 = [(((250 - (data[5])) / 2)-(500-SES[9])), 0, 330]
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
    ax.plot_wireframe(x31_2, y3_2, z3_2, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_2, y3_2, z3_2, color='g', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR4####################################
    ################################################################################
    center3 = [(((250 - (data[1])) / 2)-(500-SES[9])), 280, 330]
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
    ax.plot_wireframe(x31_3, y3_3, z3_3, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_3, y3_3, z3_3, color='g', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR5####################################
    ################################################################################
    center4 = [(((250 - data[6]) / 2)-(500-SES[9])), 0, 660]
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
    ax.plot_wireframe(x31_4, y3_4, z3_4, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_4, y3_4, z3_4, color='g', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR6####################################
    ################################################################################
    center5 = [(((250 - data[2]) / 2)-(500-SES[9])), 280, 660]
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
    ax.plot_wireframe(x31_5, y3_5, z3_5, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_5, y3_5, z3_5, color='g', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR7####################################
    ################################################################################
    center6 = [(((250 - (data[7])) / 2)-(500-SES[9])), 0, 990]
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
    ax.plot_wireframe(x31_6, y3_6, z3_6, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_6, y3_6, z3_6, color='b', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR8####################################
    ################################################################################
    center7 = [(((250 - (data[3])) / 2)-(500-SES[9])), 280, 990]
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
    ax.plot_wireframe(x31_7, y3_7, z3_7, color='gray', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_7, y3_7, z3_7, color='b', rstride=1, cstride=1, alpha=0.6)  # 6
    #######################################################################################################################
 #################################################Block2#########################################################################
    #######################################################################################################################

    center_ = [((500-SES[9]) - ((250 - (data1[4])) / 2)), 0, 0]
    length_ = 250 - ((data1[4]))
    width_ = 280
    height_ = 330
    size_ = (length_, width_, height_)
    ox_, oy_, oz_ = center_
    l_, w_, h_ = size_

    x_ = np.linspace(ox_ - l_ / 2, ox_ + l_ / 2, num=10)
    y_ = np.linspace(oy_ - w_ / 2, oy_ + w_ / 2, num=10)
    z_ = np.linspace(oz_ - h_ / 2, oz_ + h_ / 2, num=10)
    x1_, z1_ = np.meshgrid(x_, z_)  ####
    y11_ = np.ones_like(x1_) * (oy_ - w_ / 2)  ####
    y12_ = np.ones_like(x1_) * (oy_ + w_ / 2)
    x2_, y2_ = np.meshgrid(x_, y_)
    z21_ = np.ones_like(x2_) * (oz_ - h_ / 2)
    z22_ = np.ones_like(x2_) * (oz_ + h_ / 2)
    y3_, z3_ = np.meshgrid(y_, z_)
    x31_ = np.ones_like(y3_) * (ox_ - l_ / 2)
    x32_ = np.ones_like(y3_) * (ox_ + l_ / 2)

    ######################################################################################
    ############################senseor 1 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_, y11_, z1_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_, y12_, z1_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_, y2_, z21_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_, y2_, z22_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_, y3_, z3_, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_, y3_, z3_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR2####################################
    ################################################################################
    center1_ = [((500-SES[9]) - ((250 - (data1[0])) / 2)), 280, 0]
    size1_ = (250 - (data1[0]), 280, 330)
    ox1_, oy1_, oz1_ = center1_
    l1_, w1_, h1_ = size1_

    x_1_ = np.linspace(ox1_ - l1_ / 2, ox1_ + l1_ / 2, num=10)
    y_1_ = np.linspace(oy1_ - w1_ / 2, oy1_ + w1_ / 2, num=10)
    z_1_ = np.linspace(oz1_ - h1_ / 2, oz1_ + h1_ / 2, num=10)
    x1_1_, z1_1_ = np.meshgrid(x_1_, z_1_)  ####
    y11_1_ = np.ones_like(x1_1_) * (oy1_ - w1_ / 2)  ####
    y12_1_ = np.ones_like(x1_1_) * (oy1_ + w1_ / 2)
    x2_1_, y2_1_ = np.meshgrid(x_1_, y_1_)
    z21_1_ = np.ones_like(x2_1_) * (oz1_ - h1_ / 2)
    z22_1_ = np.ones_like(x2_1_) * (oz1_ + h1_ / 2)
    y3_1_, z3_1_ = np.meshgrid(y_1_, z_1_)
    x31_1_ = np.ones_like(y3_1_) * (ox1_ - l1_ / 2)
    x32_1_ = np.ones_like(y3_1_) * (ox1_ + l1_ / 2)

    ######################################################################################
    ############################senseor 2 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_1_, y11_1_, z1_1_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_1_, y12_1_, z1_1_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_1_, y2_1_, z21_1_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_1_, y2_1_, z22_1_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_1_, y3_1_, z3_1_, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_1_, y3_1_, z3_1_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR3####################################
    ################################################################################
    center2_ = [((500-SES[9]) - ((250 - (data1[5])) / 2)), 0, 330]
    size2_ = (250 - (data1[5]), 280, 330)
    ox2_, oy2_, oz2_ = center2_
    l2_, w2_, h2_ = size2_

    x_2_ = np.linspace(ox2_ - l2_ / 2, ox2_ + l2_ / 2, num=10)
    y_2_ = np.linspace(oy2_ - w2_ / 2, oy2_ + w2_ / 2, num=10)
    z_2_ = np.linspace(oz2_ - h2_ / 2, oz2_ + h2_ / 2, num=10)
    x1_2_, z1_2_ = np.meshgrid(x_2_, z_2_)  ####
    y11_2_ = np.ones_like(x1_2_) * (oy2_ - w2_ / 2)  ####
    y12_2_ = np.ones_like(x1_2_) * (oy2_ + w2_ / 2)
    x2_2_, y2_2_ = np.meshgrid(x_2_, y_2_)
    z21_2_ = np.ones_like(x2_2_) * (oz2_ - h2_ / 2)
    z22_2_ = np.ones_like(x2_2_) * (oz2_ + h2_ / 2)
    y3_2_, z3_2_ = np.meshgrid(y_2_, z_2_)
    x31_2_ = np.ones_like(y3_2_) * (ox2_ - l2_ / 2)
    x32_2_ = np.ones_like(y3_2_) * (ox2_ + l2_ / 2)

    ######################################################################################
    ############################senseor 3 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_2_, y11_2_, z1_2_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_2_, y12_2_, z1_2_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_2_, y2_2_, z21_2_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_2_, y2_2_, z22_2_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_2_, y3_2_, z3_2_, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_2_, y3_2_, z3_2_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR4####################################
    ################################################################################
    center3_ = [((500-SES[9]) - ((250 - (data1[1])) / 2)), 280, 330]
    size3_ = (250 - (data1[1]), 280, 330)
    ox3_, oy3_, oz3_ = center3_
    l3_, w3_, h3_ = size3_

    x_3_ = np.linspace(ox3_ - l3_ / 2, ox3_ + l3_ / 2, num=10)
    y_3_ = np.linspace(oy3_ - w3_ / 2, oy3_ + w3_ / 2, num=10)
    z_3_ = np.linspace(oz3_ - h3_ / 2, oz3_ + h3_ / 2, num=10)
    x1_3_, z1_3_ = np.meshgrid(x_3_, z_3_)  ####
    y11_3_ = np.ones_like(x1_3_) * (oy3_ - w3_ / 2)  ####
    y12_3_ = np.ones_like(x1_3_) * (oy3_ + w3_ / 2)
    x2_3_, y2_3_ = np.meshgrid(x_3_, y_3_)
    z21_3_ = np.ones_like(x2_3_) * (oz3_ - h3_ / 2)
    z22_3_ = np.ones_like(x2_3_) * (oz3_ + h3_ / 2)
    y3_3_, z3_3_ = np.meshgrid(y_3_, z_3_)
    x31_3_ = np.ones_like(y3_3_) * (ox3_ - l3_ / 2)
    x32_3_ = np.ones_like(y3_3_) * (ox3_ + l3_ / 2)

    ######################################################################################
    ############################senseor 4 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_3_, y11_3_, z1_3_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_3_, y12_3_, z1_3_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_3_, y2_3_, z21_3_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_3_, y2_3_, z22_3_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_3_, y3_3_, z3_3_, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_3_, y3_3_, z3_3_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR5####################################
    ################################################################################
    center4_ = [((500-SES[9]) - ((250 - data1[6]) / 2)), 0, 660]
    size4_ = (250 - (data1[6]), 280, 330)
    ox4_, oy4_, oz4_ = center4_
    l4_, w4_, h4_ = size4_

    x_4_ = np.linspace(ox4_ - l4_ / 2, ox4_ + l4_ / 2, num=10)
    y_4_ = np.linspace(oy4_ - w4_ / 2, oy4_ + w4_ / 2, num=10)
    z_4_ = np.linspace(oz4_ - h4_ / 2, oz4_ + h4_ / 2, num=10)
    x1_4_, z1_4_ = np.meshgrid(x_4_, z_4_)  ####
    y11_4_ = np.ones_like(x1_4_) * (oy4_ - w4_ / 2)  ####
    y12_4_ = np.ones_like(x1_4_) * (oy4_ + w4_ / 2)
    x2_4_, y2_4_ = np.meshgrid(x_4_, y_4_)
    z21_4_ = np.ones_like(x2_4_) * (oz4_ - h4_ / 2)
    z22_4_ = np.ones_like(x2_4_) * (oz4_ + h4_ / 2)
    y3_4_, z3_4_ = np.meshgrid(y_4_, z_4_)
    x31_4_ = np.ones_like(y3_4_) * (ox4_ - l4_ / 2)
    x32_4_ = np.ones_like(y3_4_) * (ox4_ + l4_ / 2)

    ######################################################################################
    ############################senseor 5 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_4_, y11_4_, z1_4_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_4_, y12_4_, z1_4_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_4_, y2_4_, z21_4_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_4_, y2_4_, z22_4_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_4_, y3_4_, z3_4_, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_4_, y3_4_, z3_4_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR6####################################
    ################################################################################
    center5_ = [((500-SES[9]) - ((250 - data1[2]) / 2)), 280, 660]
    size5_ = (250 - (data1[2]), 280, 330)
    ox5_, oy5_, oz5_ = center5_
    l5_, w5_, h5_ = size5_

    x_5_ = np.linspace(ox5_ - l5_ / 2, ox5_ + l5_ / 2, num=10)
    y_5_ = np.linspace(oy5_ - w5_ / 2, oy5_ + w5_ / 2, num=10)
    z_5_ = np.linspace(oz5_ - h5_ / 2, oz5_ + h5_ / 2, num=10)
    x1_5_, z1_5_ = np.meshgrid(x_5_, z_5_)  ####
    y11_5_ = np.ones_like(x1_5_) * (oy5_ - w5_ / 2)  ####
    y12_5_ = np.ones_like(x1_5_) * (oy5_ + w5_ / 2)
    x2_5_, y2_5_ = np.meshgrid(x_5_, y_5_)
    z21_5_ = np.ones_like(x2_5_) * (oz5_ - h5_ / 2)
    z22_5_ = np.ones_like(x2_5_) * (oz5_ + h5_ / 2)
    y3_5_, z3_5_ = np.meshgrid(y_5_, z_5_)
    x31_5_ = np.ones_like(y3_5_) * (ox5_ - l5_ / 2)
    x32_5_ = np.ones_like(y3_5_) * (ox5_ + l5_ / 2)

    ######################################################################################
    ############################senseor 6 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_5_, y11_5_, z1_5_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_5_, y12_5_, z1_5_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_5_, y2_5_, z21_5_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_5_, y2_5_, z22_5_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_5_, y3_5_, z3_5_, color='g', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_5_, y3_5_, z3_5_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6

    #################################################################################
    ##############################SET UP SENSOR7####################################
    ################################################################################
    center6_ = [((500-SES[9]) - ((250 - (data1[7])) / 2)), 0, 990]
    size6_ = (250 - (data1[7]), 280, 330)
    ox6_, oy6_, oz6_ = center6_
    l6_, w6_, h6_ = size6_

    x_6_ = np.linspace(ox6_ - l6_ / 2, ox6_ + l6_ / 2, num=10)
    y_6_ = np.linspace(oy6_ - w6_ / 2, oy6_ + w6_ / 2, num=10)
    z_6_ = np.linspace(oz6_ - h6_ / 2, oz6_ + h6_ / 2, num=10)
    x1_6_, z1_6_ = np.meshgrid(x_6_, z_6_)  ####
    y11_6_ = np.ones_like(x1_6_) * (oy6_ - w6_ / 2)  ####
    y12_6_ = np.ones_like(x1_6_) * (oy6_ + w6_ / 2)
    x2_6_, y2_6_ = np.meshgrid(x_6_, y_6_)
    z21_6_ = np.ones_like(x2_6_) * (oz6_ - h6_ / 2)
    z22_6_ = np.ones_like(x2_6_) * (oz6_ + h6_ / 2)
    y3_6_, z3_6_ = np.meshgrid(y_6_, z_6_)
    x31_6_ = np.ones_like(y3_6_) * (ox6_ - l6_ / 2)
    x32_6_ = np.ones_like(y3_6_) * (ox6_ + l6_ / 2)

    ######################################################################################
    ############################senseor 7 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_6_, y11_6_, z1_6_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_6_, y12_6_, z1_6_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_6_, y2_6_, z21_6_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_6_, y2_6_, z22_6_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_6_, y3_6_, z3_6_, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_6_, y3_6_, z3_6_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6
    #################################################################################
    ##############################SET UP SENSOR8####################################
    ################################################################################
    center7_ = [((500-SES[9]) - ((250 - (data1[3])) / 2)), 280, 990]
    size7_ = (250 - (data1[3]), 280, 330)
    ox7_, oy7_, oz7_ = center7_
    l7_, w7_, h7_ = size7_

    x_7_ = np.linspace(ox7_ - l7_ / 2, ox7_ + l7_ / 2, num=10)
    y_7_ = np.linspace(oy7_ - w7_ / 2, oy7_ + w7_ / 2, num=10)
    z_7_ = np.linspace(oz7_ - h7_ / 2, oz7_ + h7_ / 2, num=10)
    x1_7_, z1_7_ = np.meshgrid(x_7_, z_7_)  ####
    y11_7_ = np.ones_like(x1_7_) * (oy7_ - w7_ / 2)  ####
    y12_7_ = np.ones_like(x1_7_) * (oy7_ + w7_ / 2)
    x2_7_, y2_7_ = np.meshgrid(x_7_, y_7_)
    z21_7_ = np.ones_like(x2_7_) * (oz7_ - h7_ / 2)
    z22_7_ = np.ones_like(x2_7_) * (oz7_ + h7_ / 2)
    y3_7_, z3_7_ = np.meshgrid(y_7_, z_7_)
    x31_7_ = np.ones_like(y3_7_) * (ox7_ - l7_ / 2)
    x32_7_ = np.ones_like(y3_7_) * (ox7_ + l7_ / 2)

    ######################################################################################
    ############################senseor 8 ##############################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_7_, y11_7_, z1_7_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_7_, y12_7_, z1_7_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_7_, y2_7_, z21_7_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_7_, y2_7_, z22_7_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_7_, y3_7_, z3_7_, color='b', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_7_, y3_7_, z3_7_, color='gray', rstride=1, cstride=1, alpha=0.6)  # 6
    ###############################################################################################
    ##############################################################################################
    #######################################extra block############################################
    center7__ = [ 0, 140, 1370]
    size7__ = (1200, 560, 330)
    ox7__, oy7__, oz7__ = center7__
    l7__, w7__, h7__ = size7__

    x_7__ = np.linspace(ox7__ - l7__ / 2, ox7__ + l7__ / 2, num=10)
    y_7__ = np.linspace(oy7__ - w7__ / 2, oy7__ + w7__ / 2, num=10)
    z_7__ = np.linspace(oz7__ - h7__ / 2, oz7__ + h7__ / 2, num=10)
    x1_7__, z1_7__ = np.meshgrid(x_7__, z_7__)  ####
    y11_7__ = np.ones_like(x1_7__) * (oy7__ - w7__ / 2)  ####
    y12_7__ = np.ones_like(x1_7__) * (oy7__ + w7__ / 2)
    x2_7__, y2_7__ = np.meshgrid(x_7__, y_7__)
    z21_7__ = np.ones_like(x2_7__) * (oz7__ - h7__ / 2)
    z22_7__ = np.ones_like(x2_7__) * (oz7__ + h7__ / 2)
    y3_7__, z3_7__ = np.meshgrid(y_7__, z_7__)
    x31_7__ = np.ones_like(y3_7__) * (ox7__ - l7__ / 2)
    x32_7__ = np.ones_like(y3_7__) * (ox7__ + l7__ / 2)

    ######################################################################################
    ##########################################################################
    #####################################################################################
    # outside surface
    ax.plot_surface(x1_7__, y11_7__, z1_7__, color='black', rstride=1, cstride=1, alpha=0.6)  # 1 needed side
    # inside surface
    ax.plot_surface(x1_7__, y12_7__, z1_7__, color='black', rstride=1, cstride=1, alpha=0.6)  # 2 needed side
    # bottom surface
    ax.plot_surface(x2_7__, y2_7__, z21_7__, color='black', rstride=1, cstride=1, alpha=0.6)  # 3 needed side
    # upper surface
    ax.plot_surface(x2_7__, y2_7__, z22_7__, color='black', rstride=1, cstride=1, alpha=0.6)  # 4 needed side
    # left surface
    ax.plot_wireframe(x31_7__, y3_7__, z3_7__, color='black', rstride=1, cstride=1, alpha=0.6)  # 5
    # right surface
    ax.plot_surface(x32_7__, y3_7__, z3_7__, color='black', rstride=1, cstride=1, alpha=0.6)  # 6
    ###################################PLOTTING ALL##########################################
    ########################################################################################################################
    ax.set_xlim(-500, 600)
    # ax.set_ylim(-1000, 1000)
    ax.set_zlim(0, 1000)
    ax.text(-270,-500,1200,'Robotiq',color='red',size=25)
    #plt.axis('off')
    #ax.set_axis_off()
    ###########################
    return (fig_agg)
