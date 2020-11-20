from dataclasses import dataclass
from enum import Enum
import logging

from .intcode import IntCode
from aoc2019 import point

logger = logging.getLogger(__name__)
logging_fh = logging.FileHandler('debug.log', mode='w')
logger.addHandler(logging_fh)
logger.setLevel(logging.DEBUG)

# Notes
# All panels are currently black
# grid[x_y] = { color, paint_count }
# input:
# - 0 if cur_panel black, 1 if cur_panel is white
# output: two values: color, direction
# - 0 paint cur_panel black, 1 paint cur_panel white
# - 0 turn left 90 degrees, 1 turn right 90 degrees


class Color(Enum):
    BLACK = 0
    WHITE = 1


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


@dataclass
class Robot:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.debug("Robot initialized")
        self.grid = dict()
        self.position = point.Point(x=0, y=0)
        self.move_count = 0
        self._direction = Direction.NORTH
        self._grid_min_point = point.Point(x=0, y=0)
        self._grid_max_point = point.Point(x=0, y=0)
        self._logger.debug("")
        self._points_painted = set()
        self._points_visited = set()

    @property
    def position_string(self):
        return f"{self.position.x}_{self.position.y}"

    @property
    def current_color(self):
        if self.position_string not in self.grid:
            # self._logger.debug(f"{self.position_string=} not in self.grid: adding with default"
            #                    "values")
            self.grid[self.position_string] = {'color': Color.BLACK, 'paint_count': 0}
        # self._logger.debug(f"{self.grid[self.position_string]}")
        return

    def paint_position(self, new_color):
        """
        Changes color of current position in grid.
        """
        self._points_painted.add(self.position_string)
        # self._logger.debug(f"paint_position({new_color})")
        # self._logger.debug(f"{self.position_string=} {self.grid[self.position_string]=}")
        self.grid[self.position_string]['color'] = new_color
        self.grid[self.position_string]['paint_count'] += 1
        # self._logger.debug(f"{self.position_string=} {self.grid[self.position_string]=}")

    def change_direction(self, new_direction):
        # self._logger.debug(f"{self._direction}")
        if new_direction == 0:
            # self._logger.debug("turn left")
            self._turn_left()
        else:
            # self._logger.debug("turn right")
            self._turn_right()
        # self._logger.debug(f"{self._direction}")

    def move_forward(self, distance=1):
        # self._logger.debug(f"BEGIN {self.position=}")
        # self._logger.debug(f"moving forward {distance=}")
        if self._direction == Direction.NORTH:
            self.position.move_up(distance)
        elif self._direction == Direction.EAST:
            self.position.move_right(distance)
        elif self._direction == Direction.SOUTH:
            self.position.move_down(distance)
        elif self._direction == Direction.WEST:
            self.position.move_left(distance)
        # self._logger.debug(f"{self.position=}")
        self._points_visited.add(self.position_string)
        self._update_grid_size()

    def print_grid(self):
        for y in range(self._grid_max_point.y+1, self._grid_min_point.y-1, -1):
            for x in range(self._grid_min_point.x, self._grid_max_point.x+1, 1):
                position_string = f"{x}_{y}"
                if position_string not in self.grid:
                    color = Color.BLACK
                else:
                    color = self.grid[position_string]['color']

                if color == Color.WHITE:
                    print(u"\u2588", end='')
                else:
                    print(' ', end='')
            print('')

    def _turn_left(self):
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.EAST:
            self._direction = Direction.NORTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH

    def _turn_right(self):
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = Direction.NORTH

    def _update_grid_size(self):
        if self.position.x < self._grid_min_point.x:
            self._grid_min_point.x = self.position.x
        if self.position.y < self._grid_min_point.y:
            self._grid_min_point.y = self.position.y
        if self.position.x > self._grid_max_point.x:
            self._grid_max_point.x = self.position.x
        if self.position.y > self._grid_max_point.y:
            self._grid_max_point.y = self.position.y


def part1():
    intcomp = IntCode()
    intcomp.get_input("input/day11")
    robot = Robot()

    while not intcomp.halt_code_reached:
        intcomp.set_user_input([robot.current_color])
        _ = intcomp.diagnostic_program()
        instructions = intcomp.result_history[-2:]
        robot._logger.debug(f"{robot.move_count=} {instructions=}")

        if instructions[0] == 0:
            new_color = Color.BLACK
        else:
            new_color = Color.WHITE
        new_direction = instructions[1]

        robot.paint_position(new_color)
        robot.change_direction(new_direction)

        robot.move_forward(1)
        robot.move_count += 1
        # robot._logger.debug("")
    robot._logger.debug(f"{robot._grid_min_point=}")
    robot._logger.debug(f"{robot._grid_max_point=}")
    robot.print_grid()
    print(len(robot.grid))
    print(f"len(robot.grid)={len(robot.grid)}")
    print(f"{robot.move_count=}")
    print(f"len(robot._points_painted)={len(robot._points_painted)}")
    print(f"len(robot._points_visited)={len(robot._points_visited)}")
