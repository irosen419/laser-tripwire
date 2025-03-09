import RPi.GPIO as GPIO
from time import sleep

class Tripwire:
  def __init__(self, sensor_pin, speaker_pin, warnings = False):
    self.sensor_pin = sensor_pin
    self.warnings = warnings

  def setup(self):
    GPIO.setwarnings(self.warnings)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  def alert(self):
    while True:
      button_state = GPIO.input(self.sensor_pin)
      print(button_state)

      if button_state == 0:
        print('NO MOVEMENT!')
      else:
        print('LASER TRIPPED!')

      sleep(1)


test = Tripwire(18)
test.setup()
test.alert()