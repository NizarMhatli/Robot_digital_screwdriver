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
    graph.draw_circle((0, 0), 1000, fill_color=color, line_color=color1)


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
    #PORT = Port_setter(PORT)
    print(PORT)
    eip_instance = omron.n_series.NSeriesEIP()
    eip_instance.connect_explicit('192.168.251.1')
    eip_instance.register_session()
    eip_instance.update_variable_dictionary()
    layout = [[sg.Frame('Other options', [[sg.Frame('robot status', [[sg.Text(key='-OUTPUT-')]])],[sg.Frame('Figure option', [[sg.OK(), sg.Cancel()]])]]),
               sg.Frame('Active Ports',[[sg.Text(key='-OUTPUT-1')], [sg.Text(key='-OUTPUT-2')], [sg.Text(key='-OUTPUT-3')]]),
               sg.Frame('Start application', [[sg.OK(), sg.Cancel()]]),
               sg.Frame('Side hand  manual control', [[sg.Frame('Screw in command',[[sg.OK(),LEDIndicator('screw in')]]),
                                                       sg.Frame('Screw out command',[[sg.OK(),LEDIndicator('screw out')]])
            ]]),sg.Frame('Current tool used', [[sg.Frame('Gripper',[[LEDIndicator('GRIPPER')]]),
                                                       sg.Frame('PRO-EDGE',[[LEDIndicator('PROEDGE')]]) ]]),
               ],[ sg.Frame('Rest options',
                        [[sg.Frame('RESET DATA', [[sg.OK()]])
                          ]]),sg.Frame('Gripper',
                        [[sg.Frame('Gripper set', [[sg.OK()]]),
                          sg.Frame('Gripper open ', [[sg.OK()]]),
                          sg.Slider(range=(0, 250), orientation='h', default_value=0)
                          ]])]
             , [sg.Frame('Menu', [[sg.Frame('Gripper Options', [[sg.Frame('Grip Position options',
               [[sg.Text('Grip check limit'),sg.Slider(range=(0, 250), orientation='h',default_value=240)]])]
            ,  [sg.Frame('Gripper Speed', [[sg.Text('Grip speed value'), sg.Slider(range=(0, 250), orientation='h', default_value=250)]])],
               [sg.Frame('Gripper Force', [[sg.Text('Grip Torque value'),sg.Slider(range=(0, 250),orientation='h',default_value=250)]])]])],
               [sg.Frame('Pick up options', [[sg.Frame('Pick options', [[sg.Text('Pick limit'),sg.Slider(range=(0, 250), orientation='h',default_value=160)]])],
               [sg.Frame('Sensor options', [[sg.Text('Sensor check limit'),sg.Slider(range=(0, 12), orientation='h',default_value=2)]])]])]]),
                sg.Frame('System Check',
                [[sg.Frame('Connection status',
                        [[sg.Frame('Sensor connection state', [[sg.Frame('Sensors Right connection state',
                        [[LEDIndicator('Sensors Right connection state')]]),sg.Frame('Sensors Left connection state', [[LEDIndicator('Sensors Left connection state')]])]])],
                        [sg.Frame('Device connection state', [[sg.Frame('Gripper connection state',
                        [[LEDIndicator('Gripper connection state')]]),sg.Frame('Robot  connection state', [[LEDIndicator('Robot  connection state')]])]])],
                        [sg.Frame('Data communication device',[[sg.Frame('NX1 connection state', [[LEDIndicator('NX1 connection state')]])]]),
                         sg.Frame('Side hand device',[[sg.Frame('PRO-EDGE  connection state', [[LEDIndicator('PRO-EDGE  connection state')]])]])
                         ]])],
                 [sg.Frame('Cycle status:', [
                     [sg.Text('Cycle run  '), LEDIndicator('Button for Cycle run'), sg.Text('Indicator for Cycle run           '), LEDIndicator('Indicator for Cycle run')],
                     [sg.Text('Cycle stop'), LEDIndicator('Button for Cycle Stop'),sg.Text('Indicator for Cycle Stop         '), LEDIndicator('Indicator for Cycle Stop')],
                     ]),
                  ]
                 ]),sg.Frame('Manual options',
                         [[sg.Frame('Saftey Timer setting',
                                        [[sg.Slider(range=(0, 100), orientation='h',default_value=50),
                                          ]])],[sg.Frame('tool lock system manual control',
                        [[sg.Frame('TOOL LOCK', [[sg.OK()]]),
                          sg.Frame('TOOL UNLOCK', [[sg.OK()]])
                          ]])],[sg.Frame('Saftey reset',
                        [[sg.Frame('return robot', [[sg.OK()]])
                          ]])],[sg.Frame('screw row select',
                        [[sg.Frame('Row 1', [[sg.OK()]]),
                          sg.Frame('Row 2', [[sg.OK()]])
                          ]])]])]]



    gui = sg.Window(title="Touchsense user interface", layout=layout,size=(1300, 700), finalize=True,resizable=True)
    mean, mean_1, j,counter = [], [], 0,0
    SES[11] = 1
    while True:
        #try:
            (event, values) = gui.read(timeout=0)
            if event == 'OK5':
                 print('ok we good 1')
                 gri_set(PORT)
            if event == 'OK6':
                print('ok we good 2')
                gri_op(PORT,int(values[0]))
            if event == 'OK4':
                 SYS[2] = 0
                 SYS[3] = 0
                 SYS[4] = 0
                 SYS[9] = 0
                 SYS[10] = 0
            if event == 'OK7':
                print('ok we good 3')
                ######## Gripper tool
                Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
                ######### drill tool
                Tool_sensor2 = eip_instance.read_variable('t2')
                if Tool_sensor1 == False and Tool_sensor2 == False:
                    reply = eip_instance.write_variable('tol', False)
                    reply = eip_instance.write_variable('toolu', False)
                    reply = eip_instance.write_variable('toolu', True)
            if event == 'OK8':
                print('ok we good 4')
                ######## Gripper tool
                Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
                ######### drill tool
                Tool_sensor2 = eip_instance.read_variable('t2')
                if Tool_sensor1 == False and Tool_sensor2 == False:
                    reply = eip_instance.write_variable('tol', False)
                    reply = eip_instance.write_variable('toolu', False)
                    reply = eip_instance.write_variable('tol', True)
            if event == 'OK9':
                print('ok we good 5')
                final_rec()
            if event == 'OK9':
                print('ok we good 5')
                final_rec()
            if event == 'OK10':
                print('row 1')
                SES[25] = 0
            if event == 'OK11':
                print('row 2')
                SES[25] = 1
            if event == 'OK':  SES[8] = 1
            if event == 'OK0' or lad_sta[0] == 1:
                SES[10] = 1
                lad_sta[3] = 1
                lad_sta[4] = 0
                lad_sta[5] = 0
                lad_sta[1] = 0
                SES[1] = 0
                SYS[0] = 1
            if (event == 'OK2') & (SES[10] == 1):  SES[13] = 1
            if (event == 'OK3') & (SES[10] == 1):  SES[14] = 1

            if 0 <= values[6] <= 9 :
                SES[23] = 10
                SES[24] = 10
            elif  10 <= values[6] <= 29:
                SES[23] = 5
                SES[24] = 5
            elif 30 <= values[6] <= 49 :
                SES[23] = 3
                SES[24] = 3
            elif 50 <= values[6] <= 69 :
                SES[23] = 1
                SES[24] = 0.7
            elif 70 <= values[6] <= 79 :
                SES[23] = 1
                SES[24] = 0.5
            else:
                SES[23] = 10
                SES[24] = 10
            gui['-OUTPUT-1'].update('Gripper port =  ' + PORT[2].replace('/dev/tty','') )
            gui['-OUTPUT-2'].update('Sensor 1 port = ' + PORT[0].replace('/dev/tty',''))
            gui['-OUTPUT-3'].update('Sensor 2 port = ' + PORT[1].replace('/dev/tty',''))
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
            SetLED(gui, 'PRO-EDGE  connection state', 'green' if con_sta[5] == 1 else 'Black', 'blue')
            SetLED(gui, 'screw in', 'blue' if con_sta[6] == 1 else 'Black', 'blue')
            SetLED(gui, 'screw out', 'blue' if con_sta[7] == 1 else 'Black', 'blue')
            SetLED(gui, 'GRIPPER', 'blue' if SES[15] == 'GRIPPER' else 'Black', 'blue')
            SetLED(gui, 'PROEDGE', 'blue' if SES[15] == 'SCREW' else 'Black', 'blue')
            if  lad_sta[1] == 1:
                SES[8] = 0
                lad_sta[3] = 0
                lad_sta[4] = 0
                lad_sta[5] = 1
                counter +=1
                SetLED(gui, 'Indicator for Cycle Stop', 'red' if  isprime(counter)==True  else 'Black','blue')
                time.sleep(0.3)
            if values != None:
                SES[3], SES[4], SES[5], SES[6], SES[7] = values[1], values[5],values[4],values[2],values[3]
            mean.append(converter(puredata))
            mean_1.append(converter(puredata1))
            SES[2] = ((mean[j] + mean_1[j]) / 2)
            j += 1
            if event == 'Cancel':  SES[8] = 0
            if event == 'Cancel1'or lad_sta[1] == 1:
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
                lad_sta = [0,0,0,0,0,0]
                lad_sta[4] = 1
                SES[8] = 0
                SES[10] = 0
                SES[1] = 1
                SES[12] = 1
                eip_instance = omron.n_series.NSeriesEIP()
                eip_instance.connect_explicit('192.168.251.1')
                eip_instance.register_session()
                eip_instance.update_variable_dictionary()
                reply = eip_instance.write_variable('YELLOW_Lamp', False)
                reply = eip_instance.write_variable('GREEN_Lamp', False)
                reply = eip_instance.write_variable('redl', False)
                reply = eip_instance.write_variable('buz', False)
                gui.close()
                os._exit(0)
                sys.exit()
                break
        #except:
            #break
            #sys.exit()

    return ()


