let noise = 0
let strip = neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB)
basic.forever(function on_forever() {
    
    let light2 = smarthome.ReadLightIntensity(AnalogPin.P3)
    if (light2 < 50) {
        noise = smarthome.ReadNoise(AnalogPin.P2)
        if (noise > 70) {
            strip.showColor(neopixel.colors(NeoPixelColors.Orange))
            basic.pause(10000)
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
        }
        
    }
    
})
