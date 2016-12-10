WIDTH = 12
HEIGHT = 4

class Screen(list):
    def __str__(self):
        return print_screen(self)

screen = Screen(
    [
        False for i in range(HEIGHT)
    ]
    for i in range(WIDTH)
)


def rect(x, y):
    """
    Set top left rectangle
    """
    for x_ in range(x):
        for y_ in range(y):
            screen[x_][y_] = True

def rotate_row(y, distance):
    for _ in range(distance):
        last_el = screen[-1][y]
        for x_ in range(WIDTH - 1, 0, -1):
            screen[x_][y] = screen[(x_ - 1) % WIDTH][y]
        screen[0][y] = last_el

def rotate_column(x, distance):
    for _ in range(distance):
        last_el = screen[x][-1]
        for y_ in range(HEIGHT - 1, 0, -1):
            screen[x][y_] = screen[x][(y_ - 1) % HEIGHT]
        screen[x][0] = last_el


def print_screen(screen):
    x = ' '.join(str(x).ljust(2) for x in range(WIDTH)) + '\n'
    for y_ in range(HEIGHT):
        x += ('  '.join(
            map(lambda z: '#' if screen[z][y_] else '.', range(WIDTH))
        ))
        x += '\n'
    x += '\n'
    return x



rect(x=3, y=2)
print(screen)
rotate_column(1, 1)
print(screen)
rotate_row(0, 4)
print(screen)
rotate_column(1, 1)
print(screen)