def Gui_figure(puredata,puredata1,SES,lad_sta):
    while True:
        try:
             while SES[8] == 1:
                 layout = [[sg.Canvas( key='-CANVAS-2')]]
                 gui = sg.Window(title="Live Feed figure", layout=layout, finalize=True,
                             resizable=True)
                 canvas_elem2 = gui['-CANVAS-2']
                 canvas2 = canvas_elem2.TKCanvas
                 fig2, (ax2, ax3) = plt.subplots(1, 2)
                 fig2.set_size_inches(10, 4)
                 ax2.grid()
                 ax3.grid()
                 fig_agg2 = draw_figure(canvas2, fig2)
                 mean, mean_1, xax, j = [], [], [], 0
                 while SES[8] == 1:
                     (event, values) = gui.read(timeout=0)
                     mean.append(converter(puredata))
                     mean_1.append(converter(puredata1))
                     j = j + 1
                     xax.append(j)
                     fig_agg2 = figure_draw_1(fig2, ax2, ax3, mean, mean_1, fig_agg2, j, xax)
                     fig_agg2.draw()
                     if SES[8] == 0:
                         gui.close()
                         break
                         sys.exit()
                     if event == sg.WIN_CLOSED:
                         gui.close()
                         break
                         sys.exit()
                 if lad_sta[2] != 0:break
        except:
            sys.exit()
    return()


