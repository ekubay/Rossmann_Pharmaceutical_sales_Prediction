import logging

class Logger:

  def __init__(self, file_name: str, basic_level=logging.INFO):
    # Gets or creates a logger
    logger = logging.getLogger(__name__)  

    # set log level
    logger.setLevel(basic_level)

    # define file handler and set formatter
    file_handler = logging.FileHandler(f'../logs/{file_name}')
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s', '%m-%d-%Y %H:%M:%S')
    
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    self.logger = logger
    
  def  get_app_logger(self) -> logging.Logger:
    return self.logger