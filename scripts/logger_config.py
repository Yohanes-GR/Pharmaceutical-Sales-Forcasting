import logging

LOGGING_FORMAT = "%(levelname)s - %(asctime)s - %(message)s"

logging.basicConfig(filename='../logs/logs.txt',
                    level=logging.DEBUG,
                    format=LOGGING_FORMAT)

logger = logging.getLogger()
