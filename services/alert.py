from utils import Logger
from services import Mailer, Twilio

class Alert:
  def __init__(self, alert_type='multi', logger=None, mailer=None, twilio=None):
    self.type = alert_type
    self.__logger = logger or Logger()
    self.__mailer = mailer or Mailer()
    self.__twilio = twilio or Twilio()

  def alert(self):
    try:
      if self.type == 'multi':
        self.send_everything()
      elif self.type == 'email':
        self.send_email()
      elif self.type == 'sms':
        self.send_sms()
    except Exception as e:
      self.__logger(e).log_error()

  def send_everything(self):
    self.send_email()
    self.send_sms()

  def send_email(self):
    try:
      self.__mailer.send()
    except Exception as e:
      self.__logger(e).log_error()

  def send_sms(self):
    try:
      self.__twilio.send_sms()
    except Exception as e:
      self.__logger(e).log_error()