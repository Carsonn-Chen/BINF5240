def read_seq_from_filename(filepath):
    try:
        seq_file = open(filepath)
        dna_seq = ''.join(seq_file.read().split())
        dna_seq = dna_seq.upper()
        return dna_seq
    except IndexError:
        print("Error reading file")
        exit(1)


def is_valid(seq):
    valid_nuc = ['A', 'T', 'C', 'G', 'N']
    for nuc in seq:
        if nuc not in valid_nuc:
            return False
    return True


def complement(seq):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
    try:
        return ''.join(complement_dict[base] for base in seq)
    except KeyError:
        print("Invalid base")
        exit(1)


def reversed_complement(seq):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
    return ''.join(complement_dict[base] for base in reversed(seq))


def reverse(seq):
    return ''.join(reversed(seq))


def gc_content(seq):
    g_count = seq.count('G')
    c_count = seq.count('C')
    return (g_count + c_count) / len(seq) * 100
