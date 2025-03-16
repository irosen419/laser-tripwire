from twilio.rest import Client

from utils import Config, Logger

class Twilio:
  def __init__(self):
    if not self.__from_number:
      raise ValueError('TWILIO_FROM_NUMBER is missing')
    if not self.__to_number:
      raise ValueError('TWILIO_TO_NUMBER is missing')
    if not self.__account_sid:
      raise ValueError('TWILIO_ACCOUNT_SID is missing')
    if not self.__auth_key:
      raise ValueError('TWILIO_AUTH_KEY is missing')

    self.__logger = Logger

  def send_sms(self, message = 'Tripwire activated! Click here to view the footage:'):
    print('Sending sms!')

    try:
      self.__client.messages.create(
        from_ = self.__from_number,
        to = self.__to_number,
        body = message
      )
    except Exception as e:
      self.__logger(e).log_error()

  @property
  def __client(self):
    return Client(self.__account_sid, self.__auth_key)

  @property
  def __from_number(self):
    return Config.TWILIO_FROM_NUMBER

  @property
  def __to_number(self):
    return Config.TWILIO_TO_NUMBER

  @property
  def __account_sid(self):
    return Config.TWILIO_ACCOUNT_SID

  @property
  def __auth_key(self):
    return Config.TWILIO_AUTH_KEY