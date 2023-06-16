
from square import square_maker,square_maker1,DIS,vecdef,D_vector
def make_cube_ulti_new(ax,data, fig_agg,SES):
    list1,list2,list3,i = [[(((7 - (data[4])) / 2) - (14 - SES[9])), 0, 0], [(((7 - (data[0])) / 2) - (14 - SES[9])), 7.5, 0],[(((7 - (data[5])) / 2) - (14 - SES[9])), 0, 7.5],[(((7 - (data[1])) / 2) - (14 - SES[9])), 7.5, 7.5], [(((7 - data[6]) / 2) - (14 - SES[9])), 0, 15],[(((7 - data[2]) / 2) - (14 - SES[9])), 7.5, 15],[(((7 - (data[7])) / 2) - (14 - SES[9])), 0, 22.5],[(((7 - (data[3])) / 2) - (14 - SES[9])), 7.5, 22.5]],[(7 - ((data[4])), 7.5, 7.5), (7 - (data[0]), 7.5, 7.5), (7 - (data[5]), 7.5, 7.5),(7 - (data[1]), 7.5, 7.5), (7 - (data[6]), 7.5, 7.5),(7 - (data[6]), 7.5, 7.5), (7 - (data[7]), 7.5, 7.5), (7 - (data[3]), 7.5, 7.5)],['b', 'b', 'g', 'g', 'g', 'g', 'b', 'b'] ,0
    ax.cla()
    while i< len(list3):
         ax, fig_agg = square_maker(ax,fig_agg,list1[i],list2[i],list3[i])
         i+= 1
    ax.set_xlim(-15, 15)
    ax.set_zlim(000, 18)
    return(fig_agg)

def make_cube_ulti_new1(ax,data1, fig_agg,SES):
    list3,list4,list5,i = ['b', 'b', 'g', 'g', 'g', 'g', 'b', 'b'],[[((14-SES[9]) - ((7 - (data1[4])) / 2)), 0, 0],[((14-SES[9]) - ((7 - (data1[0])) / 2)), 7.5, 0],[((14 - SES[9]) - ((7 - (data1[5])) / 2)), 0, 7.5],[((14-SES[9]) - ((7 - (data1[1])) / 2)), 7.5, 7.5],[((14 - SES[9]) - ((7 - data1[6]) / 2)), 0, 15],[((14-SES[9]) - ((7 - data1[2]) / 2)), 7.5, 15],[((14 - SES[9]) - ((7 - (data1[7])) / 2)), 0, 22.5],[((14-SES[9]) - ((7 - (data1[3])) / 2)), 7.5, 22.5]],[(7 - ((data1[4])), 7.5, 7.5), (7 - (data1[0]), 7.5, 7.5), (7 - (data1[5]), 7.5, 7.5),(7 - (data1[1]), 7.5, 7.5), (7 - (data1[6]), 7.5, 7.5),(7 - (data1[6]), 7.5, 7.5), (7 - (data1[7]), 7.5, 7.5), (7 - (data1[3]), 7.5, 7.5)],0
    ax.cla()
    while i< len(list3):
         ax, fig_agg = square_maker1(ax, fig_agg, list4[i], list5[i], list3[i])
         i+= 1
    ax.set_xlim(-15, 15)
    ax.set_zlim(000, 18)
    return(fig_agg)

