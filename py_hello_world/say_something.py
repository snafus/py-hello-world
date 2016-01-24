import logging
import argparse,sys

from py_hello_world import hello_world

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

parser = argparse.ArgumentParser(description='Process and display some text')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                   help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',
#                   const=sum, default=max,
#                   help='sum the integers (default: find the max)')

parser.add_argument('bar', nargs='+', help='bar help')


def say_something(text):
    """Call the function to display supplied text"""
    hello_world.say_hello(text)


if __name__ == '__main__':
    logger.debug("Main called")
    logger.debug("Args {args}".format(args = ' , '.join((("%s" % x) for x in sys.argv))))
    
    args = parser.parse_args()
    
    say_something( ' '.join(args.bar) )

