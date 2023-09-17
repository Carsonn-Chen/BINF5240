# method 1
def comp(nuc):
    nucleotides = 'ACGTacgtNn'
    complements = 'TGCAtgcaNn'
    i = nucleotides.find(nuc)
    if i >= 0:
        return complements[i]
    return nuc

def reverse_complement(seq):
    rc = ""
    for i in seq:
        rc = comp(i) + rc
    return rc

# method 2
def reverse_complement_sequence(seq):
    complement_dict = {'N': 'N', 'n': 'n','A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    rc = ""
    for i in seq:
        rc = complement_dict[i] + rc
    return rc

#method 3
def complement(nuc):
    if nuc == 'A' or nuc == 'a':
        comp = 'T'
    elif nuc == 'T' or nuc == 't':
        comp = 'A'
    elif nuc == 'C' or nuc == 'c':
        comp = 'G'
    elif nuc == 'G' or nuc == 'g':
        comp = 'C'
    elif nuc == 'N' or nuc == 'n':
        comp = nuc
    return comp

def re_comp(seq):
    rc = ""
    for i in seq[::-1]:
        rc = rc + complement(i)
    return rc

Seq = "ATGGTCGATCTatggtcgatctn"
print(reverse_complement(Seq))
print(reverse_complement_sequence(Seq))
print(re_comp(Seq))
