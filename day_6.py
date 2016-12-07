import itertools
import collections

print(
    ''.join(
        collections.Counter(letters).most_common(1)[0][0]
        for letters in itertools.zip_longest(*open('day_6_input.txt'))
    )
)