def Gui_figure1(puredata,puredata1,SES,lad_sta):
    data1 =[0,0,0,0,0,0,0,0]
    data =[0,0,0,0,0,0,0,0]
    while True:

             while SES[8] == 1:
                 layout = [[sg.Canvas( key='-CANVAS-')]]
                 gui = sg.Window(title="Live Feed figure", layout=layout, finalize=True,
                             resizable=True)
                 canvas_elem = gui['-CANVAS-']
                 canvas = canvas_elem.TKCanvas
                 fig = plt.figure()
                 fig.set_size_inches(6, 6)
                 ax = fig.add_subplot(projection='3d')
                 fig_agg = draw_figure(canvas, fig)
                 while SES[8] == 1:
                     (event, values) = gui.read(timeout=0)
                     for i in range(0, len(puredata)):
                         data[i] = puredata[i] * 7 / 250
                         data1[i] = puredata1[i] * 7 / 250
                     fig_agg = make_cube_ulti_new_oof(ax, data,data1, fig_agg, SES)
                     fig_agg.draw()

                     if SES[8] == 0:
                         gui.close()
                         break
                         sys.exit()
                     if event == sg.WIN_CLOSED:
                         gui.close()
                         break
                         sys.exit()
             if lad_sta[2] != 0: break


    return()

def Gui_figure3(puredata,puredata1,SES,lad_sta):
    data = [0, 0, 0, 0, 0, 0, 0, 0]
    data1 = [0, 0, 0, 0, 0, 0, 0, 0]
    while True:
             while SES[8] == 1:
                layout = [[LEDIndicator1('7'),LEDIndicator1('8'),sg.Text(''),LEDIndicator1('15'),LEDIndicator1('16')],
                          [LEDIndicator1('5'),LEDIndicator1('6'),sg.Text(''),LEDIndicator1('13'),LEDIndicator1('14')]
                          ,[LEDIndicator1('3'),LEDIndicator1('4'),sg.Text(''),LEDIndicator1('11'),LEDIndicator1('12')],
                          [LEDIndicator1('1'),LEDIndicator1('2'),sg.Text(''),LEDIndicator1('9'),LEDIndicator1('10')],
                          [sg.Text(''),sg.Text('Left sensor',size=(30,30),justification='center'),sg.Text('',size=(10,10)),sg.Text('Right sensor',size=(30,30),justification='center')]]

                gui = sg.Window(title="HEATMAP", layout=layout,size=(660, 660), finalize=True,resizable=True)
                while SES[8] == 1:
                    (event, values) = gui.read(timeout=0)
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
                        gui.close()
                    if SES[8] == 0:
                        gui.close()
                        break
                        sys.exit()
                    if event == sg.WIN_CLOSED:
                        gui.close()
                        break
                        sys.exit()
                if lad_sta[2] != 0: break

