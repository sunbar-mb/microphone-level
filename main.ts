let noise = 0
let min_n = 30
let max_n = 100
basic.forever(function on_forever() {
    
    noise = smarthome.ReadNoise(AnalogPin.P2)
    noise = (noise - min_n) * (25 / max_n)
    Higlight_X_dots(noise)
})
function Higlight_X_dots(Number_of_Dots: number) {
    let Line_num = 0
    let Row_num = 0
    basic.clearScreen()
    if (Number_of_Dots > 25) {
        Number_of_Dots = 25
    }
    
    if (Number_of_Dots <= 0) {
        basic.clearScreen()
    }
    
    for (let i = 0; i < Number_of_Dots; i++) {
        led.plot(Line_num, Row_num)
        Line_num = Line_num + 1
        // Row_num = Row_num + 1
        if (Line_num > 4) {
            Line_num = 0
            Row_num = Row_num + 1
        }
        
    }
}

