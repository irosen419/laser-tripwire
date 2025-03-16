import time
import RPi.GPIO as GPIO

from services.alert import Alert
from services.sensor import Sensor
from services.sound import Sound

class Tripwire:
  def __init__(self, sensor_pin, speaker_pin=None, warnings=False, sound='buzzer.mp3'):
    self.sensor_pin = sensor_pin
    self.speaker_pin = speaker_pin
    self.warnings = warnings
    self.__alert = Alert()
    self.__sound = Sound(sound) if speaker_pin else None
    self.__wire_tripped = False

  def start(self):
    print('Tripwire activated...')

    while True:
      if self.sensor_triggered:
        if not self.__wire_tripped:
          self.alert_user()
          self.play_sound()
          self.__wire_tripped = True
      else:
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

  @property
  def gpio(self):
    GPIO.setwarnings(self.warnings)
    GPIO.setmode(GPIO.BCM)
