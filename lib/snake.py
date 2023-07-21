from . import Matrix
from .direction import Direction


class Snake(Matrix):
    DEFAULT_INITIAL_LENGTH = 3
    GEM_VALUE = 2
    direction = Direction.EAST.value
    gem_location = None
    offsets = {
        Direction.EAST.value: (1, 0,),
        Direction.SOUTH.value: (0, 1,),
        Direction.WEST.value: (-1, 0,),
        Direction.NORTH.value: (0, -1,),
    }

    def __init__(self, width: int = 31, height: int = 19, length: int = DEFAULT_INITIAL_LENGTH):
        self.width = width
        self.height = height
        Matrix.__init__(self, rows=self.height, columns=self.width)
        self.snake = [(x, 0,) for x in range(0, length)]
        self.update()
        self.create_the_gem()

    def change_direction(self, direction: int):
        self.direction = direction

    def update(self):
        self.clear()
        self.create_snake()
        self.place_the_gem()

    def place_the_gem(self):
        if self.gem_location is not None:
            self.set(col=self.gem_location[0], row=self.gem_location[1], value=self.GEM_VALUE)

    def create_the_gem(self):
        import random
        self.gem_location = None

        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.at(col=x, row=y) == self.EMPTY_VALUE:
                self.gem_location = (x, y,)
                break

    def create_snake(self):
        for a in self.snake:
            self.set(*a)

    def step(self):
        offset = self.offsets[self.direction]
        head = self.snake[-1]
        head = (
            (head[0] + offset[0]) % self.columns,
            (head[1] + offset[1]) % self.rows,
        )

        if self.at(col=head[0], row=head[1]) == self.GEM_VALUE:
            self.create_the_gem()
        else:
            self.snake.pop(0)

        if head in self.snake:
            raise Exception('Invalid move.')

        self.snake.append(head)
        self.update()
