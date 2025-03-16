import pygame

from utils import Logger

class Sound():
  def __init__(self, file_name = 'buzzer.mp3', logger=None):
    self._file_name = file_name
    self.__mixer = self.__initialize_mixer()
    self.__logger = logger or Logger()

  def __initialize_mixer(self):
    pygame.mixer.init()
    return pygame.mixer

  def play(self):
    try:
      self.__mixer.music.load(self.file_location())
      self.__mixer.music.play()
      print('Sound played!')
      self.keep_it_going()

    except Exception as e:
      self.__logger.log_error(e, context=self.__class__.__name__)

  def keep_it_going(self):
    while self.__mixer.music.get_busy():
      pygame.time.Clock().tick(10)  #* Keeps the script alive while the sound is playing

  @property
  def file_name(self):
    return self._file_name

  def file_location(self):
    return f'./assets/sounds/{self.file_name}'