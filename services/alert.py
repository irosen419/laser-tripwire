from utils import Logger
from .mailer import Mailer
from .twilio_class import Twilio

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
      self.__logger.log_error(e, context=self.__class__.__name__)

  def send_everything(self):
    if self.type == 'test':
      print('testing! everything')
      return ''
    self.send_email()
    self.send_sms()

  def send_email(self):
    if self.type == 'test':
      print('testing! email')
      return ''
    try:
      self.__mailer.send()
    except Exception as e:
      self.__logger.log_error(e, context=self.__class__.__name__)

  def send_sms(self):
    if self.type == 'test':
      print('testing! text')
      return ''
    try:
      self.__twilio.send_sms()
    except Exception as e:
      self.__logger.log_error(e, context=self.__class__.__name__)

  def test_logger(self):
    try:
      1 / 0
    except Exception as e:
      self.__logger.log_error(e, context=self.__class__.__name__)
