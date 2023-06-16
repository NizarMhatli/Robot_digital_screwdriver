import sys
import os
import time
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,FigureCanvasAgg
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import PySimpleGUI as sg
from figure_create import figure_draw_1,draw_figure
from cubemaker_ultimate_new import make_cube_ulti_new_oof,make_vector
from Newtonconvertor import converter
from PORT_manger import Port_setter
from aphyt import omron
from robot_line import rec_ov,res_gri,gri_set,gri_op,final_rec
from PRO_FUSE_SOFT import  PRO_DATA_IN,PRO_SCREW_in,PRO_SCREW_out,Z_Homing,PRO_DATA_IN2,UUID_get
def LEDIndicator(key=None, radius=30):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key)

def SetLED(window, key, color,color1):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 20, fill_color=color, line_color=color1)

def LEDIndicator1(key=None, radius=150):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key)

def SetLED1(window, key, color,color1):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 2000, fill_color=color, line_color=color1)


def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

def colorblind(data):
    if 0 <= data < 1:
        c = 'green'
    elif 1 <= data < 2:
        c = 'forest green'
    elif 2 <= data < 3:
        c = 'dark green'
    elif 3 <= data < 4:
        c = 'olive drab'
    elif 4 <= data < 5:
        c = 'yellow3'
    elif 5 <= data < 6:
        c = 'yellow2'
    elif 6 <= data < 7:
        c = 'goldenrod1'
    elif 6 <= data < 7:
        c = 'DarkGoldenrod3'
    elif 7 <= data < 8:
        c = 'OrangeRed2'
    elif 8 <= data < 9:
        c = 'OrangeRed3'
    elif 9 <= data < 10:
        c = 'OrangeRed4'
    elif 9 <= data < 10:
        c = 'red4'
    elif  data >= 10:
        c = 'red4'
    else:
        c = 'green'
    return(c)

def gui1(puredata,puredata1,PORT,SES,con_sta,lad_sta,SYS):
    print(PORT)
    sg.theme('DarkTeal9')
    layout = [[sg.Text(''),sg.Text('                              '),sg.Text('')],[sg.Frame('Other options', [[sg.Frame('robot status', [[sg.Text(key='-OUTPUT-')]])],[sg.Frame('RESET DATA', [[sg.OK()]])]]),
               sg.Frame('Active Ports',[[sg.Text(key='-OUTPUT-1')], [sg.Text(key='-OUTPUT-2')], [sg.Text(key='-OUTPUT-3')]]),
               sg.Frame('Current tool used', [[sg.Frame('Gripper',[[LEDIndicator('GRIPPER')]]),sg.Frame('PRO-FUSE',[[LEDIndicator('PROFUSE')]]) ]]),
               ], [sg.Frame('Figure option', [[sg.OK(), sg.Cancel()]]),sg.Frame('Start application', [[sg.OK(), sg.Cancel()]]),
               sg.Frame('manual display', [[sg.OK(), sg.Cancel()]])], [sg.Frame('System Check',[[sg.Frame('Connection status',
               [[sg.Frame('Touchence sensors connection state', [[sg.Frame('Right sensor connection state',
               [[LEDIndicator('Sensors Right connection state')]]),sg.Frame('Left sensor connection state', [[LEDIndicator('Sensors Left connection state')]])]])],
               [sg.Frame('Device connection state', [[sg.Frame('Robotiq F2 85 Gripper connection state',
               [[LEDIndicator('Gripper connection state')]]),sg.Frame('Omron Techman cobot  connection state', [[LEDIndicator('Robot  connection state')]])]])],
               [sg.Frame('Data communication device',[[sg.Frame('NX1 connection state', [[LEDIndicator('NX1 connection state')]])]]),
               sg.Frame('Side hand device',[[sg.Frame('PRO-FUSE  connection state', [[LEDIndicator('PRO-FUSE  connection state')]])]])]])],
               [sg.Frame('Cycle status:', [[sg.Text('Cycle run  '), LEDIndicator('Button for Cycle run'), sg.Text('Indicator for Cycle run           '),
               LEDIndicator('Indicator for Cycle run')],[sg.Text('Cycle stop'), LEDIndicator('Button for Cycle Stop'),
               sg.Text('Indicator for Cycle Stop         '), LEDIndicator('Indicator for Cycle Stop')],]),]])]]

    gui = sg.Window(title="Collabrative Robot powered digital industrial screwdriver machine with conveyor", layout=layout,size=(700, 700), finalize=True,resizable=True)
    mean, mean_1, j,counter = [], [], 0,0
    SES[11] = 1
    while True:
        try:
            (event, values) = gui.read(timeout=0)
            if event == 'OK3':
                SES[26] = 1
            if event == 'Cancel4':
                SES[26] = 0
            if event == 'OK':
                 SYS[2] = 0
                 SYS[3] = 0
                 SYS[4] = 0
                 SYS[9] = 0
                 SYS[10] = 0

            if event == 'OK0':  SES[8] = 1
            if event == 'OK1' or lad_sta[0] == 1:
                SES[10] = 1
                lad_sta[3] = 1
                lad_sta[4] = 0
                lad_sta[5] = 0
                lad_sta[1] = 0
                SES[1] = 0
                SYS[0] = 1

            gui['-OUTPUT-1'].update('Gripper port =  ' + PORT[2].replace('/dev/','') )
            gui['-OUTPUT-2'].update('Sensor 1 port = ' + PORT[0].replace('/dev/',''))
            gui['-OUTPUT-3'].update('Sensor 2 port = ' + PORT[1].replace('/dev/',''))
            gui['-OUTPUT-'].update(SES[0])

            SetLED(gui, 'Button for Cycle run', 'green', 'blue' if lad_sta[0] == 1 else 'white')
            SetLED(gui, 'Button for Cycle Stop', 'yellow', 'blue' if lad_sta[1] == 1 else 'white')
            SetLED(gui, 'Indicator for Cycle run', 'green' if lad_sta[3] == 1 else 'Black', 'blue')
            SetLED(gui, 'Indicator for Cycle Stop', 'yellow' if lad_sta[4] == 1 else 'Black', 'blue')
            SetLED(gui, 'Sensors Right connection state', 'green' if con_sta[0] == 1 else 'Black', 'blue')
            SetLED(gui, 'Sensors Left connection state', 'green' if con_sta[1] == 1 else 'Black', 'blue')
            SetLED(gui, 'Gripper connection state', 'green' if con_sta[2] == 1 else 'Black', 'blue')
            SetLED(gui, 'Robot  connection state', 'green' if con_sta[3] == 1 else 'Black', 'blue')
            SetLED(gui, 'NX1 connection state', 'green' if con_sta[4] == 1 else 'Black', 'blue')
            SetLED(gui, 'PRO-FUSE  connection state', 'green' if con_sta[5] == 1 else 'Black', 'blue')
            SetLED(gui, 'GRIPPER', 'blue' if SES[15] == 'GRIPPER' else 'Black', 'blue')
            SetLED(gui, 'PROFUSE', 'blue' if SES[15] == 'SCREW' else 'Black', 'blue')
            if  lad_sta[1] == 1:
                lad_sta[3] = 0
                lad_sta[4] = 0
                lad_sta[5] = 1
                counter +=1
                SetLED(gui, 'Indicator for Cycle Stop', 'red' if  isprime(counter)==True  else 'Black','blue')
                time.sleep(0.3)

            mean.append(converter(puredata))
            mean_1.append(converter(puredata1))
            SES[2] = ((mean[j] + mean_1[j]) / 2)
            j += 1
            if event == 'Cancel':  SES[8] = 0
            if event == 'Cancel2'or lad_sta[1] == 1:
                lad_sta[4] = 1
                lad_sta[3] = 0
                lad_sta[5] = 0
                lad_sta[0] = 0
                con_sta[0] = 0
                SES[10] = 0
                SES[1] = 1
                SES[13] = 0
                SES[14] = 0
                SYS[0] = 2
            if event == sg.WIN_CLOSED:
                eip_instance = omron.n_series.NSeriesEIP()
                eip_instance.connect_explicit('192.168.251.1')
                eip_instance.register_session()
                eip_instance.update_variable_dictionary()
                reply = eip_instance.write_variable('YELLOW_Lamp', False)
                reply = eip_instance.write_variable('GREEN_Lamp', False)
                reply = eip_instance.write_variable('redl', False)
                reply = eip_instance.write_variable('buz', False)
                lad_sta = [0,0,0,0,0,0]
                lad_sta[4] = 1
                SES[8] = 0
                SES[10] = 0
                SES[1] = 1
                SES[12] = 1
                gui.close()
                os._exit(0)
                sys.exit()
                break

        except:
            break
            sys.exit()

    return ()


