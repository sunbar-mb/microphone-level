noise = 0
min_n = 30
max_n = 100


def on_forever():
    global noise, min_n, max_n
    noise = smarthome.read_noise(AnalogPin.P2)

    noise = (noise - min_n) * (25/max_n)
    Higlight_X_dots(noise)

basic.forever(on_forever)



def Higlight_X_dots(Number_of_Dots):
    Line_num = 0
    Row_num = 0
    
    basic.clear_screen()

    if Number_of_Dots > 25:
        Number_of_Dots = 25

    if Number_of_Dots <= 0:
        basic.clear_screen()

    for i in range(Number_of_Dots):
        led.plot(Line_num, Row_num)
        Line_num = Line_num + 1
        #Row_num = Row_num + 1
        if Line_num > 4:
            Line_num = 0
            Row_num = Row_num + 1
    
