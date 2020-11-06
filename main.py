noise = 0


def on_forever():
    global noise

    noise = smarthome.read_noise(AnalogPin.P2)


basic.forever(on_forever)
