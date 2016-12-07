import itertools
import collections

PART_ONE = False

if PART_ONE:
    letter_fn = lambda x: collections.Counter(x).most_common(1)[0][0]
else:
    letter_fn = lambda x: collections.Counter(x).most_common()[-1][0]

print(
    ''.join(
        letter_fn(letters)
        for letters in itertools.zip_longest(*open('day_6_input.txt'))
    )
)
