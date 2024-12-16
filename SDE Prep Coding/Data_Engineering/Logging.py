import logging

datestr = "%Y:%m:%d %I:%M:%S %p"
fmtstr = "%(asctime)s: %(levelname)s %(filename)s %(lineno)d %(module)s- %(message)s"
log = logging.basicConfig(
    filemode="w",
    filename=r"C:\Users\rameseka\OneDrive - Cisco\Desktop\Ramesh Scripts\Probelm-Solving\SDE Prep Coding\Data_Engineering\Test.log",
    level=logging.DEBUG,
    format=fmtstr,
    datefmt=datestr
)

def funclog(function):
    print("Entering")
    def wrapper(*args, **kwargs):
        function
    print("Exitting")
    return wrapper



logging.debug("This is an Debug Message")
logging.info("This is an Info Message")
logging.warning("This is an Warming Message")
logging.error("This is an Debug Message")
logging.critical("This is an Debug Message")

import logging
from functools import wraps

# Set up a standalone logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s: %(levelname)s %(funcName)s %(lineno)d %(module)s - %(message)s")
ch.setFormatter(formatter)

logger.addHandler(ch)

def function_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing function: {func.__name__}", stacklevel=2)
        result = func(*args, **kwargs)
        logger.info(f"Exiting function: {func.__name__}", stacklevel=2)
        return result
    # print(func.__name__)
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    # wrapper.__module__ = func.__module__
    return wrapper

@function_logging
def sample_function():
    logger.info("Inside sample_function")

if __name__ == "__main__":
    sample_function()
