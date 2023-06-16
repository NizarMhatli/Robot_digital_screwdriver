
layout = [[sg.Frame('Side hand  manual control', [[sg.Frame('Screw in command', [[sg.OK(), LEDIndicator('screw in')]]),
                                        sg.Frame('Screw out command', [[sg.OK(), LEDIndicator('screw out')]])
                                        ]])],
          [[sg.Frame('Rest options',
                     []), sg.Frame('Gripper',
                                   [[sg.Frame('Gripper set', [[sg.OK()]]),
                                     sg.Frame('Gripper open ', [[sg.OK()]]),
                                     sg.Slider(range=(0, 250), orientation='h', default_value=0)
                                     ]])]],
[sg.Frame('Menu', [[sg.Frame('Gripper Options', [[sg.Frame('Grip Position options',
               [[sg.Text('Grip check limit'),sg.Slider(range=(0, 250), orientation='h',default_value=240)]])]
            ,  [sg.Frame('Gripper Speed', [[sg.Text('Grip speed value'), sg.Slider(range=(0, 250), orientation='h', default_value=250)]])],
               [sg.Frame('Gripper Force', [[sg.Text('Grip Torque value'),sg.Slider(range=(0, 250),orientation='h',default_value=250)]])]])],
               [sg.Frame('Pick up options', [[sg.Frame('Pick options', [[sg.Text('Pick limit'),sg.Slider(range=(0, 250), orientation='h',default_value=160)]])],
               [sg.Frame('Sensor options', [[sg.Text('Sensor check limit'),sg.Slider(range=(0, 12), orientation='h',default_value=2)]])]])]])],
[sg.Frame('Manual options',
                         [[],[sg.Frame('tool lock system manual control',
                        [[sg.Frame('TOOL LOCK', [[sg.OK()]]),
                          sg.Frame('TOOL UNLOCK', [[sg.OK()]])
                          ]])],[sg.Frame('Saftey reset',
                        [[sg.Frame('return robot', [[sg.OK()]])
                          ]])],[sg.Frame('screw row select',
                        [[sg.Frame('Row 1', [[sg.OK()]]),
                          sg.Frame('Row 2', [[sg.OK()]])
                          ]])]])],
         ]

SetLED(gui, 'screw in', 'blue' if con_sta[6] == 1 else 'Black', 'blue')
SetLED(gui, 'screw out', 'blue' if con_sta[7] == 1 else 'Black', 'blue')
if (event == 'OK') & (SES[10] == 1):  SES[13] = 1
if (event == 'OK0') & (SES[10] == 1):  SES[14] = 1
if event == 'OK2':
    print('ok we good 3')
    ######## Gripper tool
    Tool_sensor1 = eip_instance.read_variable('DETECT_TOOL_1')
    ######### drill tool
    Tool_sensor2 = eip_instance.read_variable('t2')
    if Tool_sensor1 == False and Tool_sensor2 == False:
        reply = eip_instance.write_variable('tol', False)
        reply = eip_instance.write_variable('toolu', False)
        reply = eip_instance.write_variable('toolu', True)
if event == 'OK3':
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
if values != None:
    SES[3], SES[4], SES[5], SES[6], SES[7] = values[1], values[5], values[4], values[2], values[3]
if event == 'OK5':
    print('ok we good 1')
    gri_set(PORT)
if event == 'OK6':
    print('ok we good 2')
    gri_op(PORT, int(values[0]))
