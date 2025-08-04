import logging
# logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArthematicApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result

def sub(a,b):
    result=a-b
    logger.error(f"Adding {a}-{b}={result}")
    return result

add(10,45)
sub(3,0)