def Gui_figure(puredata,puredata1,SES,lad_sta):
    while True:

             while SES[28] == 1:
                 arrow1 = b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJDqqzN3fAAAET0lEQVR42u3du2oUYRiH8X88BbFSLKJIPBfaizaCVuYCxGsQPIB6BeIFCBG0sLTS2CiChVilUUGwShRBgkqMFipGFhKSrEUSWc3O7By+93u/zD6/qYe8s092nZ18M0oAAAAAAAAAAAAAAAAAAAAAAAAAAABOBjTgPYL9Ia4/uzSiY9qmj3qmF5r3HgerTuulFtRWW2390E3t8B4Iy87ow0qW5W1RN7XFeyisDbP8zjnlPRa6hWmrrRveg/W7rDBt3VuXJzONkR2mrTFt8B6vf+WFIY2j/DCkcdMrDGmc9A5DGhdFwjQ2TcoHdUZ3tN97CD/ppunzMOmm6fswqaYhjNJMQxhJKaYhzIrU0hDmr7TSEKZDSmkI84900hDmP6mkIcwaaaQhTBcppCFMV/5pCJPBOw1hMvmmIUwOzzSEyeWXhjA9eKUhTE8+aQhTgEcawhQSPw1hCoqdhjCFxU1DmBJipiFMKfHSEKakTZF+jmWYAW3SUqTjKGepzlxx7ueyfcdM67XaUY6jnAG1NKkneqNF71GyFFtU3tTti65p0DsBYbpvLZ33jkCYrG1Cw+VfOtszNM7Klh3SsfI7WaYhzKrN2l1+J7s0hOlU4XW2SkOY2mzSECYAizSECSJ8GsIEEjoNYYIJm4YwAYVMQ5igwqUhTGCh0hAmuDBpCGMgRBrCmKifhjBG6qYhjJl6aQhjqE4awpiqnoYwxqqmIYy5ammO6zZhrFVJM6grOuA9ePNVSbNPJ73H7gdV0uzSdu+x+0GVNPNa8B67H1RJM6VP3mP3gypppjWmFFfmN0y1k+fbeuQ9ePNVS/NNl/TYe/Smq3o14LMuEMdW9WtoxDFW58ozcUzV+3sNcQzV/SsncczUXxtAHCMhVtQQx0SYdWjEMRBq9SZxggu35pk4gYW8U4A4QYW9v4Y4AYW+K404wYS/l5M4gVjcAU2cIGyeG0CcAKyetkGc2uyeUUOcTnPld7F8shNxVs1qsvxOG01H+qVxDetIpCd8puu5bmnee4i1hvRAS+7P8fPc3upElRfO9l0jSb81rr06avrOSXVV3JJ+6qmu6lWVneN81AxpVGfNftZLjSYaZ15TmlTLe4x8lh9rY+7/GZ+JWAc1o8t6mOjvdqLi/b4Rp6SYHwXEKSXupzRxSoj9DyhxCot/bkOcgjxOO4lTiM83AuIU4PVljTg9+X2PJk4Pnpc4iJPL9+oTcXJ4XxgkTibvNMTJ5J+GOBlSSEOcrtJIQ5wuUklDnDXSSUOc/6SUhjj/SCsNcTqkloY4iSu3NKqhi51SVSYOaSIrHoc00RWNQxoHxeKQxkWROKRx0jsOadz0ikMaR/lxSOMqL84D0vjKjnPXezRkxbnoPRi6x5nQQe+xIElDuq/FjjBfdc57JKzaqet6r5bm9F3PNNLcU4D1+ByMDdqjw9qqGb3TrPcwAAAAAAAAAAAAAAAAAAAAAAAAAAAAOf4ADjxv42esgVgAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjItMDItMTdUMDI6MzY6NTgtMDU6MDBCD2qUAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIyLTAyLTE3VDAyOjM2OjU4LTA1OjAwM1LSKAAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAAASUVORK5CYII='
                 arrow2 = b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJSU+3+FrAAAEWUlEQVR42u3csY8UZRjH8d8dwh3Gk2uNCZBw5hICiSbYqBTYWUhDiAWJiTF3jYUhdHRoRcJfQKTmHyCxsbJQLFyIetFEAgnRSEMwiCIBdi1WAsvt7O288zzv+8zO97PdJe/OO+83e7Mz2RkJAAAAAAAAAAAAAAAAAAAAAAAAAAAgvDnNlZ5C6sRn17wO6D2tqq8f9aV+1aD0hDC0oE/1mwYaaKC+rulDbSs9JQyt6+//wwxfd7ROnAj2aGMkDHHCOK6Hm9IQJ4STY8K0LM586Qlk3q9lndXH7Ygzq2mqtSZO99K0Jk4X07QkTjfTtCJOV9O0IE5304SP0+U0weN0O03oOF1PEzgOacLGIY0UNA5phgLGIc0T4eKQ5qlgcUjzrFBxSDMqUBzSPC9MHNJsFiQOacYJEYc04wWIQ5oqxeOQplrhOKSZpGgc0kxWMA5ptlIsDmm2VigOaaZRJA5pplMgDmmmlT0OaaaXOQ5p6sga54VGo+eDpn3kNq9lnZV0QY/9dyI9zYre1xva5T/FBAOtuL13xjgp5nRMv6hfcVPe7L+y3HaYtoF39YX2zvTjICZb1GHd1lXfh0SkpNmpczpUaFGiWNRh3VNPfb9NpKRZ1Wm9VGxRoljUO7qn7/3ipKQ5qI+0veCiRLGgtz3jpHzJ3Nbho8yoJX2uTxqegFSKeV7SHo5xSNOUWxzSNOcUhzQWXOKQxoZDHNJYMY9DGjvGcUhjyTQOaWwZxiGNNbM4pLFnFIc0HkzikMaHQRzSeGkchzR+GsYhjadGcUjjq0Ec0nhb0mf6IGUgafy9rFN6pf4w0uSwP+XHYaTJYUF76g8iTR4P6g8hTQ5/aqP+INLk8JWu1h9EGn89ndE/9YeRxltPa/opZSBpfPW0pl7aUNJ4ahCGNJ4ahSGNn4ZhSOOlcRjS+DAIQxoPJmFIY88oDGmsmYUhjS3DMKSxZBqGNHaMw5DGinkY0thwCEMaCy5hSNOcUxjSNOUWJi3NfT0quhxxOIZJS3NTfxRcjjhcw6Q9dOuuduutYgsSxXda1xXPDaQ94PFnHdS+IgsSxWWt6QffTaSluauvtUOvamfgJ6N5zuxy6q9k8uzAdu3Tql70nmCSxzqqE27vniXM7Drl9iDhb3Ugzy5wXlNPxk8MaerI+q+MNNPLfIwhzbSyH/xJM50C38pIM40iX5dJs7VC5zGk2UqxE0zSTFbwzJ80kxS9JEOaaoWvlZGmSvGLmKQZr3gY0owXIAxpxgkRhjSbBQlDmueFCUOaUYHCkOZZocKQ5qlgYUjzRLgwpBkKGIY0UtAwpAkbhjRhw3Q9TeAw3U4TOkyX0wQP09004cN0NU0LwnQzTSvCzG6a6lu6WhJmdtPcr/h7a8LMriP6q+QdZai2pEuEiepNbYyE+YYwcbyui7qlB/pXv+u8Xis9nbri3vdvYVEr2q2+bui6HpaeDAAAAAAAAAAAAAAAAAAAAAAAAAAA6KD/AMzW2Dec5+CaAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTAyLTE3VDAyOjM3OjM3LTA1OjAwnep4xAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wMi0xN1QwMjozNzozNy0wNTowMOy3wHgAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC'
                 sg.theme('DarkTeal9')

                 layout = [[sg.Canvas( key='-CANVAS-2')],[sg.Text('                 ')],[[sg.Text(''), sg.Frame('', [[sg.Button('', image_data=arrow1,
                                                                               button_color=(
                                                                               sg.theme_background_color(),
                                                                               sg.theme_background_color()),
                                                                               border_width=0, key='Back2'),
                                                                     sg.Button('', image_data=arrow2,
                                                                               button_color=(
                                                                               sg.theme_background_color(),
                                                                               sg.theme_background_color()),
                                                                               border_width=0, key='Next2')]])]]]
                 gui = sg.Window(title="Live Feed figure", layout=layout,size= (1500, 900), finalize=True,
                             resizable=True,element_justification='c')
                 #gui.Maximize()
                 canvas_elem2 = gui['-CANVAS-2']
                 canvas2 = canvas_elem2.TKCanvas
                 fig2, (ax2, ax3) = plt.subplots(1, 2)
                 fig2.set_size_inches(15, 6)
                 ax2.grid()
                 ax3.grid()
                 fig_agg2 = draw_figure(canvas2, fig2)
                 mean, mean_1, xax, j = [], [], [], 0
                 while SES[28] == 1:
                     (event, values) = gui.read(timeout=0)
                     if event == 'Next2':
                         print(event)
                         SES[29] = 1
                         SES[28] = 0
                     if event == 'Back2':
                         print(event)
                         SES[28] = 0
                         SES[8] = 1
                     mean.append(converter(puredata))
                     mean_1.append(converter(puredata1))
                     j = j + 1
                     xax.append(j)
                     fig_agg2 = figure_draw_1(fig2, ax2, ax3, mean, mean_1, fig_agg2, j, xax)
                     fig_agg2.draw()
                     if SES[28] == 0:
                         gui.close()
                         break
                         sys.exit()
                     if event == sg.WIN_CLOSED:
                         SES[28] = 0
                         gui.close()
                         break
                         sys.exit()
                 if lad_sta[2] != 0:break

    return()


