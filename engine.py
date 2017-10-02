"""
Engine
"""

try:
    import RPi.GPIO as gpio
except RuntimeError:
    print("""Error importing RPi.GPIO!  This is probably because you need superuser privileges.
                You can achieve this by using 'sudo' to run your script""")

LED = 40  # assign pin number


class Engine:
    def __init__(self):
        self.gpio_setup()
        gpio.output(LED, gpio.LOW)

    def turn_off(self):
        gpio.output(LED, gpio.LOW)

    def turn_on(self):
        gpio.output(LED, gpio.HIGH)

    def gpio_setup(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)
        gpio.setup(LED, gpio.OUT)


# ------

if __name__ == '__main__':
    engine = Engine()
    engine.turn_off()
