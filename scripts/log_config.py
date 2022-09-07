import logging
import sys, os
sys.path.append(os.path.abspath(os.path.join('../scripts')))
LOGGING_FORMAT = "%(levelname)s - %(asctime)s - %(message)s"

logging.basicConfig(filename='../logs/logs.txt',
                    level=logging.DEBUG,
                    format=LOGGING_FORMAT)

logger = logging.getLogger()