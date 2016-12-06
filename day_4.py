import collections
import itertools
import re

PART_ONE = False

TEST_DATA = [
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]'
]

def part_one(valid_rooms):
    return sum(room['sector_id'] for room in valid_rooms)

def part_two(valid_rooms):
    decrypted = dict(
        (
            ''.join(caeser_cipher(room['name'], room['sector_id'])),
            room['sector_id']
        )
        for room in valid_rooms
    )
    from pprint import pprint
    pprint(decrypted)


def caeser_cipher(text, key):
    def shift_char(c, key):
        key %= 26
        if c == '-':
            return '-'
        else:
            char_code = ord(c) + key
            if char_code > ord('z'):
                char_code -= 26
            return chr(char_code)
    return ''.join(shift_char(c, key) for c in text)


part_fn = part_one if PART_ONE else part_two


def get_rooms():
    for room in open('day_4_input.txt'):
        match = re.match(
            (
                r'(?P<name>([a-z\-])+)'
                r'(?P<sector_id>[0-9]+)'
                r'\[(?P<checksum>[a-z]+)\]'
            ),
            room
        )
        yield {
            'orig': room,
            'name': match.group('name'),
            'sector_id': int(match.group('sector_id')),
            'checksum': match.group('checksum')
        }

def most_common_alphabetical(counter):
    return itertools.chain.from_iterable(
        sorted(item[0] for item in items)
        for frequency, items in
        itertools.groupby(counter.most_common(), lambda x: x[1])
    )

def most_common_five(sorted_counter):
    return itertools.islice(most_common_alphabetical(sorted_counter), 5)

def valid_rooms():
    for room in get_rooms():
        counter = collections.Counter(room['name'].replace('-', ''))
        computed_checksum = ''.join(x[0] for x in most_common_five(counter))
        if room['checksum'] == computed_checksum:
            yield room

print(part_fn(valid_rooms()))
