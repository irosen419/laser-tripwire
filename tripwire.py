import RPi.GPIO as GPIO
from time import sleep
from sensor import Sensor
from sound import Sound

class Tripwire:
  def __init__(self, sensor_pin, speaker_pin = None, warnings = False):
    self.sensor_pin = sensor_pin
    self.warnings = warnings
    self.setup()

  def setup(self):
    GPIO.setwarnings(self.warnings)
    GPIO.setmode(GPIO.BCM)

  def get_sensor(self):
    return Sensor(GPIO, self.sensor_pin)

  def start(self):
    sensor = self.get_sensor()
    sound = Sound('./assets/sounds/buzzer.mp3')

    wire_tripped = False

    while True:
      sensor_state = sensor.get_status()
      print(sensor_state)

      if sensor_state == 0:
        print('NO MOVEMENT!')
        wire_tripped = False
      else:
        print('LASER TRIPPED!')
        if wire_tripped == False:
          sound.play()
          wire_tripped = True


test = Tripwire(18)
test.start()