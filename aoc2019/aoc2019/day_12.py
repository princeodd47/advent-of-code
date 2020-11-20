from dataclasses import dataclass
import logging


from aoc2019 import position

logger = logging.getLogger(__name__)
logging_fh = logging.FileHandler('debug.log', mode='w')
logger.addHandler(logging_fh)
logger.setLevel(logging.DEBUG)

# Notes


@dataclass
class Moon:
    def __init__(self, name, x, y, z):
        self.name = name
        self.position_current = position.Position(x=x, y=y, z=z)
        self.position_new = position.Position(x=0, y=0, z=0)


class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        return f'x={self.x} y={self.y} z={self.z}'

    def update_velocity(self, incremental_velocity):
        self.x += incremental_velocity.x
        self.y += incremental_velocity.y
        self.z += incremental_velocity.z


def _calculate_gravity(current_position, compared_position):
    print(f"calculate gravity between {current_position} and {compared_position}")
    # Ganymede x position = 3
    # Callisto x position = 5
    # Ganymede x velocty = +1 because Ganymede.x < Callisto.x
    # Callisto x velocty = -1
    x_velocity = 0
    y_velocity = 0
    z_velocity = 0
    if current_position.x > compared_position.x:
        x_velocity += -1
    else:
        x_velocity += 1
    if current_position.y > compared_position.y:
        y_velocity += -1
    else:
        y_velocity += 1
    if current_position.z > compared_position.z:
        z_velocity += -1
    else:
        z_velocity += 1
    print(f'{x_velocity=} {y_velocity=} {z_velocity=}')
    velocity = Velocity(x=x_velocity, y=y_velocity, z=z_velocity)
    print('{velocity.x=}')
    return velocity


def part1():
    moons = []
    moons.append(Moon(name="Io", x=-3, y=10, z=-1))
    moons.append(Moon(name="Europa", x=-12, y=-10, z=-5))
    moons.append(Moon(name="Ganymede", x=-9, y=0, z=10))
    moons.append(Moon(name="Callisto", x=7, y=-5, z=-3))
    for moon in moons:
        total_velocity = Velocity(x=0, y=0, z=0)
        if moon.name == "Io":
            other_moons = [m for m in moons if m.name != moon.name]
            for other_moon in other_moons:
                current_velocity = _calculate_gravity(moon.position_current,
                                                      other_moon.position_current)
                current_velocity.print()
                total_velocity.update_velocity(current_velocity)
                print(f'total_velocity={total_velocity.print()}')
