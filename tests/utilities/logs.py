import logging


def create_logger(log_folder):

    logger = logging.getLogger(log_folder)
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

    # Console Handler
    console_handler: logging.StreamHandler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
