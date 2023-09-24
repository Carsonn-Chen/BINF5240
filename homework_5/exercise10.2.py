def count_nucleotides(seq):
    nucleotide_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    for base in seq:
        if base in nucleotide_counts:
            nucleotide_counts[base] += 1

    sorted_counts = sorted(nucleotide_counts.items(), key=lambda x: x[1], reverse=True)

    for base, count in sorted_counts:
        print(f'{base}: {count}')


# Example usage:
input_sequence = "ATGCTAGCTAGCTAGCTA"
count_nucleotides(input_sequence)
