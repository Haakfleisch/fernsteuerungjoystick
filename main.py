radio.onReceivedString(function (receivedString) {
    if (input.rotation(Rotation.Pitch) > 20) {
        calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, input.rotation(Rotation.Pitch))
    } else if (input.rotation(Rotation.Pitch) < -20) {
        calliBot2.motor(C2Motor.beide, C2Dir.rueckwaerts, -1 * input.rotation(Rotation.Pitch))
    } else {
        calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
    }
})
radio.setGroup(2)
basic.forever(function () {
    let conack = 0
    if (0 == conack) {
        let funkgrp: null = null
        radio.sendString("" + (funkgrp))
    }
})