def Gui_figure1(puredata,puredata1,SES,lad_sta):
    data1 =[0,0,0,0,0,0,0,0]
    data =[0,0,0,0,0,0,0,0]
    while True:

             while SES[29] == 1:
                 arrow1 = b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJDqqzN3fAAAET0lEQVR42u3du2oUYRiH8X88BbFSLKJIPBfaizaCVuYCxGsQPIB6BeIFCBG0sLTS2CiChVilUUGwShRBgkqMFipGFhKSrEUSWc3O7By+93u/zD6/qYe8s092nZ18M0oAAAAAAAAAAAAAAAAAAAAAAAAAAABOBjTgPYL9Ia4/uzSiY9qmj3qmF5r3HgerTuulFtRWW2390E3t8B4Iy87ow0qW5W1RN7XFeyisDbP8zjnlPRa6hWmrrRveg/W7rDBt3VuXJzONkR2mrTFt8B6vf+WFIY2j/DCkcdMrDGmc9A5DGhdFwjQ2TcoHdUZ3tN97CD/ppunzMOmm6fswqaYhjNJMQxhJKaYhzIrU0hDmr7TSEKZDSmkI84900hDmP6mkIcwaaaQhTBcppCFMV/5pCJPBOw1hMvmmIUwOzzSEyeWXhjA9eKUhTE8+aQhTgEcawhQSPw1hCoqdhjCFxU1DmBJipiFMKfHSEKakTZF+jmWYAW3SUqTjKGepzlxx7ueyfcdM67XaUY6jnAG1NKkneqNF71GyFFtU3tTti65p0DsBYbpvLZ33jkCYrG1Cw+VfOtszNM7Klh3SsfI7WaYhzKrN2l1+J7s0hOlU4XW2SkOY2mzSECYAizSECSJ8GsIEEjoNYYIJm4YwAYVMQ5igwqUhTGCh0hAmuDBpCGMgRBrCmKifhjBG6qYhjJl6aQhjqE4awpiqnoYwxqqmIYy5ammO6zZhrFVJM6grOuA9ePNVSbNPJ73H7gdV0uzSdu+x+0GVNPNa8B67H1RJM6VP3mP3gypppjWmFFfmN0y1k+fbeuQ9ePNVS/NNl/TYe/Smq3o14LMuEMdW9WtoxDFW58ozcUzV+3sNcQzV/SsncczUXxtAHCMhVtQQx0SYdWjEMRBq9SZxggu35pk4gYW8U4A4QYW9v4Y4AYW+K404wYS/l5M4gVjcAU2cIGyeG0CcAKyetkGc2uyeUUOcTnPld7F8shNxVs1qsvxOG01H+qVxDetIpCd8puu5bmnee4i1hvRAS+7P8fPc3upElRfO9l0jSb81rr06avrOSXVV3JJ+6qmu6lWVneN81AxpVGfNftZLjSYaZ15TmlTLe4x8lh9rY+7/GZ+JWAc1o8t6mOjvdqLi/b4Rp6SYHwXEKSXupzRxSoj9DyhxCot/bkOcgjxOO4lTiM83AuIU4PVljTg9+X2PJk4Pnpc4iJPL9+oTcXJ4XxgkTibvNMTJ5J+GOBlSSEOcrtJIQ5wuUklDnDXSSUOc/6SUhjj/SCsNcTqkloY4iSu3NKqhi51SVSYOaSIrHoc00RWNQxoHxeKQxkWROKRx0jsOadz0ikMaR/lxSOMqL84D0vjKjnPXezRkxbnoPRi6x5nQQe+xIElDuq/FjjBfdc57JKzaqet6r5bm9F3PNNLcU4D1+ByMDdqjw9qqGb3TrPcwAAAAAAAAAAAAAAAAAAAAAAAAAAAAOf4ADjxv42esgVgAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjItMDItMTdUMDI6MzY6NTgtMDU6MDBCD2qUAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIyLTAyLTE3VDAyOjM2OjU4LTA1OjAwM1LSKAAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAAASUVORK5CYII='
                 arrow2 = b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJSU+3+FrAAAEWUlEQVR42u3csY8UZRjH8d8dwh3Gk2uNCZBw5hICiSbYqBTYWUhDiAWJiTF3jYUhdHRoRcJfQKTmHyCxsbJQLFyIetFEAgnRSEMwiCIBdi1WAsvt7O288zzv+8zO97PdJe/OO+83e7Mz2RkJAAAAAAAAAAAAAAAAAAAAAAAAAAAgvDnNlZ5C6sRn17wO6D2tqq8f9aV+1aD0hDC0oE/1mwYaaKC+rulDbSs9JQyt6+//wwxfd7ROnAj2aGMkDHHCOK6Hm9IQJ4STY8K0LM586Qlk3q9lndXH7Ygzq2mqtSZO99K0Jk4X07QkTjfTtCJOV9O0IE5304SP0+U0weN0O03oOF1PEzgOacLGIY0UNA5phgLGIc0T4eKQ5qlgcUjzrFBxSDMqUBzSPC9MHNJsFiQOacYJEYc04wWIQ5oqxeOQplrhOKSZpGgc0kxWMA5ptlIsDmm2VigOaaZRJA5pplMgDmmmlT0OaaaXOQ5p6sga54VGo+eDpn3kNq9lnZV0QY/9dyI9zYre1xva5T/FBAOtuL13xjgp5nRMv6hfcVPe7L+y3HaYtoF39YX2zvTjICZb1GHd1lXfh0SkpNmpczpUaFGiWNRh3VNPfb9NpKRZ1Wm9VGxRoljUO7qn7/3ipKQ5qI+0veCiRLGgtz3jpHzJ3Nbho8yoJX2uTxqegFSKeV7SHo5xSNOUWxzSNOcUhzQWXOKQxoZDHNJYMY9DGjvGcUhjyTQOaWwZxiGNNbM4pLFnFIc0HkzikMaHQRzSeGkchzR+GsYhjadGcUjjq0Ec0nhb0mf6IGUgafy9rFN6pf4w0uSwP+XHYaTJYUF76g8iTR4P6g8hTQ5/aqP+INLk8JWu1h9EGn89ndE/9YeRxltPa/opZSBpfPW0pl7aUNJ4ahCGNJ4ahSGNn4ZhSOOlcRjS+DAIQxoPJmFIY88oDGmsmYUhjS3DMKSxZBqGNHaMw5DGinkY0thwCEMaCy5hSNOcUxjSNOUWJi3NfT0quhxxOIZJS3NTfxRcjjhcw6Q9dOuuduutYgsSxXda1xXPDaQ94PFnHdS+IgsSxWWt6QffTaSluauvtUOvamfgJ6N5zuxy6q9k8uzAdu3Tql70nmCSxzqqE27vniXM7Drl9iDhb3Ugzy5wXlNPxk8MaerI+q+MNNPLfIwhzbSyH/xJM50C38pIM40iX5dJs7VC5zGk2UqxE0zSTFbwzJ80kxS9JEOaaoWvlZGmSvGLmKQZr3gY0owXIAxpxgkRhjSbBQlDmueFCUOaUYHCkOZZocKQ5qlgYUjzRLgwpBkKGIY0UtAwpAkbhjRhw3Q9TeAw3U4TOkyX0wQP09004cN0NU0LwnQzTSvCzG6a6lu6WhJmdtPcr/h7a8LMriP6q+QdZai2pEuEiepNbYyE+YYwcbyui7qlB/pXv+u8Xis9nbri3vdvYVEr2q2+bui6HpaeDAAAAAAAAAAAAAAAAAAAAAAAAAAA6KD/AMzW2Dec5+CaAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTAyLTE3VDAyOjM3OjM3LTA1OjAwnep4xAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wMi0xN1QwMjozNzozNy0wNTowMOy3wHgAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC'
                 sg.theme('DarkTeal9')

                 layout = [[sg.Canvas( key='-CANVAS-')],[sg.Text('                 ')],[[sg.Text(''), sg.Frame('', [[sg.Button('', image_data=arrow1,
                                                                               button_color=(
                                                                               sg.theme_background_color(),
                                                                               sg.theme_background_color()),
                                                                               border_width=0, key='Back1'),
                                                                     sg.Button('', image_data=arrow2,
                                                                               button_color=(
                                                                               sg.theme_background_color(),
                                                                               sg.theme_background_color()),
                                                                               border_width=0, key='Next1')]])]]]
                 gui = sg.Window(title="Live Feed figure", layout=layout,size=(800, 1000), finalize=True,
                             resizable=True,element_justification='c')
                 #gui.Maximize()
                 canvas_elem = gui['-CANVAS-']
                 canvas = canvas_elem.TKCanvas
                 fig = plt.figure()
                 fig.set_size_inches(8, 8)
                 ax = fig.add_subplot(projection='3d')
                 fig_agg = draw_figure(canvas, fig)
                 while SES[29] == 1:
                     (event, values) = gui.read(timeout=0)
                     if event == 'Next1':
                         print(event)
                         SES[30] = 1
                         SES[29] = 0
                     if event == 'Back1':
                         print(event)
                         SES[29] = 0
                         SES[28] = 1
                     puredata[4] = puredata[0]
                     puredata[5] = puredata[0]
                     for i in range(0, len(puredata)):
                         data[i] = puredata[i] * 7 / 250
                         data1[i] = puredata1[i] * 7 / 250
                     fig_agg = make_cube_ulti_new_oof(ax, data,data1, fig_agg, SES)
                     fig_agg.draw()

                     if SES[29] == 0:
                         gui.close()
                         break
                         sys.exit()
                     if event == sg.WIN_CLOSED:
                         SES[29] = 0
                         gui.close()
                         break
                         sys.exit()
             if lad_sta[2] != 0: break


    return()

