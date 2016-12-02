input_str = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5"

SECOND_PART = True

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

dirs = [NORTH, WEST, SOUTH, EAST]


location = (0,0)
orientation_index = 0

visited_locations = list()

def turn(direction):
    global orientation_index
    if direction == 'L':
        orientation_index -= 1
    elif direction == 'R':
        orientation_index += 1
    orientation_index %= 4

def move(distance, direction):
    global location

    for i in range(1, distance + 1):
        location = (
            location[0] + (direction[0]),
            location[1] + (direction[1])
        )
        if location in visited_locations:
            from pprint import pprint
            pprint(location)
            pprint(visited_locations)
            if SECOND_PART:
                raise StopIteration
        else:
            visited_locations.append(location)

try:
    for instruction in input_str.replace(' ', '').split(','):
        turn(instruction[0])

        move(int(instruction[1:]), dirs[orientation_index])
finally:
    print( abs(location[0]) + abs(location[1]))
