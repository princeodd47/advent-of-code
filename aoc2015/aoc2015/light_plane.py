class Plane():
    def __init__(self, max_x=1000, max_y=1000):
        self.points = {}
        self.max_x = max_x
        self.max_y = max_y
        self._add_points(max_x, max_y)
        self.action_map = {
            'turn on': self._turn_on_point,
            'turn off': self._turn_off_point,
            'toggle': self._toggle_point
        }
        self.action_map_part2 = {
            'turn on': self._turn_on_point_part2,
            'turn off': self._turn_off_point_part2,
            'toggle': self._toggle_point_part2
        }

    @property
    def total_points(self):
        return len(self.points)

    @property
    def total_brightness(self):
        return sum([v for v in self.points.values()])

    @property
    def total_points_on(self):
        return len([v for v in self.points.values() if v >= 1])

    @property
    def total_points_off(self):
        return len([v for v in self.points.values() if v == 0])

    def _add_points(self, max_x, max_y):
        for y in range(max_y):
            for x in range(max_x):
                self._add_point(x, y)

    def _add_point(self, x, y):
        self.points[(x, y)] = 0

    def commit_actions(self, actions):
        for action in actions:
            self._commit_action(action)

    def _commit_action(self, action):
        for y in range(action['begin_y'], action['end_y'] + 1):
            for x in range(action['begin_x'], action['end_x'] + 1):
                self.action_map[action['action']](x, y)

    def _toggle_point(self, x, y):
        if self.points[(x, y)] == 0:
            self._turn_on_point(x, y)
        else:
            self._turn_off_point(x, y)

    def _turn_on_point(self, x, y):
        self.points[(x, y)] = 1
        
    def _turn_off_point(self, x, y):
        self.points[(x, y)] = 0
        
    def commit_actions_part2(self, actions):
        for action in actions:
            self._commit_action_part2(action)

    def _commit_action_part2(self, action):
        for y in range(action['begin_y'], action['end_y'] + 1):
            for x in range(action['begin_x'], action['end_x'] + 1):
                self.action_map_part2[action['action']](x, y)

    def _toggle_point_part2(self, x, y):
        self.points[(x, y)] += 2

    def _turn_on_point_part2(self, x, y):
        self.points[(x, y)] += 1
        
    def _turn_off_point_part2(self, x, y):
        if self.points[(x, y)] > 0:
            self.points[(x, y)] -= 1

    def print_plane(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.points[(x,y)]:
                    print("\u2588\u2588", end="")
                else:
                    print("  ", end="")
            print("")
