import logging
import os
from logging.handlers import RotatingFileHandler

from framework.logger.logger_config import LoggerConfig


class Logger:
    """
    Class contains logger and methods
    """
    if not os.path.isdir(LoggerConfig.DIR_NAME):
        os.makedirs(LoggerConfig.DIR_NAME)

    __logger = logging.getLogger(LoggerConfig.NAME)
    __logger.setLevel(LoggerConfig.LEVEL)
    __logger.addHandler(RotatingFileHandler(LoggerConfig.FILE_NAME))

    @staticmethod
    def get_log():
        return Logger.__logger
