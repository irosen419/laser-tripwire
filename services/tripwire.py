import time
import RPi.GPIO as GPIO

from .alert import Alert
from .sensor import Sensor
from .sound import Sound

class Tripwire:
  def __init__(self, sensor_pin, speaker_pin=None, warnings=False, sound='buzzer.mp3'):
    self.sensor_pin = sensor_pin
    self.speaker_pin = speaker_pin
    self.warnings = warnings
    self.__alert = Alert()
    self.__sound = Sound(sound)
    self.__wire_tripped = False
    self.__setup_gpio()

  def start(self):
    print('Starting up...')

    while True:
      if self.sensor_triggered:
        if not self.__wire_tripped:
          print('Tripwire activated!!')
          self.alert_user()
          self.play_sound()
          self.__wire_tripped = True
      else:
        print('No movement...')
        self.__wire_tripped = False

      time.sleep(0.1)  # Prevents CPU from overheating

  @property
  def sensor_triggered(self):
    return self.__sensor.is_triggered

  @property
  def __sensor(self):
    return Sensor(GPIO, self.sensor_pin)

  def alert_user(self):
    self.__alert.alert()

  def play_sound(self):
    if self.__sound:
      self.__sound.play()

  def __setup_gpio(self):
    GPIO.setwarnings(self.warnings)
    GPIO.setmode(GPIO.BCM)

# Tripwire(18).start()