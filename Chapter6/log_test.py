import loggingBASE_FORMAT = "[%(name)s] [%(levelname)-6s] %(message)s"FILE_FORMAT = "[%(asctime)s]" + BASE_FORMATlogger = logging.getLogger()logger.setLevel(logging.DEBUG)try:    file_logger = logging.FileHandler("./application.log")    file_logger.setFormatter(logging.Formatter(FILE_FORMAT))    logger.addHandler(file_logger)except (OSError, IOError):    file_logger = logging.FileHandler("/tmp/application.log")    file_logger.setFormatter(logging.Formatter(FILE_FORMAT))    logger.addHandler(file_logger)logger.warning('this is an info message from the root logger')app_logger = logging.getLogger('my-app')app_logger.warning('an info message from my-app')app_logger.info('hihi')