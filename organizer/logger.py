import logging
import os

def setup_logging(log_file="file_organizer.log"):
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("file_organizer")
    logger.setLevel(logging.INFO)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_file)

    # Create formatters and add it to handlers
    c_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger


