from mailersend import emails

from utils import Config, Logger

class Mailer:
  def __init__(self, logger=None):
    print('Initializing Mailer!')
    if not self.__mailersend_api_key:
      raise ValueError('MAILERSEND_API_KEY is missing')
    if not self.__to_email:
      raise ValueError('TO_EMAIL is missing')
    if not self.__from_email:
      raise ValueError('FROM_EMAIL is missing')

    self._app_name = 'Doggy Tripwire'
    self.__logger = logger or Logger()
    self.mail_body = {}

  def send(self):
    mailer = self.initialize_mailer()
    html_content = self.load_template('./templates/email.html', app_name=self.app_name)

    try:
      mailer.set_mail_from(self.mail_from, self.mail_body)
      mailer.set_mail_to(self.mail_to, self.mail_body)
      mailer.set_subject('You doggy tripwire has been activated!', self.mail_body)
      mailer.set_html_content(html_content, self.mail_body)

      # using print() will also return status code and data
      sent = mailer.send(self.mail_body)
      print('Sent Email. Code: ', sent)
    except Exception as e:
      self.__logger.log_error(e, context=self.__class__.__name__)

  def initialize_mailer(self):
    return emails.NewEmail(self.__mailersend_api_key)

  def load_template(self, filename, **kwargs):
    with open(filename, 'r') as file:
      html = file.read()
      return html.format(**kwargs)

  @property
  def mail_to(self):
    return [{ 'name': 'Ian Rosen', 'email': self.__to_email }]

  @property
  def mail_from(self):
    return { 'name': self.app_name, 'email': self.__from_email }

  @property
  def reply_to(self):
    return { 'name': self.app_name, 'email': self.__reply_to_email }

  @property
  def app_name(self):
    return self._app_name

  @property
  def __to_email(self):
    return Config.TO_EMAIL

  @property
  def __from_email(self):
    return Config.FROM_EMAIL

  @property
  def __reply_to_email(self):
    return Config.FROM_EMAIL

  @property
  def __mailersend_api_key(self):
    return Config.MAILERSEND_API_KEY