def Gui_figure3(puredata,puredata1,SES,lad_sta):
    data = [0, 0, 0, 0, 0, 0, 0, 0]
    data1 = [0, 0, 0, 0, 0, 0, 0, 0]
    while True:
             while SES[30] == 1:
                arrow1= b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJDqqzN3fAAAET0lEQVR42u3du2oUYRiH8X88BbFSLKJIPBfaizaCVuYCxGsQPIB6BeIFCBG0sLTS2CiChVilUUGwShRBgkqMFipGFhKSrEUSWc3O7By+93u/zD6/qYe8s092nZ18M0oAAAAAAAAAAAAAAAAAAAAAAAAAAABOBjTgPYL9Ia4/uzSiY9qmj3qmF5r3HgerTuulFtRWW2390E3t8B4Iy87ow0qW5W1RN7XFeyisDbP8zjnlPRa6hWmrrRveg/W7rDBt3VuXJzONkR2mrTFt8B6vf+WFIY2j/DCkcdMrDGmc9A5DGhdFwjQ2TcoHdUZ3tN97CD/ppunzMOmm6fswqaYhjNJMQxhJKaYhzIrU0hDmr7TSEKZDSmkI84900hDmP6mkIcwaaaQhTBcppCFMV/5pCJPBOw1hMvmmIUwOzzSEyeWXhjA9eKUhTE8+aQhTgEcawhQSPw1hCoqdhjCFxU1DmBJipiFMKfHSEKakTZF+jmWYAW3SUqTjKGepzlxx7ueyfcdM67XaUY6jnAG1NKkneqNF71GyFFtU3tTti65p0DsBYbpvLZ33jkCYrG1Cw+VfOtszNM7Klh3SsfI7WaYhzKrN2l1+J7s0hOlU4XW2SkOY2mzSECYAizSECSJ8GsIEEjoNYYIJm4YwAYVMQ5igwqUhTGCh0hAmuDBpCGMgRBrCmKifhjBG6qYhjJl6aQhjqE4awpiqnoYwxqqmIYy5ammO6zZhrFVJM6grOuA9ePNVSbNPJ73H7gdV0uzSdu+x+0GVNPNa8B67H1RJM6VP3mP3gypppjWmFFfmN0y1k+fbeuQ9ePNVS/NNl/TYe/Smq3o14LMuEMdW9WtoxDFW58ozcUzV+3sNcQzV/SsncczUXxtAHCMhVtQQx0SYdWjEMRBq9SZxggu35pk4gYW8U4A4QYW9v4Y4AYW+K404wYS/l5M4gVjcAU2cIGyeG0CcAKyetkGc2uyeUUOcTnPld7F8shNxVs1qsvxOG01H+qVxDetIpCd8puu5bmnee4i1hvRAS+7P8fPc3upElRfO9l0jSb81rr06avrOSXVV3JJ+6qmu6lWVneN81AxpVGfNftZLjSYaZ15TmlTLe4x8lh9rY+7/GZ+JWAc1o8t6mOjvdqLi/b4Rp6SYHwXEKSXupzRxSoj9DyhxCot/bkOcgjxOO4lTiM83AuIU4PVljTg9+X2PJk4Pnpc4iJPL9+oTcXJ4XxgkTibvNMTJ5J+GOBlSSEOcrtJIQ5wuUklDnDXSSUOc/6SUhjj/SCsNcTqkloY4iSu3NKqhi51SVSYOaSIrHoc00RWNQxoHxeKQxkWROKRx0jsOadz0ikMaR/lxSOMqL84D0vjKjnPXezRkxbnoPRi6x5nQQe+xIElDuq/FjjBfdc57JKzaqet6r5bm9F3PNNLcU4D1+ByMDdqjw9qqGb3TrPcwAAAAAAAAAAAAAAAAAAAAAAAAAAAAOf4ADjxv42esgVgAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjItMDItMTdUMDI6MzY6NTgtMDU6MDBCD2qUAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIyLTAyLTE3VDAyOjM2OjU4LTA1OjAwM1LSKAAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAAASUVORK5CYII='
                arrow2= b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJSU+3+FrAAAEWUlEQVR42u3csY8UZRjH8d8dwh3Gk2uNCZBw5hICiSbYqBTYWUhDiAWJiTF3jYUhdHRoRcJfQKTmHyCxsbJQLFyIetFEAgnRSEMwiCIBdi1WAsvt7O288zzv+8zO97PdJe/OO+83e7Mz2RkJAAAAAAAAAAAAAAAAAAAAAAAAAAAgvDnNlZ5C6sRn17wO6D2tqq8f9aV+1aD0hDC0oE/1mwYaaKC+rulDbSs9JQyt6+//wwxfd7ROnAj2aGMkDHHCOK6Hm9IQJ4STY8K0LM586Qlk3q9lndXH7Ygzq2mqtSZO99K0Jk4X07QkTjfTtCJOV9O0IE5304SP0+U0weN0O03oOF1PEzgOacLGIY0UNA5phgLGIc0T4eKQ5qlgcUjzrFBxSDMqUBzSPC9MHNJsFiQOacYJEYc04wWIQ5oqxeOQplrhOKSZpGgc0kxWMA5ptlIsDmm2VigOaaZRJA5pplMgDmmmlT0OaaaXOQ5p6sga54VGo+eDpn3kNq9lnZV0QY/9dyI9zYre1xva5T/FBAOtuL13xjgp5nRMv6hfcVPe7L+y3HaYtoF39YX2zvTjICZb1GHd1lXfh0SkpNmpczpUaFGiWNRh3VNPfb9NpKRZ1Wm9VGxRoljUO7qn7/3ipKQ5qI+0veCiRLGgtz3jpHzJ3Nbho8yoJX2uTxqegFSKeV7SHo5xSNOUWxzSNOcUhzQWXOKQxoZDHNJYMY9DGjvGcUhjyTQOaWwZxiGNNbM4pLFnFIc0HkzikMaHQRzSeGkchzR+GsYhjadGcUjjq0Ec0nhb0mf6IGUgafy9rFN6pf4w0uSwP+XHYaTJYUF76g8iTR4P6g8hTQ5/aqP+INLk8JWu1h9EGn89ndE/9YeRxltPa/opZSBpfPW0pl7aUNJ4ahCGNJ4ahSGNn4ZhSOOlcRjS+DAIQxoPJmFIY88oDGmsmYUhjS3DMKSxZBqGNHaMw5DGinkY0thwCEMaCy5hSNOcUxjSNOUWJi3NfT0quhxxOIZJS3NTfxRcjjhcw6Q9dOuuduutYgsSxXda1xXPDaQ94PFnHdS+IgsSxWWt6QffTaSluauvtUOvamfgJ6N5zuxy6q9k8uzAdu3Tql70nmCSxzqqE27vniXM7Drl9iDhb3Ugzy5wXlNPxk8MaerI+q+MNNPLfIwhzbSyH/xJM50C38pIM40iX5dJs7VC5zGk2UqxE0zSTFbwzJ80kxS9JEOaaoWvlZGmSvGLmKQZr3gY0owXIAxpxgkRhjSbBQlDmueFCUOaUYHCkOZZocKQ5qlgYUjzRLgwpBkKGIY0UtAwpAkbhjRhw3Q9TeAw3U4TOkyX0wQP09004cN0NU0LwnQzTSvCzG6a6lu6WhJmdtPcr/h7a8LMriP6q+QdZai2pEuEiepNbYyE+YYwcbyui7qlB/pXv+u8Xis9nbri3vdvYVEr2q2+bui6HpaeDAAAAAAAAAAAAAAAAAAAAAAAAAAA6KD/AMzW2Dec5+CaAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTAyLTE3VDAyOjM3OjM3LTA1OjAwnep4xAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wMi0xN1QwMjozNzozNy0wNTowMOy3wHgAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC'
                sg.theme('DarkTeal9')

                layout = [[sg.Image('left.png',size= (120,100)),sg.Text('      '),sg.Image('right.png',size= (120,100))],
                          [LEDIndicator1('7'),LEDIndicator1('8'),sg.Text(''),LEDIndicator1('15'),LEDIndicator1('16')],
                          [LEDIndicator1('5'),LEDIndicator1('6'),sg.Text(''),LEDIndicator1('13'),LEDIndicator1('14')]
                          ,[LEDIndicator1('3'),LEDIndicator1('4'),sg.Text(''),LEDIndicator1('11'),LEDIndicator1('12')],
                          [LEDIndicator1('1'),LEDIndicator1('2'),sg.Text(''),LEDIndicator1('9'),LEDIndicator1('10')],[sg.Text('                   ')],
                          [[sg.Text(''), sg.Frame('', [[sg.Button('', image_data=arrow1,
                                                                               button_color=(
                                                                               sg.theme_background_color(),
                                                                               sg.theme_background_color()),
                                                                               border_width=0, key='Back'),
                                                                     sg.Button('', image_data=arrow2,
                                                                               button_color=(
                                                                               sg.theme_background_color(),
                                                                               sg.theme_background_color()),
                                                                               border_width=0, key='Next')]])]]
                          ]
                gui = sg.Window(title="HEATMAP", layout=layout,size=(640, 900), finalize=True,resizable=True,element_justification='c')
                #gui.Maximize()
                while SES[30] == 1:
                    (event, values) = gui.read(timeout=0)
                    if event == 'Next':
                        SES[30] = 0
                        SES[8] = 1
                        print(event)
                    if event == 'Back':
                        print(event)
                        SES[30] = 0
                        SES[29] = 1
                    puredata[4] = puredata[0]
                    puredata[5] = puredata[0]
                    for i in range(0, len(data)):
                        data[i] = puredata[i] * 11.6 / 250
                        data1[i] = puredata1[i] * 11.6 / 250

                    c1 = colorblind(data[0])
                    SetLED1(gui, '1', c1,  'black')
                    c2 = colorblind(data[4])
                    SetLED1(gui, '2', c2,  'black')
                    c3 = colorblind(data[1])
                    SetLED1(gui, '3', c3,  'black')
                    c4 = colorblind(data[5])
                    SetLED1(gui, '4', c4,  'black')
                    c5 = colorblind(data[2])
                    SetLED1(gui, '5', c5,  'black')
                    c6 = colorblind(data[6])
                    SetLED1(gui, '6', c6,  'black')
                    c7 = colorblind(data[3])
                    SetLED1(gui, '7', c7,  'black')
                    c8 = colorblind(data[7])
                    SetLED1(gui, '8',c8,  'black')

                    c9 = colorblind(data1[0])
                    SetLED1(gui, '9', c9, 'black')
                    c10 = colorblind(data1[4])
                    SetLED1(gui, '10', c10, 'black')
                    c11 = colorblind(data1[1])
                    SetLED1(gui, '11', c11, 'black')
                    c12 = colorblind(data1[5])
                    SetLED1(gui, '12', c12, 'black')
                    c13 = colorblind(data1[2])
                    SetLED1(gui, '13', c13, 'black')
                    c14 = colorblind(data1[6])
                    SetLED1(gui, '14', c14, 'black')
                    c15 = colorblind(data1[3])
                    SetLED1(gui, '15', c15, 'black')
                    c16 = colorblind(data1[7])
                    SetLED1(gui, '16', c16, 'black')


                    if event == sg.WIN_CLOSED:
                        SES[30] = 0
                        gui.close()
                    if SES[30] == 0:
                        gui.close()
                        break
                        sys.exit()
                    if event == sg.WIN_CLOSED:
                        gui.close()
                        break
                        sys.exit()
                if lad_sta[2] != 0: break


