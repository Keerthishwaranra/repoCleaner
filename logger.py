import logging

def setup_logger(log_file):
    logger = logging.getLogger('repoCleaner')
    logger.setLevel(logging.DEBUG)

    # File handler for debug logs
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    # Console handler for info logs
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger