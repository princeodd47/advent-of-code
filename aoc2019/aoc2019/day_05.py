import logging
import pdb

from .intcode import IntCode

logger = logging.getLogger(__name__)
logging_fh = logging.FileHandler('debug.log')
logger.addHandler(logging_fh)
logger.setLevel(logging.DEBUG)


def part1():
    test = IntCode()
    test.get_input("input/day_05")
    test.set_user_input([1])
    test.diagnostic_program()
    print(test.result)


def part2():
    test = IntCode()
    test.get_input("input/day_05")
    test.set_user_input([5])
    test.diagnostic_program()
    print(test.result)