def make_cube_ulti_new_oof(ax,data,data1, fig_agg,SES):
    ses = SES[9] * 7 / 250
    list1 = [[(((7 - (data[4])) / 2) - (14 - ses)), 0, 0], [(((7 - (data[0])) / 2) - (14 - ses)), 7.5, 0],[(((7 - (data[5])) / 2) - (14 - ses)), 0, 7.5],[(((7 - (data[1])) / 2) - (14 - ses)), 7.5, 7.5], [(((7 - data[6]) / 2) - (14 - ses)), 0, 15],[(((7 - data[2]) / 2) - (14 - ses)), 7.5, 15],[(((7 - (data[7])) / 2) - (14 - ses)), 0, 22.5],[(((7 - (data[3])) / 2) - (14 - ses)), 7.5, 22.5]]
    list2 = [(7 - ((data[4])), 7.5, 7.5), (7 - (data[0]), 7.5, 7.5), (7 - (data[5]), 7.5, 7.5),(7 - (data[1]), 7.5, 7.5), (7 - (data[6]), 7.5, 7.5),(7 - (data[6]), 7.5, 7.5), (7 - (data[7]), 7.5, 7.5), (7 - (data[3]), 7.5, 7.5)]
    list3 = ['b', 'b', 'g', 'g', 'g', 'g', 'b', 'b']
    list4 = [[((14-ses) - ((7 - (data1[4])) / 2)), 0, 0],[((14-ses) - ((7 - (data1[0])) / 2)), 7.5, 0],[((14 - ses) - ((7 - (data1[5])) / 2)), 0, 7.5],[((14-ses) - ((7 - (data1[1])) / 2)), 7.5, 7.5],[((14 - ses) - ((7 - data1[6]) / 2)), 0, 15],[((14-ses) - ((7 - data1[2]) / 2)), 7.5, 15],[((14 - ses) - ((7 - (data1[7])) / 2)), 0, 22.5],[((14-ses) - ((7 - (data1[3])) / 2)), 7.5, 22.5]]
    list5 = [(7 - ((data1[4])), 7.5, 7.5), (7 - (data1[0]), 7.5, 7.5), (7 - (data1[5]), 7.5, 7.5),(7 - (data1[1]), 7.5, 7.5), (7 - (data1[6]), 7.5, 7.5),(7 - (data1[6]), 7.5, 7.5), (7 - (data1[7]), 7.5, 7.5), (7 - (data1[3]), 7.5, 7.5)]
    i = 0
    ax.cla()

    while i< len(list3):
         ax, fig_agg = square_maker(ax,fig_agg,list1[i],list2[i],list3[i])
         ax, fig_agg = square_maker1(ax, fig_agg, list4[i], list5[i], list3[i])
         i+= 1
    ax, fig_agg = DIS(ax, fig_agg,list1,list4)
    ax, fig_agg = vecdef(ax, fig_agg, list1, list4)
    ax.set_xlim(-15, 15)
    ax.set_zlim(000, 18)
    return(fig_agg)

def make_vector(ax,data,data1, fig_agg,SES):
    list1,list2,list3,list4,list5,i = [[(((7 - (data[4])) / 2) - (14 - SES[9])), 0, 0], [(((7 - (data[0])) / 2) - (14 - SES[9])), 7.5, 0],[(((7 - (data[5])) / 2) - (14 - SES[9])), 0, 7.5],[(((7 - (data[1])) / 2) - (14 - SES[9])), 7.5, 7.5], [(((7 - data[6]) / 2) - (14 - SES[9])), 0, 15],[(((7 - data[2]) / 2) - (14 - SES[9])), 7.5, 15],[(((7 - (data[7])) / 2) - (14 - SES[9])), 0, 22.5],[(((7 - (data[3])) / 2) - (14 - SES[9])), 7.5, 22.5]],[(7 - ((data[4])), 7.5, 7.5), (7 - (data[0]), 7.5, 7.5), (7 - (data[5]), 7.5, 7.5),(7 - (data[1]), 7.5, 7.5), (7 - (data[6]), 7.5, 7.5),(7 - (data[6]), 7.5, 7.5), (7 - (data[7]), 7.5, 7.5), (7 - (data[3]), 7.5, 7.5)],['b', 'b', 'g', 'g', 'g', 'g', 'b', 'b'],[[((14-SES[9]) - ((7 - (data1[4])) / 2)), 0, 0],[((14-SES[9]) - ((7 - (data1[0])) / 2)), 7.5, 0],[((14 - SES[9]) - ((7 - (data1[5])) / 2)), 0, 7.5],[((14-SES[9]) - ((7 - (data1[1])) / 2)), 7.5, 7.5],[((14 - SES[9]) - ((7 - data1[6]) / 2)), 0, 15],[((14-SES[9]) - ((7 - data1[2]) / 2)), 7.5, 15],[((14 - SES[9]) - ((7 - (data1[7])) / 2)), 0, 22.5],[((14-SES[9]) - ((7 - (data1[3])) / 2)), 7.5, 22.5]],[(7 - ((data1[4])), 7.5, 7.5), (7 - (data1[0]), 7.5, 7.5), (7 - (data1[5]), 7.5, 7.5),(7 - (data1[1]), 7.5, 7.5), (7 - (data1[6]), 7.5, 7.5),(7 - (data1[6]), 7.5, 7.5), (7 - (data1[7]), 7.5, 7.5), (7 - (data1[3]), 7.5, 7.5)],0
    ax.cla()
    ax,fig_agg = D_vector(ax, fig_agg,list1,list4)
    ax.set_xlim(-15, -6)
    ax.set_zlim(000, 20)
    return(fig_agg)