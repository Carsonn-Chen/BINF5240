import sys
forward_primer = sys.argv[1]
reverse_primer = sys.argv[2]
# print(forward_primer, reverse_primer)

def complement(nuc):
    nucleotides = 'ACTG'
    complements = 'TGAC'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverseComplement(seq):
    seq = seq.upper()
    newseq = ''
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

print("The reverse complement sequence of forward primer is", reverseComplement(forward_primer))
print("The reverse complement sequence of reverse primer is", reverseComplement(reverse_primer))
