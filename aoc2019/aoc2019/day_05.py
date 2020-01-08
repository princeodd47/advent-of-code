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
    test.diagnostic_program(1)
    print(test.result)


def part2():
    test = IntCode()
    test.get_input("input/day_05")
    test.diagnostic_program(5)
    print(test.result)
