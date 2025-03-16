import os
from dotenv import load_dotenv
from logger import Logger
from twilio.rest import Client

class Twilio:
  def __init__(self):
    load_dotenv()
    self.__logger = Logger

  def send_sms(self, message = 'Tripwire activated! Click here to view the footage:'):
    print('Sending sms!')

    try:
      self.__client.messages.create(
        from_ = self.__from_number(),
        to = self.__to_number()       ,
        body = message
      )
    except Exception as e:
      self.__logger(e).log_error()

  @property
  def __client(self):
    return Client(self.__account_sid(), self.__auth_key())

  @property
  def from_number(self):
    return os.getenv('TWILIO_FROM_NUMBER')

  @property
  def to_number(self):
    return os.getenv('TWILIO_TO_NUMBER')

  @property
  def account_sid(self):
    return os.getenv('TWILIO_ACCOUNT_SID')

  @property
  def auth_key(self):
    return os.getenv('TWILIO_AUTH_KEY')