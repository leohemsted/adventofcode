import itertools

PART_ONE = False

def part_one(triangle_file):
    return (map(int, line.split()) for line in triangle_file)

def part_two(triangle_file):
    triangle_buffer = []
    for line in triangle_file:
        triangle_buffer.append(map(int, line.split()))

        if len(triangle_buffer) == 3:
            yield tuple(triangle_buffer[x][0] for x in range(3))
            yield tuple(triangle_buffer[x][1] for x in range(3))
            yield tuple(triangle_buffer[x][2] for x in range(3))
            triangle_buffer = []

parsing_fn = part_one if PART_ONE else part_two

print(
    sum(
        all(
            a + b > c
            for a, b, c in itertools.permutations(triangle)
        )
        for triangle in parsing_fn(open('day_3_input.txt'))
    )
)
