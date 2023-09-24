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

def translation(seq):
    seqlen = len(seq)
    seq = seq.upper()
    amino_acid_seq = ["","",""]
    for j in range(0, 3):
        for i in range(j, seqlen, 3):
            codon = seq[i: i+3]
            if len(codon) == 3:
                if 'N' in codon:
                    pos = codon.find('N')
                    codon[pos] = 'A'
                    tmp = codons[codon]
                    flag = True
                    for k in 'CTG':
                        codon[pos] = k
                        if codons[codon] != tmp:
                            flag = False
                    if flag:
                        amino_acid_seq[j] = amino_acid_seq[j] + tmp
                    else:
                        amino_acid_seq[j] = amino_acid_seq[j] + 'X'
                else:    
                    amino_acid_seq[j] = amino_acid_seq[j]+codons[codon]
    return amino_acid_seq
print(amino_acid_seq)