def Gui_manual(SES,lad_sta,con_sta,PORT):
    #eip_instance = omron.n_series.NSeriesEIP()
    #eip_instance.connect_explicit('192.168.251.1')
    #eip_instance.register_session()
    #eip_instance.update_variable_dictionary()
    while True:
             while SES[26] == 1:
                 sg.theme('DarkTeal9')

                 layout =  [[sg.Text('                                                               '),
                   sg.Frame('Cycle in motion', [[sg.Text('     '),LEDIndicator('Cycle')]])],
                   [sg.Frame('Picking options', [[sg.Frame('Gripper Options', [[sg.Frame('Grip Position options',
                   [[sg.Text('Grip check limit'),sg.Slider(range=(0, 250), orientation='h',default_value=240)]])],
                   [sg.Frame('Gripper Speed', [[sg.Text('Grip speed value'), sg.Slider(range=(0, 250), orientation='h', default_value=250)]])],
                   [sg.Frame('Gripper Force', [[sg.Text('Grip Torque value'),sg.Slider(range=(0, 250),orientation='h',default_value=250)]])]])],
                   [sg.Frame('Pick up options', [[sg.Frame('Pick options', [[sg.Text('Pick limit'),sg.Slider(range=(0, 250), orientation='h',default_value=160)]])],
                   [sg.Frame('Sensor options', [[sg.Text('Sensor check limit'),sg.Slider(range=(0, 12), orientation='h',default_value=2)]])]])]]),
                   sg.Frame('Device Manual control', [[sg.Frame('Manual options',[[sg.Frame('tool lock system manual control',[[sg.Frame('TOOL LOCK', [[sg.OK()]]),
                   sg.Frame('TOOL UNLOCK', [[sg.OK()]])]])],[sg.Frame('Saftey reset',[[sg.Frame('return robot', [[sg.OK()]])]]),
                   sg.Frame('screw row select',[[sg.Frame('Row 1', [[sg.OK()]]),sg.Frame('Row 2', [[sg.OK()]])]])]]
                                    )],
                   [sg.Frame('Gripper',[[sg.Frame('Gripper set', [[sg.OK()]]),sg.Frame('Gripper open ', [[sg.OK()]])],
                   [sg.Slider(range=(0, 250), orientation='h', default_value=0)]])],
                   [sg.Frame('Side hand  manual control', [[sg.Frame('Screw in command', [[sg.OK(), LEDIndicator('screw in')]]),
                   sg.Frame('Screw out command', [[sg.OK(), LEDIndicator('screw out')]])]])],
                   [sg.Frame('Convyor Manual control',[[sg.Frame('Convyor ENTER',
                   [[sg.OK()]]),sg.Frame('Convyor EXIT', [[sg.OK()]])]])]])]]

                 gui = sg.Window(title="Manual control", layout=layout, finalize=True,
                             resizable=True)

                 while SES[26] == 1:
                     (event, values) = gui.read(timeout=0)
                     SetLED(gui, 'screw in', 'blue' if con_sta[6] == 1 else 'Black', 'blue')
                     SetLED(gui, 'screw out', 'blue' if con_sta[7] == 1 else 'Black', 'blue')
                     SetLED(gui, 'Cycle', 'Green' if SES[27] == 1 else 'Yellow', 'blue')
                     if (event == 'OK8') & (SES[10] == 0):
                         if SES[27] == 0:
                             print('ENTER')
                             reply = eip_instance.write_variable('Condi', 0)
                             time.sleep(0.1)
                             reply = eip_instance.write_variable('Condi', 2)
                             time.sleep(0.1)
                     if (event == 'OK9') & (SES[10] == 0):
                         if SES[27] == 0:
                             print('EXIT')
                             reply = eip_instance.write_variable('Condi', 0)
                             time.sleep(0.1)
                             reply = eip_instance.write_variable('Condi', 1)
                             time.sleep(0.1)
                     if (event == 'OK6') & (SES[10] == 0):
                         if SES[27] == 0:
                             con_sta[6] = 1
                             PRO_SCREW_in()
                             con_sta[6] = 0
                     if (event == 'OK7') & (SES[10] == 0):
                         if SES[27] == 0:
                             con_sta[7] = 1
                             PRO_SCREW_out()
                             con_sta[7] = 0
                     if event == 'OK':
                         if SES[27] == 0:
                             print('ok we good 3')
                             ######## Gripper tool
                             try:
                                Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
                             except:
                                 time.sleep(2)
                                 print('try again')
                             ######### drill tool
                             try:
                                Tool_sensor2 = eip_instance.read_variable('t2')
                             except:
                                 time.sleep(2)
                                 print('try again')
                             if Tool_sensor1 == False and Tool_sensor2 == False:
                                 try:
                                     reply = eip_instance.write_variable('tol', False)
                                     reply = eip_instance.write_variable('toolu', False)
                                     reply = eip_instance.write_variable('toolu', True)
                                 except:
                                     time.sleep(2)
                                     print('try again')
                     if event == 'OK0':
                         if SES[27] == 0:
                             print('ok we good 4')
                             ######### gripper tool
                             try:
                                 Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
                             except:
                                 time.sleep(2)
                                 print('try again')
                                 ######### drill tool
                             try:
                                 Tool_sensor2 = eip_instance.read_variable('t2')
                             except:
                                 time.sleep(2)
                                 print('try again')
                             if Tool_sensor1 == False and Tool_sensor2 == False:
                                 try:
                                    reply = eip_instance.write_variable('tol', False)
                                    reply = eip_instance.write_variable('toolu', False)
                                    reply = eip_instance.write_variable('tol', True)
                                 except:
                                     time.sleep(2)
                                     print('try again')
                     if event == 'OK1':
                         if SES[27] == 0:
                             print('ok we good 5')
                             final_rec()
                     if event == 'OK2':
                             if SES[27] == 0:
                                 print('row 1')
                                 SES[25] = 0
                     if event == 'OK3':
                         if SES[27] == 0:
                             print('row 2')
                             SES[25] = 1
                     if values != None:
                         SES[3], SES[4], SES[5], SES[6], SES[7] = values[0], values[4], values[3], values[1], values[2]

                     if event == 'OK4':
                         if SES[27] == 0:
                             print('ok we good 1')
                             gri_set(PORT)
                     if event == 'OK5':
                         if SES[27] == 0:
                             print('ok we good 2')
                             gri_op(PORT, int(values[5]))

                     if SES[26] == 0:
                         gui.close()
                         break
                         sys.exit()
                     if event == sg.WIN_CLOSED:
                         SES[26] = 0
                         gui.close()
                         break
                         sys.exit()
             if lad_sta[2] != 0: break
    return()
