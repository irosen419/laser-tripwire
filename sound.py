import pygame

from logger import Logger

class Sound():
  def __init__(self, file_name = 'buzzer.mp3'):
    self.file_name = file_name
    self.__mixer = self.__initialize_mixer()
    self.__logger = Logger

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
      self.__logger(e).log()

  def keep_it_going(self):
    while self.__mixer.music.get_busy():
      pygame.time.Clock().tick(10)  #* Keeps the script alive while the sound is playing

  def file_location(self):
    return f'./assets/sounds/{self.file_name}'