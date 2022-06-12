class Plane():
    def __init__(self, robo=False):
        self.points = {}
        self.positions = {
            'santa': {
                'x': 0,
                'y': 0
            }
        }
        self._move_to_point("santa", 0, 0)
        if robo:
            self._add_robo()

    @property
    def number_of_points(self):
        return len(self.points)

    def _add_robo(self):
            self.positions['robo'] = {
                'x': 0,
                'y': 0
            }   
            self._move_to_point("robo", 0, 0)

    def _add_point(self, x, y):
        self.points[(x, y)] = 1

    def _increment_point_counter(self, x, y):
        self.points[(x, y)] += 1

    def _move_to_point(self, who, x, y):
        self._add_or_increment_point(x, y)
        self.positions[who]['x'] = x
        self.positions[who]['y'] = y

    def _add_or_increment_point(self, x, y):
        if (x, y) in self.points:
            self._increment_point_counter(x, y)
        else:
            self._add_point(x, y)

    def move_up(self, who="santa", amount=1):
        self._move_to_point(who, self.positions[who]['x'], self.positions[who]['y']+1)

    def move_down(self, who="santa", amount=1):
        self._move_to_point(who, self.positions[who]['x'], self.positions[who]['y']-1)

    def move_left(self, who="santa", amount=1):
        self._move_to_point(who, self.positions[who]['x']-1, self.positions[who]['y'])

    def move_right(self, who="santa", amount=1):
        self._move_to_point(who, self.positions[who]['x']+1, self.positions[who]['y'])
