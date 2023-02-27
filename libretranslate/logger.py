import logging
from logging.handlers import RotatingFileHandler

MAX_FILE_SIZE = 100000000

class Logger: 
    def __init__(self, name: str, file: str) -> None:
        self.logger = logging.getLogger(name)

        self.f_handler = RotatingFileHandler(file, mode='a', maxBytes=MAX_FILE_SIZE, 
                                 backupCount=2, encoding=None, delay=0)
        self.f_handler.setLevel(logging.INFO)
        self.f_format = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s',datefmt='%d-%b-%y %H:%M:%S')
        self.f_handler.setFormatter(self.f_format)

        self.logger.addHandler(self.f_handler)
        self.logger.setLevel(logging.INFO)
    
    def log_successful_request(self, time_taken: float):
        self.logger.info(f'[SUCCESS][Time Taken: {time_taken}s]')

    def log_exception(self, message: str):
        self.logger.critical(f'[EXCEPTION][Message: {message}]')
    
    def log_info(self,info):
        self.logger.info(info)
    
    def extend_logger(self,handler): 
        self.logger.handlers.extend(handler)