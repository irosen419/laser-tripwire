import pygame

class Sound():
  def __init__(self, file_name):
    self.file_name = file_name

  def mixer(self):
    pygame.mixer.init()
    return pygame.mixer

  def play(self):
    pygame.mixer.init()
    pygame.mixer.music.load(self.file_name)
    pygame.mixer.music.play()