codon = "ATG"

lower_codon = codon.lower()
print(lower_codon)

lower_codon_backwards = lower_codon[-1] + lower_codon[-2] + lower_codon[-3]
print(lower_codon_backwards)

'''
tmp = lower_codon[-1:-4:-1]
print(tmp)
'''
