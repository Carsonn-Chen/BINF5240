start_codon = "ATG"
sequence = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

pos = sequence.find(start_codon.lower())+1
print("The position of the first start-codon in the sequence is ", pos)
pos_frame = pos%3
print("The translation frame of the first start-codon in the sequence is ", pos_frame)
