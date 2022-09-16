import logging
from setting import pathlog
print("log_write pathlog=",pathlog)
format_="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
logging.basicConfig(filename=pathlog,format=format_,filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')





