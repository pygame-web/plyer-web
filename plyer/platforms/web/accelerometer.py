import js
from plyer.facades import Accelerometer

js.eval("""
window.accelerometer = {x:0.0,y:0.0,z:9.807}

try {
    window.dev = window.dev || {}

    const accel = new Accelerometer({ frequency: 60 })
    window.dev["accelerometer"] = accel
    accel.addEventListener("reading", () => {
        window.accelerometer.x = accel.x
        window.accelerometer.y = accel.y
        window.accelerometer.z = accel.z
    })

} catch (x) {
    console.error("Accelerometer not supported")
}

""")



class WebAccelerometer(Accelerometer):
    def _enable(self):
        js.window.dev.accelerometer.start()

    def _disable(self):
        js.window.dev.accelerometer.stop()

    def _get_acceleration(self):
        adict = js.window.accelerometer
        return (float(adict.x), float(adict.y), float(adict.z),)


def instance():
    return WebAccelerometer()
