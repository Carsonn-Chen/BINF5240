seq = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAGXYZN"

def count_nucleotides(seq):
    nucleotide_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    for i in seq:
        nucleotide_counts[i] = nucleotide_counts.get(i, 0)+1

    sorted_counts = sorted(nucleotide_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


sorted_counts = count_nucleotides(seq)
for base, count in sorted_counts:
        print(f'{base}: {count}')

