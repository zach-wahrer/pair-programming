"""
   List of movent.

   [3, "R", "L"]

   N (0,0)

    """


class Cardinal:
    def __init__(self, dir):
        self.dir = dir
        self.left = None
        self.right = None

    def add(self, next_dir):
        if not self.right:
            new_cardinal = Cardinal(next_dir)
            self.right = new_cardinal
            new_cardinal.left = self
        else:
            self.right.add(next_dir)
        return self


class Compas:
    def __init__(self):
        self.cardinal = Cardinal("North")
        self._add_cardinals()
        self._connect_NW()

    def _connect_NW(self):
        west = self.cardinal.right.right.right
        print("ping1", west.dir)
        self.cardinal.left = west
        west.right = self.cardinal
        print("ping1", self.cardinal.left.dir)
        print("ping1", self.cardinal.left.right.dir)

    def _add_cardinals(self):
        self.cardinal.add("East").add("South").add("West")

    def rotate(self, hand):
        if hand == "Right":
            self.cardinal = self.cardinal.right
        else:
            self.cardinal = self.cardinal.left


class Robot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.compas = Compas()

    def rotate(self, hand):
        self.compas.rotate(hand)

    def advance(self, dist):
        if self.compas.cardinal.dir == "North":
            self.y += dist
        elif self.compas.cardinal.dir == "South":
            self.y -= dist
        elif self.compas.cardinal.dir == "East":
            self.x += dist
        else:
            self.x -= dist
        return self

    def action(self, move):
        "apply rotate or advance"
        if type(move) == int:
            self.advance(move)
        else:
            self.rotate(move)
        return self

    def actions(self, moves):
        for move in moves:
            self.action(move)
        return self

    def standing_home(self):
        return self.x == 0 and self.y == 0 and self.compas.cardinal.dir == "North"

    def returns_home(self, moves, times) -> bool:
        for _ in range(times):
            if self.actions(moves).standing_home():
                print(times, " to home")
                return True
        print("No luck")
        return False


moves = [1, "Right", 1]
mike = Robot("Mike")
mike.returns_home(moves, 10)
print(mike.standing_home())
print(mike.x)
print(mike.y)
print(mike.compas.cardinal.dir)
