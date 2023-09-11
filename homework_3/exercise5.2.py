seq1 = "TTGAGTAGACGCGTCTACTCAA"
seq2 = "TTGAGTAGACGTCGTCTACTCAA"
seq3 = "ATATATATATATATAT"
seq4 = "ATCTATATATATGTAT"

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

tmp = seq4
if tmp == reverseComplement(tmp):
    print("The primer", tmp, "is a reverse complement palindrome")
else:
    print("The primer", tmp, "isn't a reverse complement palindrome")
