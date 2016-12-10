import itertools


def get_abas(s):
    letter_counts = [(k, len(list(g))) for k, g in itertools.groupby(s)]
    # for all
    for i in range(1, len(letter_counts) - 1):
        if (
            letter_counts[i][1] == 1 and
            letter_counts[i - 1][0] == letter_counts[i + 1][0]
        ):
            yield ''.join([letter_counts[i - 1][0], letter_counts[i][0], letter_counts[i + 1][0]])


def get_bab(aba):
    return ''.join([aba[1], aba[0], aba[1]])

def chunk_ip_addr(ip_address):
    hypernets = []
    sequences = []

    # a[b]c becomes ['a', 'b]c']
    for chunk in ip_address.split('['):
        if ']' in chunk:
            # reassign chunk to discard the hypernet from the normal sequences
            hypernet, chunk = chunk.split(']')
            hypernets.append(hypernet)
        sequences.append(chunk)

    return sequences, hypernets


def has_aba(ip_address):
    sequences, hypernets = chunk_ip_addr(ip_address)

    for sequence in sequences:
        for aba in get_abas(sequence):
            bab = get_bab(aba)
            if any(bab in hypernet for hypernet in hypernets):
                return True
    return False



print(sum(has_aba(ip_address) for ip_address in open('day_7_input.txt')))
