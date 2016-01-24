from __future__ import print_function
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def say_hello(text):
    """Print out text."""
    logger.debug("Say Message: {text}".format(text = text))
    print(text)




