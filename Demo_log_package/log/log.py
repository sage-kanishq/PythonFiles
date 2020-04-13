import socket
import logging

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def logged(e,logger=__name__,severity="info",max_level = 20):    
    logger = logging.getLogger(logger)
    logger.setLevel(max_level)
    formatter = logging.Formatter(f"[%(asctime)s:%(msecs)s] [%(levelname)s] [{get_ip_address()}] [%(name)s] :%(message)s",datefmt="%d-%b-%Y %H:%M:%S")
    fileHandler = logging.FileHandler("main.log")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    if severity.lower()=="error":                   
        logger.error(e)

    elif severity.lower()=="info":
        logger.info(e)

    elif severity.lower()=="debug":
        logger.debug(e)

    elif severity.lower()=="critical":
        logger.critical(e)

    elif severity.lower()=="warning":
        logger.warning(e)

    elif severity.lower()=="exception":
        logger.exception(e)
    else:
        raise f"{severity} not supported enter either : DEBUG, INFO, WARNING, ERROR, CRITICAl"


def getNameOfFile(a):
    return a.split("/")[len(a.split("/"))-1]

    

                     





