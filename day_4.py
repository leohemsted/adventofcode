import collections
import itertools
import re

TEST_DATA = [
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]'
]
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
            'name': match.group('name').replace('-', ''),
            'sector_id': match.group('sector_id'),
            'checksum': match.group('checksum')
        }

def most_common_alphabetical(counter):
    return itertools.chain.from_iterable(
        sorted(item[0] for item in items)
        for frequency, items in
        itertools.groupby(counter.most_common(), lambda x: x[1])
    )

def most_common_five(counter):
    return itertools.islice(most_common_alphabetical(counter), 5)

def valid_sector_ids(rooms):
    for room in rooms:
        counter = collections.Counter(room['name'])
        computed_checksum = ''.join(x[0] for x in most_common_five(counter))
        if room['checksum'] == computed_checksum:
            yield int(room['sector_id'])

print(sum(valid_sector_ids(get_rooms())))
