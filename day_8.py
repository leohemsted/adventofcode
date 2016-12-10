import re
import itertools
from functools import partial

WIDTH = 50
HEIGHT = 6

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
            '#' if screen[z][y_] else '.' for z in range(WIDTH))
        )
        x += '\n'
    x += '\n'
    return x


def get_command(line):
    """
    Return a callable pre-loaded with the arguments provided
    """
    RECT_STR = r'rect (?P<x>\d+)x(?P<y>\d+)'
    ROW_STR = r'rotate row y=(?P<y>\d+) by (?P<dist>\d+)'
    COL_STR = r'rotate column x=(?P<x>\d+) by (?P<dist>\d+)'
    rect_match = re.match(RECT_STR, line)
    row_match = re.match(ROW_STR, line)
    col_match = re.match(COL_STR, line)
    if rect_match:
        return partial(rect, int(rect_match.group('x')), int(rect_match.group('y')))
    if row_match:
        return partial(rotate_row, int(row_match.group('y')), int(row_match.group('dist')))
    if col_match:
        return partial(rotate_column, int(col_match.group('x')), int(col_match.group('dist')))

def count_lit_pixels():
    return sum(itertools.chain.from_iterable(screen))

data = open('day_8_input.txt')
test_data = [
    'rect 3x2',
    'rotate column x=1 by 1',
    'rotate row y=0 by 4',
    'rotate column x=1 by 1',
]
for line in data:
    x = get_command(line)
    print(x)
    x()
    print(screen)

print(count_lit_pixels())
