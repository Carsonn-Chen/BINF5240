start_codon = "ATG"
sequence = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

pos = sequence.find(start_codon.lower())
print(pos)
pos_frame = pos % 3
print(pos_frame)
