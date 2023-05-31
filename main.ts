radio.setGroup(2)
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate9600
)
basic.forever(function () {
    radio.sendValue("X", pins.analogReadPin(AnalogPin.P2))
    radio.sendValue("Y", pins.analogReadPin(AnalogPin.P1))
    serial.writeLine("X   " + pins.analogReadPin(AnalogPin.P2) + "   Y   " + pins.analogReadPin(AnalogPin.P1))
})
