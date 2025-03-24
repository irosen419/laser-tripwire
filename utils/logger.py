import traceback

class Logger:
  def __init__(self):
    #* No need for arguments or instance variables here
    pass

  def log_error(self, error, context=None):
    print(f"Error in [{context}]: {self.capitalize_error(error)}\n")
    traceback.print_exception(type(error), error, error.__traceback__)


  def capitalize_error(self, error):
    return str(error).capitalize()