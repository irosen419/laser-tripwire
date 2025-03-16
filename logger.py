import traceback

class Logger:
  def __init__(self, error):
    self.error = error

  def log_error(self):
    print(f"Error sending email: {self.error}")
    traceback.print_exception(type(self.error), self.error, self.error.__traceback__)