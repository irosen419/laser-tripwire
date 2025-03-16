class Sensor:
  def __init__(self, gpio, pin):
    self._gpio = gpio
    self._pin = pin
    self._setup()

  def status(self):
    return self._gpio.input(self._pin)

  @property
  def is_triggered(self):
    return self.status() != 0

  def _setup(self):
    self._gpio.setup(self._pin, self._gpio.IN, pull_up_down=self._gpio.PUD_UP)
