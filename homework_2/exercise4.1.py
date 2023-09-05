codon = 'ATG'
codon_2 = 'atg'
codon_3 = 'GTA'
codon_4 = 'XYZ'
codon_5 = 'aaa'

first = codon[0]
second = codon[1]
third = codon[2]
reversed_codon = third + second + first

def complement(nuc):
    if nuc == 'A':
        comp = 'T'
    elif nuc == 'T':
        comp = 'A'
    elif nuc == 'C':
        comp = 'G'
    elif nuc == 'G':
        comp = 'C'
    else:
        comp = nuc
    return comp

re_com_codon = complement(reversed_codon[0]) + complement(reversed_codon[1]) + complement(reversed_codon[2])
print(re_com_codon)

def re_complement(codon):
    first = codon[0]
    second = codon[1]
    third = codon[2]
    reversed_codon = third + second + first
    re_com_codon = complement(reversed_codon[0]) + complement(reversed_codon[1]) + complement(reversed_codon[2])
    return re_com_codon

re_com_codon_2 = re_complement(codon)
print(re_com_codon_2)

def up_low_complement(nuc):
    if nuc == 'A':
        comp = 'T'
    elif nuc == 'T':
        comp = 'A'
    elif nuc == 'C':
        comp = 'G'
    elif nuc == 'G':
        comp = 'C'
    elif nuc == 'a':
        comp = 't'
    elif nuc == 't':
        comp = 'a'
    elif nuc == 'c':
        comp = 'g'
    elif nuc == 'g':
        comp = 'c'
    else:
        comp = nuc
    return comp

def up_low_re_complement(codon):
    first = codon[0]
    second = codon[1]
    third = codon[2]
    reversed_codon = third + second + first
    re_com_codon = up_low_complement(reversed_codon[0]) + up_low_complement(reversed_codon[1]) + up_low_complement(reversed_codon[2])
    return re_com_codon

print(up_low_re_complement(codon_2))
print(up_low_re_complement(codon_3))
print(up_low_re_complement(codon_4))
print(up_low_re_complement(codon_5))
