# DNA is cool
dna_sequence = 'gcatgacgttattacgactctgtgtggcgtctgctggg'

# Compute dependent values
first_nucleotide = dna_sequence[0]
last_nucleotide = dna_sequence[-1]
first_four_nucs = dna_sequence[0:4]
last_ten_nucs = dna_sequence[-10:]
sequence_length = len(dna_sequence)

# Output results
print("First nucleotide",first_nucleotide)
print("Last nucleotide",last_nucleotide)
print("First four nucleotides",first_four_nucs)
print("Last ten nucleotides",last_ten_nucs)
print("Sequence length",sequence_length)
