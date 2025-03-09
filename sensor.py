class Sensor():
  def __init__(self, gpio, pin):
    self.pin = pin
    self.GPIO = gpio
    self.setup()

  def setup(self):
    self.GPIO.setup(self.pin, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)

  def get_status(self):
    return self.GPIO.input(self.pin)
