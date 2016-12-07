import itertools


def contains_abba(s):
    letter_counts = [(k, len(list(g))) for k, g in itertools.groupby(s)]
    # for all
    return any(
        letter_counts[i][1] == 2 and
        letter_counts[i - 1][0] == letter_counts[i + 1][0]
        for i in range(1, len(letter_counts) - 1)
    )


def has_abba(ip_address):
    hypernets = []
    sequences = []

    # a[b]c becomes ['a', 'b]c']
    for chunk in ip_address.split('['):
        if ']' in chunk:
            # reassign chunk to discard the hypernet from the normal sequences
            hypernet, chunk = chunk.split(']')
            hypernets.append(hypernet)
        sequences.append(chunk)

    return not any(contains_abba(s) for s in hypernets) and any(contains_abba(s) for s in sequences)


print(sum(has_abba(ip_address) for ip_address in open('day_7_input.txt')))
