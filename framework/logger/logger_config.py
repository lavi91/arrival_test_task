import logging
import os


class LoggerConfig:
    """
    Class contains logger config data
    """
    DIR_NAME = "logs"
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
    FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    NAME = "Logger"
    FILE_NAME = DIR_NAME + os.sep + "api.log"
    LEVEL = logging.INFO
