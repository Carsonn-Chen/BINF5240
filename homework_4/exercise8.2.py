import sys
codon_name = sys.argv[1]
seq_name = sys.argv[2]
#print(codon_name, seq_name)

codon_table = {}
f = open(codon_name)
for i in f:
    tmp = i.split()
    codon_table[tmp[0]] = tmp[2]
f.close()
# print(codon_table)

codons = {}
starts = {}
aas_len = len(codon_table['AAs'])
for i in range(aas_len):
    codon = codon_table['Base1'][i] + codon_table['Base2'][i] + codon_table['Base3'][i]
    codons[codon] = codon_table['AAs'][i]
    starts[codon] = (codon_table['Starts'][i] == 'M')

f = open(seq_name)
seq = ''.join(f.read().split())
f.close()

seqlen = len(seq)
amino_acid_seq = ""
for i in range(0, seqlen, 3):
    codon = seq[i: i+3]
    amino_acid_seq = amino_acid_seq+codons[codon]

print(amino_acid_seq)
if starts[seq[0: 3]]:
    print("The initial codon is consistent with the codon table's start codons.")
else:
    print("The initial codon isn't consistent with the codon table's start codons.")