def gui_display(PORT,SES,con_sta,lad_sta):
    while True:
             while SES[8] == 1:
                arrow1= b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJDqqzN3fAAAET0lEQVR42u3du2oUYRiH8X88BbFSLKJIPBfaizaCVuYCxGsQPIB6BeIFCBG0sLTS2CiChVilUUGwShRBgkqMFipGFhKSrEUSWc3O7By+93u/zD6/qYe8s092nZ18M0oAAAAAAAAAAAAAAAAAAAAAAAAAAABOBjTgPYL9Ia4/uzSiY9qmj3qmF5r3HgerTuulFtRWW2390E3t8B4Iy87ow0qW5W1RN7XFeyisDbP8zjnlPRa6hWmrrRveg/W7rDBt3VuXJzONkR2mrTFt8B6vf+WFIY2j/DCkcdMrDGmc9A5DGhdFwjQ2TcoHdUZ3tN97CD/ppunzMOmm6fswqaYhjNJMQxhJKaYhzIrU0hDmr7TSEKZDSmkI84900hDmP6mkIcwaaaQhTBcppCFMV/5pCJPBOw1hMvmmIUwOzzSEyeWXhjA9eKUhTE8+aQhTgEcawhQSPw1hCoqdhjCFxU1DmBJipiFMKfHSEKakTZF+jmWYAW3SUqTjKGepzlxx7ueyfcdM67XaUY6jnAG1NKkneqNF71GyFFtU3tTti65p0DsBYbpvLZ33jkCYrG1Cw+VfOtszNM7Klh3SsfI7WaYhzKrN2l1+J7s0hOlU4XW2SkOY2mzSECYAizSECSJ8GsIEEjoNYYIJm4YwAYVMQ5igwqUhTGCh0hAmuDBpCGMgRBrCmKifhjBG6qYhjJl6aQhjqE4awpiqnoYwxqqmIYy5ammO6zZhrFVJM6grOuA9ePNVSbNPJ73H7gdV0uzSdu+x+0GVNPNa8B67H1RJM6VP3mP3gypppjWmFFfmN0y1k+fbeuQ9ePNVS/NNl/TYe/Smq3o14LMuEMdW9WtoxDFW58ozcUzV+3sNcQzV/SsncczUXxtAHCMhVtQQx0SYdWjEMRBq9SZxggu35pk4gYW8U4A4QYW9v4Y4AYW+K404wYS/l5M4gVjcAU2cIGyeG0CcAKyetkGc2uyeUUOcTnPld7F8shNxVs1qsvxOG01H+qVxDetIpCd8puu5bmnee4i1hvRAS+7P8fPc3upElRfO9l0jSb81rr06avrOSXVV3JJ+6qmu6lWVneN81AxpVGfNftZLjSYaZ15TmlTLe4x8lh9rY+7/GZ+JWAc1o8t6mOjvdqLi/b4Rp6SYHwXEKSXupzRxSoj9DyhxCot/bkOcgjxOO4lTiM83AuIU4PVljTg9+X2PJk4Pnpc4iJPL9+oTcXJ4XxgkTibvNMTJ5J+GOBlSSEOcrtJIQ5wuUklDnDXSSUOc/6SUhjj/SCsNcTqkloY4iSu3NKqhi51SVSYOaSIrHoc00RWNQxoHxeKQxkWROKRx0jsOadz0ikMaR/lxSOMqL84D0vjKjnPXezRkxbnoPRi6x5nQQe+xIElDuq/FjjBfdc57JKzaqet6r5bm9F3PNNLcU4D1+ByMDdqjw9qqGb3TrPcwAAAAAAAAAAAAAAAAAAAAAAAAAAAAOf4ADjxv42esgVgAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjItMDItMTdUMDI6MzY6NTgtMDU6MDBCD2qUAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIyLTAyLTE3VDAyOjM2OjU4LTA1OjAwM1LSKAAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAAASUVORK5CYII='
                arrow2= b'iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAQAAACxtTziAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQfmAhECJSU+3+FrAAAEWUlEQVR42u3csY8UZRjH8d8dwh3Gk2uNCZBw5hICiSbYqBTYWUhDiAWJiTF3jYUhdHRoRcJfQKTmHyCxsbJQLFyIetFEAgnRSEMwiCIBdi1WAsvt7O288zzv+8zO97PdJe/OO+83e7Mz2RkJAAAAAAAAAAAAAAAAAAAAAAAAAAAgvDnNlZ5C6sRn17wO6D2tqq8f9aV+1aD0hDC0oE/1mwYaaKC+rulDbSs9JQyt6+//wwxfd7ROnAj2aGMkDHHCOK6Hm9IQJ4STY8K0LM586Qlk3q9lndXH7Ygzq2mqtSZO99K0Jk4X07QkTjfTtCJOV9O0IE5304SP0+U0weN0O03oOF1PEzgOacLGIY0UNA5phgLGIc0T4eKQ5qlgcUjzrFBxSDMqUBzSPC9MHNJsFiQOacYJEYc04wWIQ5oqxeOQplrhOKSZpGgc0kxWMA5ptlIsDmm2VigOaaZRJA5pplMgDmmmlT0OaaaXOQ5p6sga54VGo+eDpn3kNq9lnZV0QY/9dyI9zYre1xva5T/FBAOtuL13xjgp5nRMv6hfcVPe7L+y3HaYtoF39YX2zvTjICZb1GHd1lXfh0SkpNmpczpUaFGiWNRh3VNPfb9NpKRZ1Wm9VGxRoljUO7qn7/3ipKQ5qI+0veCiRLGgtz3jpHzJ3Nbho8yoJX2uTxqegFSKeV7SHo5xSNOUWxzSNOcUhzQWXOKQxoZDHNJYMY9DGjvGcUhjyTQOaWwZxiGNNbM4pLFnFIc0HkzikMaHQRzSeGkchzR+GsYhjadGcUjjq0Ec0nhb0mf6IGUgafy9rFN6pf4w0uSwP+XHYaTJYUF76g8iTR4P6g8hTQ5/aqP+INLk8JWu1h9EGn89ndE/9YeRxltPa/opZSBpfPW0pl7aUNJ4ahCGNJ4ahSGNn4ZhSOOlcRjS+DAIQxoPJmFIY88oDGmsmYUhjS3DMKSxZBqGNHaMw5DGinkY0thwCEMaCy5hSNOcUxjSNOUWJi3NfT0quhxxOIZJS3NTfxRcjjhcw6Q9dOuuduutYgsSxXda1xXPDaQ94PFnHdS+IgsSxWWt6QffTaSluauvtUOvamfgJ6N5zuxy6q9k8uzAdu3Tql70nmCSxzqqE27vniXM7Drl9iDhb3Ugzy5wXlNPxk8MaerI+q+MNNPLfIwhzbSyH/xJM50C38pIM40iX5dJs7VC5zGk2UqxE0zSTFbwzJ80kxS9JEOaaoWvlZGmSvGLmKQZr3gY0owXIAxpxgkRhjSbBQlDmueFCUOaUYHCkOZZocKQ5qlgYUjzRLgwpBkKGIY0UtAwpAkbhjRhw3Q9TeAw3U4TOkyX0wQP09004cN0NU0LwnQzTSvCzG6a6lu6WhJmdtPcr/h7a8LMriP6q+QdZai2pEuEiepNbYyE+YYwcbyui7qlB/pXv+u8Xis9nbri3vdvYVEr2q2+bui6HpaeDAAAAAAAAAAAAAAAAAAAAAAAAAAA6KD/AMzW2Dec5+CaAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTAyLTE3VDAyOjM3OjM3LTA1OjAwnep4xAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wMi0xN1QwMjozNzozNy0wNTowMOy3wHgAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC'
                sg.theme('DarkTeal9')

                layout = [[sg.Text(''),sg.Text('                                                  ')],
                          [ sg.Text(''),sg.Frame('',[[sg.Image('display.png',size= (371,181))],[sg.Text('              '),sg.Frame('',[[
                                                                        sg.Button('', image_data=arrow2,button_color=(sg.theme_background_color(),
                                                                                      sg.theme_background_color()),
                                                                                  border_width=0, key='Next3')]])]])]
]
                gui = sg.Window(title="Touchsense user interface", layout=layout,size=(1500, 900), finalize=True,resizable=True,element_justification='c')
                #gui.Maximize()
                mean, mean_1, j,counter = [], [], 0,0
                SES[11] = 1
                while True:
                        (event, values) = gui.read(timeout=0)
                        if event == 'Next3':
                            print(event)
                            SES[28] = 1
                            SES[8] = 0
                        if event == 'Back3':
                            print(event)
                        if  lad_sta[1] == 1:
                            SES[8] = 0
                            counter +=1
                        if SES[8] == 0:
                            gui.close()
                            break
                            sys.exit()
                        if event == sg.WIN_CLOSED:
                            SES[8] = 0
                            gui.close()
                            break
                            sys.exit()
             if lad_sta[2] != 0: break




    return ()
