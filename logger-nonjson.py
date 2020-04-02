import logging
import time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

while(True):
    logging.debug("Hello World!")
    time.sleep(1)
