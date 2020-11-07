# Simle application to test Microphone sensor from Smart home kit 
# Application measures noise level , it is in range 36-75
# and result is dispayed on LED matrix (0=40LEDs, 65=25LEDs)
# !!! If there's no sensor connected to the PIN, system returns value 55 !!!

noise = 0
min_n = 40
max_n = 65

# min bylo 36, max bylo 105

serial.redirect_to_usb()


def on_forever():
    global noise, min_n, max_n
    noise = smarthome.read_noise(AnalogPin.P2)
    serial.write_value("x", noise) 
    noise = (noise - min_n) * (25/max_n)
    Higlight_X_dots(noise)
    pause(1000)

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
    


def on_button_pressed_a():
    global min_n
    min_n -= 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global max_n
    max_n += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global max_n, min_n
    basic.show_string("Min" + str(min_n))
input.on_button_pressed(Button.AB, on_button_pressed_ab)
